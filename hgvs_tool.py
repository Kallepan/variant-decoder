import hgvs.parser
import hgvs.variantmapper
import hgvs.assemblymapper
import hgvs.dataproviders.uta
"""
    HG19: chr17 29508835 29508835
    HG38: chr17 31181817 31181817
            
    Current: NM_000267.3 c.730+32_730+33insT # ENST00000356175
    Desired: NC_000017:10.g.29508835dup
"""

def main():
    parser = hgvs.parser.Parser()
    
    # parse variant string to a Variant "object"
    hgvs_c = parser.parse_hgvs_variant('NM_000267.3:c.730+32_730+33insT')

    # connect to dataprovider
    hdp = hgvs.dataproviders.uta.connect(db_url="postgresql://anonymous@localhost:15032/uta/uta_20170117")

    vm_37 = hgvs.assemblymapper.AssemblyMapper(
        hdp, assembly_name="GRCh37", alt_aln_method="splign")
    vm_38 = hgvs.assemblymapper.AssemblyMapper(
        hdp, assembly_name="GRCh38", alt_aln_method="splign")
    
    var_g = vm_37.c_to_g(hgvs_c)
    print(var_g)
    var_g = vm_38.c_to_g(hgvs_c)
    print(var_g)

if __name__ == '__main__':
    main()