from elasticsearch import Elasticsearch

from shared.configs.elastic_search_config import ELASTIC_PASSWORD

def get_es_client() -> Elasticsearch:
    # Create the client instance
    es = Elasticsearch(
        "https://localhost:9200",
        ca_certs="config/certs/http_ca.crt",
        basic_auth=("elastic", ELASTIC_PASSWORD),
        verify_certs=False
    )
    return es


ES_CLIENT = get_es_client()