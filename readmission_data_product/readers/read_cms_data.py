from typing import Dict, Any

import requests

class CMSDataReader:
    def __init__(self):
        self.hospital_readmissions_reduction_url = 'https://data.cms.gov/provider-data/api/1/datastore/query/9n3s-kdb3'

    def get_request(self, index=0) -> Dict[str, Any]:
        return requests.get(f'{self.hospital_readmissions_reduction_url}/{index}').json()
