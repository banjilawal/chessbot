class EncounteringSelfException(PieceException):
    """
    Prevents the piece from adding itself to the list of encounters.
    """

    ERROR_CODE = "SELF_ENCOUNTER_ERROR"
    DEFAULT_MESSAGE = "Piece cannot create an Encounter entry on itself"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"