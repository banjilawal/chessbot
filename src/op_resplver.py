from enum import Enum
from typing import Union

from chess.common import Result
from chess.builder import BuildResult
from chess.search import SearchResult


class OperationResolver(Enum):
    @staticmethod
    def resolve(outcome: Union[Result, BuildResult, SearchResult], logger: logging.Logger) -> Union[Any, Exception]:
        """
        Logs the outcome and returns the payload or exception.
        """

        if outcome.is_success():
            logger.info("✅ Success: %s", getattr(outcome, 'payload', None))
            return getattr(outcome, 'payload', None)

        exception = outcome.exception or ValueError("Unknown failure")
        logger.error("❌ Failure: %s", str(exception), exc_info=exception)
        return exception
