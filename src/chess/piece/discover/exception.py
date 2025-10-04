from chess.exception import ChessException, RollbackException, NullException, BuilderException, ValidationException


__all__ = [
    'DiscoveryException',
    'NullDiscoveryException',
    'DiscoveryBuilderException',
    'CircularDiscoveryException',
    'AddingValidDiscoveryFailedException',
    'AddDuplicateDiscoveryException',
    'AddNullDiscoveryException',
    
# === DISCOVERY EXCEPTIONS WITH ROLLBACK===
    'DiscoveryRolledBackException',
    'CircularDiscoveryRolledBackException',
    'DuplicateDiscoveryRolledBackException',
    'AddNullDiscoveryRolledBackException'
]

class DiscoveryException(ChessException):
    """
    Super class of all exceptions a Board object raises. Do not use directly. Subclasses
    give details useful for debugging. This class exists primarily to allow catching
    all board exceptions
    """
    ERROR_CODE = "DISCOVERY_ERROR"
    DEFAULT_MESSAGE = "Discovery instance raised an err"
    
class InvalidDiscoveryException(DiscoveryException, ValidationException):
    """
    Raised by DiscoveryValidator if board fails sanity checks. Exists primarily to catch all
    exceptions raised validating an existing board
    """
    ERROR_CODE = "DISCOVERY_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Discovery validate failed."

class NullDiscoveryException(DiscoveryException, NullException):
    """
    Raised if an entity, method, or operation requires a discovery but gets null instead.
    """
    ERROR_CODE = "NULL_DISCOVERY_ERROR"
    DEFAULT_MESSAGE = f"Discovery cannot be null"


class DiscoveryBuilderException(DiscoveryException, BuilderException):
    """
    Raised when BoardBuilder encounters an err while building a team. Exists primarily to
    catch all exceptions raised building a new board
    """
    ERROR_CODE = "DISCOVERY_BUILDER_ERROR"
    DEFAULT_MESSAGE = "DiscoveryBuilder raised an err"


class CircularDiscoveryException(DiscoveryException):
    """Raised if an actor scans itself."""
    ERROR_CODE = "OBSERVER_CIRCULAR_SCAN_ERROR"
    DEFAULT_MESSAGE = "An actor cannot discover itself"


class AddingValidDiscoveryFailedException(DiscoveryException):
    """Raised if a  could not be added to the team's roster"""
    ERROR_CODE = "ADDING_DISCOVERY_FAILED_ERROR"
    DEFAULT_MESSAGE = "Adding a validated discovery failed"


class AddDuplicateDiscoveryException(DiscoveryException):
    """Raised if an actor tries adding a discovery twice."""
    ERROR_CODE = "ADD_DUPLICATE_DISCOVERY_ERROR"
    DEFAULT_MESSAGE = "The discovery has already been added to the list"
    
class AddNullDiscoveryException(DiscoveryException):
    """Raised if an actor tries adding a null or empty discovery to its list"""
    ERROR_CODE = "ADD_NULL_DISCOVERY_ERROR"
    DEFAULT_MESSAGE = "Cannot add a null discovery to the list"

# === DISCOVERY EXCEPTIONS WITH ROLLBACK===
class DiscoveryRolledBackException(DiscoveryException, RollbackException):
    """
    Any inconsistencies a discovery introduces into a transaction need to be rolled back.
    This is the super class of a discovery mutator operations, methods, or fields that raise
    errors. Do not use directly. Subclasses give details useful for debugging. This class
    exists primarily to allow catching all Discovery exceptions that happen when a failed
    transaction must be rolled back.
    """
    ERROR_CODE = "DISCOVERY_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Discovery raised an err. Transaction rolled back"


class CircularDiscoveryRolledBackException(DiscoveryException):
    """
    Raised if an actor scans itself during an ACID transaction. The
    transaction was rolled back before raising this err.
    """
    ERROR_CODE = "OBSERVER_CIRCULAR_SCAN_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "An actor cannot discover itself. Transaction rolled back."


class DuplicateDiscoveryRolledBackException(DiscoveryException):
    """
    Raised if a transaction attempts adding a discovery twice to an actor. The
    transaction was rolled back before raising this err.
    """
    ERROR_CODE = "ADD_DUPLICATE_DISCOVERY_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "The discovery has already been added to the list. Transaction rolled back."
    )


class AddNullDiscoveryRolledBackException(DiscoveryException):
    """
    Raised if a transaction attempts adding a null or empty discovery to an
    actor's list. The transaction was rolled back before raising this err.
    """
    ERROR_CODE = "ADD_NULL_DISCOVERY_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Cannot add a null discovery to the list. Transaction rolled back."
    
    
class DiscoveryRolledBackException(DiscoveryException, RollbackException):
    """
    RollBackCapture exceptions should be raised in ACID transactions where a capture can
    raise an err. Do not use directly. Subclasses give details useful for debugging.
    """
    ERROR_CODE = "CAPTURE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Capture raised an err. "

class CaptureFriendRolledBackException(DiscoveryRolledBackException):
    """
    Raised if a transaction attempts capturing a friend. The transaction
    was rolled back before raising this err.
    """
    ERROR_CODE = "FRIEND_CAPTURE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Cannot capture a friend. Transaction rollback performed."
    )

class KingCaptureRolledBackException(DiscoveryRolledBackException):
    """
    Raised if a transaction attempts capturing an enemy. Kings can only be checked or
    checkmated. 
    """
    ERROR_CODE = "KING_CAPTURE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "An enemy king cannot be captured. It can only be checked or checkmated. "
        "Transaction rollback performed."
    )

class DoubleCaptureRolledBackException(DiscoveryRolledBackException):
    """
    Raised if a transaction attempts capturing an enemy combatant that is already
    a prisoner. The transaction was rolled back before raising this err.
    """
    ERROR_CODE = "DOUBLE_CAPTURE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Cannot capture a discovery that is already a prisoner. Transaction "
        "rollback performed."
    )

class UnsetCaptureRolledBackException(DiscoveryRolledBackException):
    """
    Raised if a transaction attempts setting prisoner's captor field null.
    The transaction was rolled back before raising this err.
    """
    ERROR_CODE = "UNSET_CAPTOR_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Cannot set a prisoner's captor to null. A captured discovery cannot be freed. "
        "Transaction rollback performed."
    )
