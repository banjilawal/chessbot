from chess.common import Result

class SearchResult(Result):

    def is_not_found(self) -> bool:
        """"""
        return not (self._exception is None and self._payload is None)


    def __str__(self):
        if self.is_success():
            return f"Result(SUCCESS: {self._payload})"
        elif self.is_not_found():
            return "Result(NOT_FOUND)"
        else:
            return f"Result(FAILURE: {self._exception}"