from argparse import ArgumentParser
import json

from indexing.enums.index_names import IndexName
from shared.es.es_client import ES_CLIENT as es
from indexing.mappings.mappings import ESMappings

from indexing.indexers.bm25_indexer import BM25Indexer
from indexing.indexers.dpr_indexer import DPRIndexer
from indexing.indexers.t5_indexer import T5Indexer


def index(index_name: str, data: list):

    INDEX_TO_INDEXER_MAPPING = {
        IndexName.UWATERLOO_COURSES_INDEX : BM25Indexer,
        IndexName.UWATERLOO_COURSES_INDEX_DPR: DPRIndexer,
        IndexName.UWATERLOO_COURSES_INDEX_T5: T5Indexer
    }

    indexer_class = INDEX_TO_INDEXER_MAPPING.get(index_name)

    indexer = indexer_class(index_name=index_name, data=data)
    
    # delete index if already exists to prevent double indexing
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
    
    mapping = ESMappings.get_mapping_from_index_name(index_name.value)
    assert mapping is not None
    es.indices.create(index=index_name, body=mapping)

    print(f"Starting Indexing into {index_name}")
    indexer.index()
    print("Completed Indexing")


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-i", "--index_name",
                        type=str,
                        help="The index name where to store the data",
                        required=True)
    parser.add_argument("-d", "--data_path",
                        type=str,
                        help="Path to JSON file containing data",
                        required=True)

    args = parser.parse_args()

    # get index_name
    index_name = IndexName(args.index_name)

    # load data
    data = []
    with open(args.data_path, "r") as f:
        data = json.load(f)
    
    if not data:
        print("No data")
        exit()

    index(index_name=index_name, data=data) 