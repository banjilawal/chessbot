from assurance.result import Result


class TransactionResult:
    def __init__(self, method_name: str, outcome: Result):
        self._method_name = method_name
        self._outcome = outcome

    @property
    def method_name(self) -> str:
        return self._method_name

    @property
    def outcome(self) -> Result:
        return self._outcome