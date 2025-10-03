# chess/collection/exception.py
from chess.exception import ChessException

# Export all exceptions
__all__ = [
    # General Chess collection exceptions
    'CollectionException',
    'EmptyCollectionException',
    'NullAdditionException',
    'DuplicateItemException',
    'CorruptedCollectionException',
    'CollectionSizeConflictException',

    # Exceptions raised when there is an inconsistency between the o
    # ne-to-many sides of a bidirectional relationship
    'RelationshipException',
    'BrokenRelationshipException',

    'GameListException',

    # CoordStack related exceptions
    'CoordStackException',
    'PopEmptyStackException',
    'DuplicatePushException',
    'PushNullException',
    'InconsistentCurrentCoordException',

    # EncounterList relate exceptions
    'EncounterLogException',
    'NullEncounterException'
]

class CollectionException(ChessException):
    """Base exception for all collection-related errors."""
    ERROR_CODE = "COLLECTION_ERROR"
    DEFAULT_MESSAGE = "Collection transaction failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

# === GENERIC COLLECTION OPERATIONS ===

class EmptyCollectionException(CollectionException):
    """Raised when trying to access items from an empty collection."""
    ERROR_CODE = "EMPTY_COLLECTION_ERROR"
    DEFAULT_MESSAGE = "Cannot access items from empty collection"

class NullAdditionException(CollectionException):
    """Raised when trying to add null/None item to collection."""
    ERROR_CODE = "NULL_ITEM_ERROR"
    DEFAULT_MESSAGE = "Cannot add null item to collection"

class DuplicateItemException(CollectionException):
    """Raised when trying to add duplicate item to collection that doesn't allow duplicates."""
    ERROR_CODE = "DUPLICATE_ITEM_ERROR"
    DEFAULT_MESSAGE = "Cannot add duplicate item to collection"

class CorruptedCollectionException(CollectionException):
    """Raised when collection's internal state is corrupted."""
    ERROR_CODE = "CORRUPTED_COLLECTION_ERROR"
    DEFAULT_MESSAGE = "Collection internal state is corrupted"

class CollectionSizeConflictException(CollectionException):
    """Raised when collection size methods return conflicting results."""
    ERROR_CODE = "COLLECTION_SIZE_CONFLICT_ERROR"
    DEFAULT_MESSAGE = "Collection size methods return conflicting results"


# === STACK-SPECIFIC EXCEPTIONS ===

class CoordStackException(CollectionException):
    """Base exception for stack operations."""
    ERROR_CODE = "STACK_ERROR"
    DEFAULT_MESSAGE = "Stack transaction failed"


class PopEmptyStackException(CoordStackException):
    """Raised when trying to pop from empty stack."""
    ERROR_CODE = "POP_EMPTY_STACK_ERROR"
    DEFAULT_MESSAGE = "Cannot pop from empty stack"


class DuplicatePushException(CoordStackException):
    """Raised when trying to push duplicate to stack that doesn't allow duplicates."""
    ERROR_CODE = "DUPLICATE_PUSH_ERROR"
    DEFAULT_MESSAGE = "Cannot push duplicate item to stack"


class PushNullException(CoordStackException):
    """Raised when trying to push null item to stack."""
    ERROR_CODE = "PUSH_NULL_ERROR"
    DEFAULT_MESSAGE = "Cannot push null item to stack"


class InconsistentCurrentCoordException(CoordStackException):
    ERROR_CODE = "INCONSISTENT_CURRENT_COORD_ERROR"
    DEFAULT_MESSAGE = "Current coordinate state is inconsistent"


# === SPECIFIC COLLECTION EXCEPTIONS ===


class GameListException(CollectionException):
    """Game list specific errors."""
    ERROR_CODE = "GAME_LIST_ERROR"
    DEFAULT_MESSAGE = "Game list transaction failed"

class EncounterLogException(CollectionException):
    """Encounter log specific errors."""
    ERROR_CODE = "ENCOUNTER_LOG_ERROR"
    DEFAULT_MESSAGE = "Encounter log transaction failed"

class NullEncounterException(EncounterLogException):
    ERROR_CODE = "NULL_ENCOUNTER_ERROR"
    DEFAULT_MESSAGE = "Cannot add null encounter to log"

# === RELATIONSHIP EXCEPTIONS ===

class RelationshipException(ChessException):
    """Base exception for relationship consistency errors."""
    ERROR_CODE = "RELATIONSHIP_ERROR"
    DEFAULT_MESSAGE = "Relationship consistency exception"

class BrokenRelationshipException(RelationshipException):
    ERROR_CODE = "BROKEN_RELATIONSHIP_ERROR"
    DEFAULT_MESSAGE = "Broken bidirectional relationship detected"

