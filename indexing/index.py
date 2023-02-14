from argparse import ArgumentParser
import json
from typing import Any

from indexing.enums.index_names import IndexName
from indexing.indexers.index_to_indexer_mapping import INDEX_TO_INDEXER_MAPPING
from shared.es.es_client import ES_CLIENT as es
from indexing.mappings.mappings import ESMappings



def index(index_name: str, data: list, indexer_args: dict[str, Any]):
    indexer_class = INDEX_TO_INDEXER_MAPPING.get(index_name)

    indexer = indexer_class(index_name=index_name, data=data, **indexer_args)
    
    # check if index already exists. If not then create one with the correct mapping
    # If the index exists we assume it has the correct mapping already
    if not es.indices.exists(index=index_name):
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
    parser.add_argument("-m", "--model_name",
                        type=str,
                        help="hugging face model name",
                        required=False)

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

    dict_args = vars(args)
    del dict_args["index_name"]
    del dict_args["data_path"]

    index(index_name=index_name, data=data, indexer_args=dict_args) 