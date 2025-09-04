from chess.exception.null.base import NullException


class NullEncounterException(NullException):
    """
    NullEncounterException is raised when attempts to put null into a piece's
    encounter records.
    """

    ERROR_CODE = "NULL_ENCOUNTER_ERROR"
    DEFAULT_MESSAGE = f"Encounter cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"