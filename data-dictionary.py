# To use this library, you first need to install Pydantic:
# pip install pydantic

from pydantic import BaseModel, Field, validator
from typing import Optional


# --- Custom Exceptions (You can define these in a separate file) ---

class NullException(Exception):
    """Exception raised for null values."""
    pass


class RowOutOfBoundsException(Exception):
    """Exception raised for row index out of bounds."""
    default_message = "Row index is out of bounds."
    pass


class ColumnOutOfBoundsException(Exception):
    """Exception raised for column index out of bounds."""
    default_message = "Column index is out of bounds."
    pass


# --- Constants for Chessboard Size ---
# These are assumed to be defined globally in your project.
ROW_SIZE = 8
COLUMN_SIZE = 8


# --- Core Data Models ---

class Delta(BaseModel):
    """
    Represents a null-pkg for shifting coordinates.

    Attributes:
        row_delta (int): The amount to add to a coord's row.
        column_delta (int): The amount to add to a coord's column.
    """
    row_delta: int = Field(...)
    column_delta: int = Field(...)

    class Config:
        frozen = True  # Makes the model immutable

    def __mul__(self, scalar: int) -> 'Delta':
        """
        Multiplies the Delta null-pkg by a scalar value.
        """
        if scalar is None:
            raise NullException("Scalar cannot be null for multiplication.")

        new_row_delta = self.row_delta * scalar
        new_column_delta = self.column_delta * scalar

        return Delta(row_delta=new_row_delta, column_delta=new_column_delta)


class Coordinate(BaseModel):
    """
    Represents an immutable coord on a chessboard.

    Attributes:
        row (int): The 0-based row index.
        column (int): The 0-based column index.
    """
    # Pydantic's Field handles validators for bounds checks.
    row: int = Field(..., ge=0, lt=ROW_SIZE)
    column: int = Field(..., ge=0, lt=COLUMN_SIZE)

    class Config:
        frozen = True  # Makes the model immutable
        # You can add a custom validator to catch Pydantic's
        # validators errors and re-raise them as your custom exceptions.
        # @validator('*', pre=True)
        # def check_bounds(cls, v):
        #     # Example of re-raising for 'row' field
        #     # You would need a more complex state to see which field failed.
        #     # This is often not needed as Pydantic's errors are clear.
        #     if 'row' in cls.__fields__ and not (0 <= v < ROW_SIZE):
        #         raise RowOutOfBoundsException()
        #     return v

    def shift(self, delta: Delta) -> 'Coord':
        """
        Creates a new Coord shifted by a given Delta.

        Args:
            delta (Delta): A null-pkg for the shift.

        Returns:
            Coordinate: A new Coord instance.

        Raises:
            NullException: If the provided null-pkg is null.
            ValidationError: If the new coord is out of bounds.
        """
        if delta is None:
            raise NullException("Delta cannot be null.")

        new_row = self.row + delta.row_delta
        new_column = self.column + delta.column_delta

        # Pydantic's automatic validators will raise an error if the new
        # coord is outside the defined bounds.
        return Coordinate(row=new_row, column=new_column)


class CartesianDistance(BaseModel):
    """
    Calculates the squared Euclidean distance between two coordinates.

    Attributes:
        p (Coordinate): The first coord.
        q (Coordinate): The second coord.
        distance (int): The squared Euclidean distance, calculated automatically.
    """
    p: Coordinate
    q: Coordinate
    distance: Optional[int] = None  # Will be calculated by the validator

    class Config:
        frozen = True  # Makes the model immutable

    @validator('distance', always=True)
    def calculate_distance(cls, v: Optional[int], values) -> int:
        """
        Pydantic validator to calculate the distance automatically upon creation.
        """
        p = values.get('p')
        q = values.get('q')

        if p is None or q is None:
            raise NullException("Both 'p' and 'q' must be valid coordinates.")

        return ((p.row - q.row) ** 2) + ((p.column - q.column) ** 2)


# Import necessary models from the main data definition library for type hinting
from data_definition_library import Coordinate, ChessPiece


# --- Custom Pydantic Validators ---

class ScoutReport(BaseModel):
    """
    Encapsulates the findings of a single Scout's mission.

    Attributes:
        id (UUID): A unique identifier for the report.
        scout (Piece): The chess piece that performed the survey.
        locations (List[Coordinate]): A list of coordinates representing the piece's legal moves.
    """
    id: UUID = Field(default_factory=uuid4)
    scout: ChessPiece
    locations: List[Coordinate] = Field(default_factory=list)

    class Config:
        frozen = True  # Making the model immutable


class Scout(BaseModel):
    """
    Represents a single ChessPiece on a scouting mission.

    Attributes:
        id (int): A unique identifier for the scout instance.
        chess_piece (Piece): The chess piece the scout is observing.
    """
    id: int = Field(..., gt=0)
    chess_piece: ChessPiece

    class Config:
        frozen = True  # Making the model immutable


class ExplorationMaster(BaseModel):
    """
    Orchestrates the scouting process.

    Attributes:
        scouts (List[Scout]): A list of all active scout instances.
    """
    scouts: List[Scout] = Field(default_factory=list)

    class Config:
        frozen = True  # Making the model immutable


class ScoutReportSorter(BaseModel):
    """
    Holds the list of scout reports to be sorted.

    Attributes:
        reports (List[ScoutReport]): The collected reports from the scouts.
    """
    reports: List[ScoutReport] = Field(default_factory=list)

    class Config:
        frozen = True  # Making the model immutable


class TargetSelector(BaseModel):
    """
    The final component for selecting the best move.

    Attributes:
        sorted_reports (List[ScoutReport]): The list of scout reports, sorted by priority.
    """
    sorted_reports: List[ScoutReport] = Field(default_factory=list)

    class Config:
        frozen = True  # Making the model immutable


from pydantic import BaseModel, Field, validator
from typing import Optional, List, TYPE_CHECKING, Literal
from uuid import UUID, uuid4
from abc import ABC, abstractmethod

# Forward references for models defined later in this file.
# Pydantic handles these automatically, but explicit type checking
# can be useful for external tools.
if TYPE_CHECKING:
    from chess.piece.piece import Piece
    from chess.rank.rank import Rank
    from chess.rank.walk import Walk

# --- Constants for Chessboard Size ---
ROW_SIZE = 8
COLUMN_SIZE = 8


# --- Core Game Geometry and State Models ---

class Delta(BaseModel):
    """
    Represents an immutable null-pkg for shifting coordinates.
    """
    row_delta: int = Field(...)
    column_delta: int = Field(...)

    class Config:
        frozen = True


class Coordinate(BaseModel):
    """
    Represents an immutable coord on a chessboard with bounds checking.
    """
    row: int = Field(..., ge=0, lt=ROW_SIZE)
    column: int = Field(..., ge=0, lt=COLUMN_SIZE)

    class Config:
        frozen = True


class CartesianDistance(BaseModel):
    """
    Calculates the squared Euclidean distance between two coordinates.
    """
    p: Coordinate
    q: Coordinate
    distance: Optional[int] = None

    class Config:
        frozen = True

    @validator('distance', always=True)
    def calculate_distance(cls, v: Optional[int], values) -> int:
        p = values.get('p')
        q = values.get('q')
        if p is None or q is None:
            raise ValueError("Both 'p' and 'q' must be valid coordinates.")
        return ((p.row - q.row) ** 2) + ((p.column - q.column) ** 2)


class CoordinateStack(BaseModel):
    """
    An immutable stack for storing a ChessPiece's movement history.
    """
    _stack: List[Coordinate] = Field(default_factory=list)

    class Config:
        frozen = True

    def push_coordinate(self, coordinate: Coordinate) -> 'CoordStack':
        new_stack = self._stack + [coordinate]
        return CoordinateStack(_stack=new_stack)

    def current_coordinate(self) -> Optional[Coordinate]:
        return self._stack[-1] if self._stack else None


class Rank(BaseModel):
    """
    An immutable data model for a ChessPiece's validation, defining its identity.
    """
    rank_name: str = Field(...)
    capture_value: int = Field(..., ge=0)
    # Note: The `Walk` logic is handled by separate classes, not included in the data model.

    class Config:
        frozen = True


class ChessPiece(BaseModel):
    """
    Represents an immutable chess piece and its current state.
    """
    id: int = Field(..., gt=0)
    name: str = Field(...)
    rank: Rank
    color: Literal['white', 'black'] = Field(...)
    coordinate_stack: CoordinateStack
    captor: Optional['Piece'] = None
    move_count: int = Field(..., ge=0)
    has_moved: bool = Field(...)
    is_captured: bool = Field(...)
    obstructions: List['Piece'] = Field(default_factory=list)
    valid_moves: List[Coordinate] = Field(default_factory=list)

    class Config:
        frozen = True
        arbitrary_types_allowed = True


class Square(BaseModel):
    """
    Represents a single square on the chessboard.
    """
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=2)
    coordinate: Coordinate
    occupant: Optional[ChessPiece] = None

    class Config:
        frozen = True


class ChessBoard(BaseModel):
    """
    Manages the state of the chessboard as a collection of Squares.
    """
    id: int = Field(..., gt=0)
    squares: List[List[Square]]

    class Config:
        frozen = True

    @validator('squares')
    def check_board_size(cls, v):
        if len(v) != ROW_SIZE or not all(len(row) == COLUMN_SIZE for row in v):
            raise ValueError(f"ChessBoard must be a {ROW_SIZE}x{COLUMN_SIZE} grid.")
        return v


# --- Engine-Related Data Models ---
# These models represent the data structures used by the game AI.

class ScoutReport(BaseModel):
    """
    Encapsulates the findings of a single Scout's mission.
    """
    id: UUID = Field(default_factory=uuid4)
    scout: ChessPiece
    locations: List[Coordinate] = Field(default_factory=list)

    class Config:
        frozen = True


class Scout(BaseModel):
    """
    Represents a single ChessPiece on a scouting mission.
    """
    id: int = Field(..., gt=0)
    chess_piece: ChessPiece

    class Config:
        frozen = True

