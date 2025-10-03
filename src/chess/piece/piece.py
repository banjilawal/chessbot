"""
Module: piece
Author: Banji Lawal
Created: 2025-09-28
Purpose:
    Defines the Piece class hierarchy for the chess engine, including abstract and
    concrete pieces such as KingPiece and CombatantPiece. Pieces track identity, team
    membership, rank, and board position, and manage interactions with other pieces.

Contents:
    - Piece: Abstract base class representing a chess piece with position and rank.
    - KingPiece: Concrete subclass representing a king piece.
    - CombatantPiece: Concrete subclass representing a piece capable of capturing others.
    - CoordStack, Discovery, Discoveries: Supporting classes for tracking piece positions
      and discoveries.
    - Validators and exceptions related to piece creation and validation.

Notes:
    This module is part of the chess.piece package. Validation exceptions are defined
    in PieceValidator and related exception classes. Piece objects are designed to be
    immutable in their core properties.
"""



from abc import ABC
from typing import Optional, cast

from chess.rank import Rank
from chess.coord import Coord
from chess.common import IdValidator, NameValidator, NameValidationException, InvalidIdException
from chess.piece import CoordStack, Discovery, DiscoveryBuilder, Discoveries, PieceValidator, AutoDiscoveryException
from chess.team import Team, TeamValidator, InvalidTeamException

__all__ = [
    'Piece',
    'KingPiece',
    'CombatantPiece'
]



class Piece(ABC):
    """An abstract base class representing a single chess discover.

    A `Piece` is a fundamental game entity that has an identity, belongs to a `Team`, and has a `Rank` that
    defines its movement logic. It tracks its position on the board and records discoveries with other pieces.
    The class is designed to be immutable with respect to its core properties (`id`, `name`, `rank`, `team`).

    Attributes:
        _id (int): A unique identifier for the discover.
        _name (str): The name of the discover (e.g., "Pawn", "Queen").
        _team (Team): The team the discover belongs to.
        _rank (Rank): The rank that defines the discover's movement strategy.
        _roster_number (int): The discover's number on its team's roster.
        _current_position (Optional[Coord]): The current coordinate of the discover on the board.
        _discoveries (Discoveries): A log of discoveries with other pieces.
        _positions (CoordStack): A stack of the discover's historical coordinates.
    """

    _id: int
    _name: str
    _team: Team
    _rank: Rank
    _captor: 'Piece'
    _roster_number: int
    _current_position: Coord
    _discoveries: Discoveries
    _positions: CoordStack

    def __init__(self, piece_id: int, name: str, rank: Rank, team: Team):
        """Initializes a Piece instance.

        Args:
            piece_id (int): A unique identifier for the discover.
            name (str): The name of the discover.
            rank (Rank): The rank that defines the discover's movement strategy.
            team (Team): The team the discover belongs to.

        Raises:
            InvalidIdException: If `discovery_id` fails validation checks.
            NameValidationException: If `name` fails validation checks.
            InvalidTeamException: If `team` fails validation checks.
        """

        method = "Piece.__init__"

        id_validation = IdValidator.validate(piece_id)
        if not id_validation.is_success():
            raise InvalidIdException(f"Piece.__init__: {InvalidIdException.DEFAULT_MESSAGE}")

        name_validation = NameValidator.validate(name)
        if not name_validation.is_success():
            raise NameValidationException(
                f"Piece.__init__: {NameValidationException.DEFAULT_MESSAGE}"
            )

        team_validation = TeamValidator.validate(team)
        if not team_validation.is_success():
            raise InvalidTeamException(f"Piece.__init__: {InvalidTeamException.DEFAULT_MESSAGE}")

        team = cast(Team, team_validation.payload)

        self._id = cast(int, id_validation.payload)
        self._name = cast(str, name_validation.payload)
        self._rank = rank

        self._roster_number = len(team.roster) + 1
        self._team = team

        self._discoveries = Discoveries()
        self._positions = CoordStack()
        self._current_position = self._positions.current_coord

        if self not in team.roster:
            team.add_to_roster(self)


    @property
    def id(self) -> int:
        """The unique ID of the discover."""
        return self._id


    @property
    def name(self) -> str:
        """The name of the discover."""
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
    def discoveries(self) -> Discoveries:
        """A log of items the piece discovered when the piece is scanning the board or moving."""
        return self._discoveries


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
        """
        Checks if another piece belongs to an opposing team.

        Args:
            piece (Piece): The other piece to compare.
        
        Returns:
            bool: `True` if the piece belongs to a different team, otherwise `False`.
        
        Raises:
            NullPieceException: If the provided discover is `None`.
        """
        method = "Piece.is_enemy"

        validation = PieceValidator.validate(piece)
        if not validation.is_success():
            raise validation.exception

        return self._team != piece.team


    def record_discovery(self, piece: 'Piece'):
        """
        Records a piece discovered when scanning or moving on the board.

        Args:
            piece (Piece): The item that this piece has found.

        Raises:
            NullPieceException: If the found piece is `None`.
            AutoDiscoveryException: If the piece wants tries to record a discover of itself.
        """
        method = "Piece.record_discovery"
        
        try:
            build_outcome = DiscoveryBuilder.build(observer=self, subject=piece)
            if not build_outcome.is_success():
                raise build_outcome.exception
            discovery = build_outcome.payload

            if discovery not in self._discoveries:
                self._discoveries.record_discovery(discovery)

        except Exception as e:
            raise e


    def __str__(self) -> str:
        """Returns a string representation of the Piece."""
        return (
            f"Piece[id:{self._id} "
            f"name:{self._name} "
            f"rank:{self._rank.name} "
            f"team:{self._team.scheme.name} "
            f"position:{self._positions.current_coord} "
            f"moves:{self._positions.size()}]"
        )


class KingPiece(Piece):
    """A concrete subclass representing a king piece."""
    _is_checked: bool
    _is_checkmated: bool

    def __init__(self, piece_id: int, name: str, rank: 'Rank', team: 'Team'):
        super().__init__(piece_id, name, rank, team)
        self._is_checked = False
        self._is_checkmated = False


    @property
    def is_checked(self) -> bool:
        return self._is_checked

    @property
    def is_checkmated(self) -> bool:
        return self._is_checkmated

    @is_checked.setter
    def is_checked(self, is_checked: bool):
        self._is_checked = is_checked

    @is_checkmated.setter
    def is_checkmated(self, is_checkmated: bool):
        if self._is_checked:
            self._is_checkmated = is_checkmated
        else:
            raise Exception("Cannot set checkmated status if not checked")


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



