from enum import Enum, auto


class TokenLocation(Enum):
    ROSTER = auto(),
    HOSTAGES = auto(),
    BOTH_DATASETS = auto(),
    NEITHER_DATASET = auto(),
    