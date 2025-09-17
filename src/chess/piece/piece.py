from abc import ABC
from typing import Optional, cast

from chess.rank import Rank
from chess.coord import Coord, CoordStack
from chess.exception import ChessException, IdValidationException, NameValidationException
from chess.piece import Encounter, EncounterScan, PieceValidator
from chess.team import Team, TeamValidator, TeamValidationException



class Piece(ABC):
    """An abstract base class representing a single chess piece.

    A `Piece` is a fundamental game entity that has an identity, belongs to a `Team`, and has a `Rank` that
    defines its movement logic. It tracks its position on the board and records encounters with other pieces.
    The class is designed to be immutable with respect to its core properties (`id`, `name`, `rank`, `team`).

    Attributes:
        _id (int): A unique identifier for the piece.
        _name (str): The name of the piece (e.g., "Pawn", "Queen").
        _team (Team): The team the piece belongs to.
        _rank (Rank): The rank that defines the piece's movement strategy.
        _roster_number (int): The piece's number on its team's roster.
        _current_position (Optional[Coord]): The current coordinate of the piece on the board.
        _encounters (EncounterScan): A log of encounters with other pieces.
        _positions (CoordStack): A stack of the piece's historical coordinates.
    """

    _id: int
    _name: str
    _team: Team
    _rank: Rank
    _captor: 'Piece'
    _roster_number: int
    _current_position: Coord
    _encounters: EncounterScan
    _positions: CoordStack

    def __init__(self, piece_id: int, name: str, rank: Rank, team: Team):
        method = ("Piece.__init__"
                  "")
        """Initializes a Piece instance.

        Args:
            piece_id (int): A unique identifier for the piece.
            name (str): The name of the piece.
            rank (Rank): The rank that defines the piece's movement strategy.
            team (Team): The team the piece belongs to.

        Raises:
            IdValidationException: If `piece_id` fails validation checks.
            NameValidationException: If `name` fails validation checks.
            TeamValidationException: If `team` fails validation checks.
        """

        id_validation = IdValidator.validate(piece_id)
        if not id_validation.is_success():
            raise IdValidationException(f"Piece.__init__: {IdValidationException.DEFAULT_MESSAGE}")

        name_validation = NameValidator.validate(name)
        if not name_validation.is_success():
            raise NameValidationException(
                f"Piece.__init__: {NameValidationException.DEFAULT_MESSAGE}"
            )

        side_validation = TeamValidator.validate(team)
        if not side_validation.is_success():
            raise TeamValidationException(f"Piece.__init__: {TeamValidationException.DEFAULT_MESSAGE}")

        team = cast(Team, side_validation.payload)

        self._id = cast(int, id_validation.payload)
        self._name = cast(str, name_validation.payload)
        self._rank = rank

        self._roster_number = len(team.roster) + 1
        self._team = team

        self._encounters = EncounterScan()
        self._positions = CoordStack()
        self._current_position = self._positions.current_coord

        if self not in team.roster:
            team.add_to_roster(self)


    @property
    def id(self) -> int:
        """The unique ID of the piece."""
        return self._id


    @property
    def name(self) -> str:
        """The name of the piece."""
        return self._name


    @property
    def roster_number(self) -> int:
        """The piece's number on its team's roster."""
        return self._roster_number


    @property
    def team(self) -> 'Team':
        """The team the piece belongs to."""
        return self._team


    @property
    def rank(self) -> 'Rank':
        """The rank that defines the piece's movement strategy."""
        return self._rank


    @property
    def positions(self) -> CoordStack:
        """A stack of the piece's historical coordinates."""
        return self._positions


    @property
    def current_position(self) -> Optional[Coord]:
        """The current coordinate of the piece."""
        return self._positions.current_coord


    @property
    def encounters(self) -> EncounterScan:
        """A log of encounters with other pieces."""
        return self._encounters


    def __eq__(self, other: object) -> bool:
        """Compares two Piece instances for equality based on their ID."""
        if other is self:
            return True
        if not isinstance(other, Piece):
            return NotImplemented
        return self._id == other.id


    def __hash__(self) -> int:
        """Returns the hash value of the Piece based on its ID."""
        return hash(self._id)


    def is_enemy(self, piece: 'Piece') -> bool:
        method = "Piece.is_enemy"

        """Checks if another piece belongs to an opposing team.

        Args:
            piece (Piece): The other piece to compare.

        Returns:
            bool: `True` if the piece belongs to a different team, otherwise `False`.

        Raises:
            NullPieceException: If the provided piece is `None`.
        """
        validation = PieceValidator.validate(piece)
        if not validation.is_success():
            raise validation.exception

        return self._team != piece.team


    def record_encounter(self, piece: 'Piece'):
        method = "Piece.record_encounter"

        """Records an encounter with another piece.

        Args:
            piece (Piece): The piece that this piece has encountered.

        Raises:
            NullPieceException: If the provided piece is `None`.
            SelfEncounterException: If the piece encounters itself.
        """

        validation = PieceValidator.validate(piece)
        if not validation.is_success():
            raise validation.exception

        if piece is self:
            raise SelfEncounterException(f"{method}: {SelfEncounterException.DEFAULT_MESSAGE}")

        self._encounters.add_encounter(Encounter(piece))


    def __str__(self) -> str:
        """Returns a string representation of the Piece."""
        return (
            f"Piece[id:{self._id} "
            f"name:{self._name} "
            f"rank:{self._rank.name} "
            f"team:{self._team.profile.name} "
            f"position:{self._positions.current_coord} "
            f"moves:{self._positions.size()}]"
        )


class KingPiece(Piece):

    def __init__(self, piece_id: int, name: str, rank: 'Rank', side: 'Team'):
        super().__init__(piece_id, name, rank, side)


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, KingPiece):
            return self.id == other.id


class CombatantPiece(Piece):
    _captor: Optional[Piece]

    def __init__(self, piece_id: int, name: str, rank: 'Rank', team: 'Team'):
        super().__init__(piece_id, name, rank, team)
        self._captor = None


    @property
    def captor(self) -> Optional[Piece]:
        return self._captor


    @captor.setter
    def captor(self, captor: Piece):
        method = "Captor.@setter.captor"

        if captor is None:
            raise SetCaptorNullException(f"{method}: {SetCaptorNullException.DEFAULT_MESSAGE}")

        if self._captor is not None:
            raise PrisonerReleaseException(f"{method}: {PrisonerReleaseException.DEFAULT_MESSAGE}")

        self._captor = captor


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, CombatantPiece):
            return self.id == other.id



