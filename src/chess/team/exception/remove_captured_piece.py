

class RemoveCombatantException(TeamException):
    """
    If Team.remove_captured_combatant fails this exception is raised.
    """

    ERROR_CODE = "REMOVE_CAPTURED_COMBATANT_ERROR"
    DEFAULT_MESSAGE = "Could not remove the captured hostage from the roster"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
