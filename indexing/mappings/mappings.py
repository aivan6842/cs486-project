import copy
from enum import Enum

from indexing.enums.index_names import IndexName

class ESMappings(dict, Enum):
    UWATERLOO_BM25_INDEX_MAPPING = \
        {
            "settings": {
                "similarity": {
                    "default": {"type": "BM25"}
                }
            },
            "mappings": {
                "properties" : {
                    "courseCode": {"type": "text"},
                    "courseName": {"type": "text"},
                    "courseDescription": {"type": "text"}
                }
            }
        }
    
    UWATERLOO_DPR_INDEX_MAPPING = \
        {
            "mappings": {
                "properties" : {
                    "courseCode": {"type": "text"},
                    "courseName": {"type": "text"},
                    "courseDescription": {"type": "text"},
                    "courseDescEncoding": {"type": "dense_vector", "dims": 768, "index": True, "similarity": "l2_norm"}
                }
            }
        }
    
    UWATERLOO_T5_INDEX_MAPPING = copy.deepcopy(UWATERLOO_DPR_INDEX_MAPPING)

    @classmethod
    def get_mapping_from_index_name(cls, index_name: str):
        name_to_mapping = {
            IndexName.UWATERLOO_COURSES_INDEX: cls.UWATERLOO_BM25_INDEX_MAPPING,
            IndexName.UWATERLOO_COURSES_INDEX_DPR: cls.UWATERLOO_DPR_INDEX_MAPPING,
            IndexName.UWATERLOO_COURSES_INDEX_T5: cls.UWATERLOO_T5_INDEX_MAPPING
        }

        return name_to_mapping.get(index_name)