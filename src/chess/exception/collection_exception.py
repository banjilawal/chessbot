# chess/collection/err.py
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
  # ne-to-many sides of team bidirectional relationship
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
  """Base error for all collection-related errors."""
  ERROR_CODE = "COLLECTION_ERROR"
  DEFAULT_MESSAGE = "Collection transaction failed"

  def __init__(self, message=None):
    self.message = message or self.DEFAULT_MESSAGE
    super().__init__(self.message)

  def __str__(self):
    return f"[{self.ERROR_CODE}] {self.message}"

#======================# GENERIC COLLECTION OPERATIONS #======================#  

class EmptyCollectionException(CollectionException):
  """Raised when trying to access items from an empty collection."""
  ERROR_CODE = "EMPTY_COLLECTION_ERROR"
  DEFAULT_MESSAGE = "Cannot access items from empty collection"

class NullAdditionException(CollectionException):
  """Raised when trying to add null/None item to collection."""
  ERROR_CODE = "NULL_ITEM_ERROR"
  DEFAULT_MESSAGE = "Cannot add null item to collection"

class DuplicateItemException(CollectionException):
  """Raised when trying to add duplicate item to collection that doesn'candidate allow duplicates."""
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


#======================# STACK-SPECIFIC EXCEPTIONS #======================#  




#======================# SPECIFIC COLLECTION EXCEPTIONS #======================#  


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

#======================# RELATIONSHIP EXCEPTIONS #======================#  


