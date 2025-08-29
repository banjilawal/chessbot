class NullRequestException(NullException):
    ERROR_CODE = "NULL_REQUEST_ERROR"
    DEFAULT_MESSAGE = f"Request cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class NullAttackRequestException(NullRequestException):
    ERROR_CODE = "NULL_ATTACK_REQUEST_ERROR"
    DEFAULT_MESSAGE = f"AttackRequest cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class NullOccupationRequestException(NullRequestException):
    ERROR_CODE = "NULL_OCCUPATION_REQUEST_ERROR"
    DEFAULT_MESSAGE = f"OccupationRequest cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class NullPromotionRequestException(NullRequestException):
    ERROR_CODE = "NULL_PROMOTION_REQUEST_ERROR"
    DEFAULT_MESSAGE = f"PromotionRequest cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"