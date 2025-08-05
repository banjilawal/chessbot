from enum import Enum, auto


class Deployment(Enum):
    DEBUG = auto()
    PRODUCTION = auto()

    def handle_error(self, error: Exception):
        if self == Deployment.DEBU:
            raise RuntimeError(error)
        else:
            print("[WARNING]", error)