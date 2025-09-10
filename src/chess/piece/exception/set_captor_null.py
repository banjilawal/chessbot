class SetCaptorNullException(PieceException):
    """
    If the captor field has not been set its already null. I really want to prevent nulls being passed to
    Combatant.captor. This is for consistency. I don't just want an if that returns to caller when
    Combatant.captor == None and the caller tries to send null again. I want an exception to catch it. The
    exception name needs improvement.
    """

    ERROR_CODE = "CAPTURED_PIECE_ESCAPE_ERROR"
    DEFAULT_MESSAGE = "A captured piece cannot move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"