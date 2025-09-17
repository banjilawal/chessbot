from enum import Enum, auto
import logging


class Deployment(Enum):
    DEBUG = auto()
    PRODUCTION = auto()

    def handle_error(self, error: Exception):
        logger = logging.getLogger("AppLog")

        if self == Deployment.DEBUG:
            logger.exception("[EXCEPTION]", exec_info=error)
            raise RuntimeError(error)
        else:
            logger.warning(f"[WARNING]: {str(error)}")