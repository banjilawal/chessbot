from enum import EnumMeta, Enum, auto


class OperationResult(Enum):
    SUCCESS = auto()
    FAILURE = auto()