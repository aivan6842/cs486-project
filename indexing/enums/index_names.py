from enum import Enum

class IndexName(str, Enum):
    UWATERLOO_COURSES_INDEX = "uwaterloo-courses"
    UWATERLOO_COURSES_INDEX_DPR = "uwaterloo-courses-dpr"
    UWATERLOO_COURSES_INDEX_T5 = "uwaterloo-courses-t5"