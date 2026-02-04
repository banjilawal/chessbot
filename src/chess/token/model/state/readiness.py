from enum import Enum, auto


class ReadinessState(Enum):
    FREE = auto(),
    IN_CHECK = auto(),
    CHECKMATED = auto(),
    NOT_INITIALIZED = auto(),
    CAPTURE_ACTIVATED = auto(),
    HOSTAGE_MANIFEST_CREATED = auto(),
    HOSTAGE_MANIFEST_IN_DATABASE = auto(),
    DEACTIVATED = auto(),