from indexing.enums.index_names import IndexName
from indexing.indexers.bm25_indexer import BM25Indexer
from indexing.indexers.dpr_indexer import DPRIndexer
from indexing.indexers.t5_indexer import T5Indexer

INDEX_TO_INDEXER_MAPPING = {
    IndexName.UWATERLOO_COURSES_INDEX : BM25Indexer,
    IndexName.UWATERLOO_COURSES_INDEX_DPR: DPRIndexer,
    IndexName.UWATERLOO_COURSES_INDEX_T5: T5Indexer
}