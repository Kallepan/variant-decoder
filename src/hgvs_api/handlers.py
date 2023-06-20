import hgvs.variantmapper
import hgvs.assemblymapper
import hgvs.parser
import hgvs.dataproviders.uta
import hgvs.exceptions

import os 
import logging

HOST = os.environ.get("UTA_HOST", "localhost")
PORT = os.environ.get("UTA_PORT", "30120")
VERSION = os.environ.get("UTA_VERSION", "20210129")
DB_URL = f"postgresql://anonymous@{HOST}:{PORT}/uta/{VERSION}"

class HGVSWrapper:
    def __init__(self) -> None:
        self.hdp = hgvs.dataproviders.uta.connect(db_url=DB_URL)
    
    def translate_cDNA_to_genomic(self, cDNA: str, hg38: bool = False) -> str:
        logging.info(f"Translating {cDNA} to genomic coordinates to hg38={hg38} or hg19={not hg38}")
        
        # Create a parser
        parser = hgvs.parser.Parser()
        # Parse the cDNA variant
        try:
            hgvs_c = parser.parse_hgvs_variant(cDNA)
        except hgvs.exceptions.HGVSParseError as e:
            logging.error(f"Could not parse {cDNA}")
            raise e
        
        # Create a mapper
        if hg38:
            assembly_name = "GRCh38"
        else:
            assembly_name = "GRCh37"

        am = hgvs.assemblymapper.AssemblyMapper(
            self.hdp,
            assembly_name=assembly_name,
            alt_aln_method="splign",
            replace_reference=True,
        )

        # Map the cDNA variant to genomic coordinates
        try:
            hgvs_g = am.c_to_g(hgvs_c)
        except hgvs.exceptions.HGVSDataNotAvailableError as e:
            logging.error(f"Could not map {cDNA} to genomic coordinates")
            raise e

        # Return the genomic variant
        return str(hgvs_g)