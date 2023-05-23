import requests

ENSEMBL_URL = 'https://rest.ensembl.org'

def request(url, headers=None, params=None):
    if headers is None:
        headers = {
            "Content-Type": "application/json",
        }
    if params is None:
        params = {
            "content-type": "application/json"
        }
    response = requests.get(url, headers=headers, params=params)
    
    if not response.ok:
        response.raise_for_status()
    
    return response.json()

def main():
    """
        HG19: chr17 29508835 29508835
        HG38: chr17 31181817 31181817
                
        Current: NM_000267.3 c.730+32_730+33insT # ENST00000356175
        Desired: NC_000017:10.g.29508835dup
    """
    # This does not retrieve the correct data
    # The coordinates are off by almost 20000?
    # How? 
    mapping = request(f"{ENSEMBL_URL}/map/cdna/ENST00000356175/762..763")
    info = request(f"{ENSEMBL_URL}/lookup/id/ENST00000356175")
    
    print(mapping)
    print(info)


if __name__ == '__main__':
    main()