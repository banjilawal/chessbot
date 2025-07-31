class ChessException(Exception):
    """Base exception with default message support"""
    default_message = "Chess game error occurred"

    def __init__(self, message=None, **kwargs):
        self.message = message or self.default_message
        self.context = kwargs  # Store any additional context
        super().__init__(self.message)

    def __str__(self):
        if self.context:
            return f"{self.message} [Context: {self.context}]"
        return self.message