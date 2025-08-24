class NullColumnException(Exception):
    default_message=f"Column cannot be null"

    def __init__(self, message=default_message):
        self.message = message
        super().__init__(self.message)