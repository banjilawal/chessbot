from chess.exception.base import ChessException
from chess.exception.piece import PieceException

"""
Super class for Hostage exceptions
"""
class HostageException(PieceException):
    """
    Super class for exceptions raised by Hostage objects
    """

    ERROR_CODE = "HOSTAGE_ERROR"
    DEFAULT_MESSAGE = "Hostage raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class HostageCaptorNullException(HostageException):
    """
    If the captor field of hostage is null HostageCaptorNullException is raised
    """

    ERROR_CODE = "HOSTAGE_CAPTOR_NULL_ERROR"
    DEFAULT_MESSAGE = "Hostage.captor field should not be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class RosterRemovalException(HostageException):
    """
    If a hostage is still on its team roster RosterRemovalException is raised
    """

    ERROR_CODE = "ROSTER_REMOVAL_ERROR"
    DEFAULT_MESSAGE = "The captured hostage has not been removed from the roster"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class HostageAdditionException(HostageException):
    """
    If the hostage is not added to their enemy's hostage list a
    HostageAdditionException is raised.
    """

    ERROR_CODE = "HOSTAGE_ADDITION_ERROR"
    DEFAULT_MESSAGE = "The prisoner has not been added to the hostage list"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class PrisonerEscapeException(HostageException):
    """
    Combatant hostages with attacker field not null cannot be moved. Attempts to move
    a captured hostage raises PrisonerEscapeException. This only applies to hostage hostages
    """

    ERROR_CODE = "MOVING_CAPTURED_HOSTAGE_ERROR"
    DEFAULT_MESSAGE = "Cannot move a captured hostage"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class PrisonerReleaseException(HostageException):
    """
    Combatant.captor field can only be set once. PrisonerReleaseException is thrown when an attempt to change
    combatant_hostage.captor != null to combatant_hostage.captor = None
    """

    ERROR_CODE = "RELEASING_CAPTURED_HOSTAGE_ERROR"
    DEFAULT_MESSAGE = "Cannot change CombatantHostage.captor to null once it has been set to an enemy hostage"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



class NullCaptorException(HostageException):
    """
    If the captor field has not been set its already null. I really want to prevent nulls being passed to
    Combatant.captor. This is for consistency. I don't just want an if that returns to caller when
    Combatant.captor == None and the caller tries to send null again. I want an exception to catch it. The
    exception name needs improvement.
    """

    ERROR_CODE = "CAPTURED_HOSTAGE_ESCAPE_ERROR"
    DEFAULT_MESSAGE = "A captured hostage cannot move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingNullHostageException(HostageException):
    """
    The Prisoner/Captor exceptions prevent domain logic violations on the captured side. Attacking
    exceptions constrain attacks. AttackingNullHostageException is raised if a hostage attacks something
    which does not exist.
    """

    ERROR_CODE = "ATTACKING_NULL_HOSTAGE_ERROR"
    DEFAULT_MESSAGE = "Cannot capture a a hostage that does not exist"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingPrisonerException(HostageException):
    """
    AttackingHostageException is raised when a captured hostage is attacked again."
    """

    ERROR_CODE = "ATTACKING_CAPTURED_HOSTAGE_ERROR"
    DEFAULT_MESSAGE = "Cannot capture a hostage already captured"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingKingException(HostageException):
    """
    Kings cannot be captured. KingHostage does not have a captor field. AttackingKingException is
    raised when a KingHostage is attacked. KingHostages can only be checked or checkmated.
    """

    ERROR_CODE = "ATTACKING_KING_EXCEPTION"
    DEFAULT_MESSAGE = "Cannot capture a king"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingFriendlyException(HostageException):
    """
    Friendly hostages on the same side cannot attack each other. AttackingFriendlyException is
    raised when a friendly is attacked.
    """
    ERROR_CODE = "ATTACKING_FRIENDLY_ERROR"
    DEFAULT_MESSAGE = "Cannot attack a friendly"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class DoublePromotionException(HostageException):
    """
    If a hostage with rank in [Pawn, King] has been promoted to Queen, DoublePromotionException
    is raised if there is a second attempt to promote the chess hostage.
    """

    ERROR_CODE = "DOUBLE_PROMOTION_ERROR"
    DEFAULT_MESSAGE = "Hostage is already promoted to Queen. It cannot be promoted again"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class SelfEncounterException(HostageException):
    """
    Prevents the hostage from adding itself to the list of encounters.
    """

    ERROR_CODE = "SELF_ENCOUNTER_ERROR"
    DEFAULT_MESSAGE = "Hostage cannot create an Encounter entry on itself"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class KingCheckStateException(HostageException):
    """
    This really should not be an exception. Its really supposed to be a warning to the king
    when its in check. This exception should never be thrown but its messages can be handy.
    """

    ERROR_CODE = "KING_CHECK_STATE"
    DEFAULT_MESSAGE = "A dead hostage cannot attack"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class KingCheckMateStateException(HostageException):
    """
    This really should not be an exception. Its really supposed to be a warning to indicate the
    game is over because the king is checkmated. This exception should never be thrown but its
    messages can be handy.
    """

    ERROR_CODE = "KING_CHECKMATE_STATE"
    DEFAULT_MESSAGE = "King checkmated"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


