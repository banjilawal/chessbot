from logging import exception
from typing import List, TYPE_CHECKING, cast, Sequence, Optional

from assurance.exception.validation.coord import CoordValidationException
from assurance.exception.validation.id import IdValidationException
from assurance.result.base import Result
from assurance.validators.coord import CoordValidator
from assurance.validators.id import IdValidator
from assurance.validators.competitor import CompetitorValidator
from assurance.validators.piece import PieceValidator
from chess.config.game import SideProfile
from chess.exception.null.number import NullNumberException
from chess.exception.null.piece import NullPieceException
from chess.exception.null.side_profile import NullSideProfileException
from chess.exception.null.text import NullStringException
from chess.exception.piece import PrisonerEscapeException, PieceCoordNullException, AlreadyAtDestinationException
from chess.exception.search import PieceNotFoundException
from chess.exception.side import SideSearchException, SideException, ConflictingSideException, AddPieceException, \
    RemoveCombatantException
from chess.exception.stack import BrokenRelationshipException
from chess.exception.text import BlankStringException
from chess.geometry.coord import Coord

if TYPE_CHECKING:
    from chess.competitor.model import Competitor
    from chess.token.model import Piece, CombatantPiece


class Side:
    _id:int
    _controller:'Competitor'
    _profile:SideProfile
    _roster:list['Piece']
    _hostages:list['Piece']

    def __init__(self, side_id:int, controller:'Competitor', profile:SideProfile):
        method = "Team.__init__"

        if profile is None:
            raise NullSideProfileException(f"{method}: {NullSideProfileException.DEFAULT_MESSAGE}")

        id_validation = IdValidator.validate(side_id)
        if not id_validation.is_success():
            raise id_validation.exception

        side_id = cast(int, id_validation.payload)

        competitor_validation = CompetitorValidator.validate(controller)
        if not competitor_validation.is_success():
            raise competitor_validation.exception

        from chess.competitor.model import Competitor
        controller = cast(Competitor, competitor_validation.payload)

        self._id = side_id
        self._controller = controller
        self._profile = profile
        self._roster = []


        if self not in controller.sides_played.items:
            controller.sides_played.push_side(self)

        if self not in controller.sides_played.items:
            raise BrokenRelationshipException(f"{method}:{BrokenRelationshipException.DEFAULT_MESSAGE}")


    @property
    def id(self) -> int:
        return self._id


    @property
    def controller(self) -> 'Competitor':
        return self._controller


    @property
    def profile(self) -> SideProfile:
        return self._profile


    @property
    def roster(self) -> Sequence['Piece']:
        """
        Returns a read-only view of the side's roster. The returned sequence is safe to
        iterate and index, but mutating it will not affect the original roster.
        """

        return self._roster.copy()


    @property
    def hostages(self) -> Sequence['Piece']:
        """
        Returns a read-only view of the side's rostages. The returned sequence is safe to
        iterate and index, but mutating it will not affect the original hostage list.
        """

        return self._hostages.copy()


    def find_piece_by_jersey(self, jersey:int) -> Result['Piece']:
        method = "Side.find_piece_by_jersey"

        """
        Find a piece with the jersey. 

        Args:
           jersey (int): There are 16 chess pieces per side. jersey_range = [0,15]

        Returns:
            Result: If the piece with jersey is found 

        Raises:
             NullNumberException
             PieceNotFountException
        """
        try:
            if jersey is None:
                raise NullNumberException(f"{method}: {NullNumberException.DEFAULT_MESSAGE}")

            for piece in self._roster:
                if piece.jersey == jersey:
                    return Result(payload=piece)
            return Result(
                exception=PieceNotFoundException(f"{method}: {PieceNotFoundException.DEFAULT_MESSAGE}")
            )

        except (NullStringException, BlankStringException, PieceNotFoundException) as e:
            raise SideSearchException(f"{method} {SideException.DEFAULT_MESSAGE}") from e


    def find_piece_by_id(self, piece_id: int) -> Result['Piece']:
        method = "Side.find_piece_by_id"

        """
        Find a piece whose id matches

        Args:
           id (int): a valid id

        Returns:
            Piece: If a piece's id matches the target
            None: If no matches are found.

        Raises:
             IdValidationException 
        """
        try:
            validation = IdValidator.validate(id)
            if not validation.is_success():
                raise validation.exception

            for piece in self._roster:
                return Result(payload=piece)
            return Result(
                exception=PieceNotFoundException(f"{method}: {PieceNotFoundException.DEFAULT_MESSAGE}")
            )

        except (IdValidationException, PieceNotFoundException) as e:
            raise SideSearchException(f"{method}: {SideSearchException.DEFAULT_MESSAGE}")


    def find_piece_by_name(self, name: str) -> Result['Piece']:
        method = "Side.find_piece_by_name"

        """
        Find a piece with the name

        Args:
           name (str): a nonnull string

        Returns:
            Piece: If a piece's current_position matches coord
            None: If no matches are found.

        Raises:
             NullStringException: if name is null.
             BlankStringException: if name is a empty string
        """
        try:
            if name is None:
                raise NullStringException(f"{method}: {NullStringException.DEFAULT_MESSAGE}")

            if len(name) == 0 or not name.strip():
                raise BlankStringException(f"{method}: {BlankStringException.DEFAULT_MESSAGE}")

            for piece in self._roster:
                if piece.name.upper() == name.upper():
                    return Result(payload=piece)
            return Result(
                exception=PieceNotFoundException(f"{method}: {PieceNotFoundException.DEFAULT_MESSAGE}")
            )

        except (NullStringException, BlankStringException, PieceNotFoundException) as e:
            raise SideSearchException(f"{method} {SideException.DEFAULT_MESSAGE}") from e


    def find_piece_by_coord(self, coord: Coord) -> Result['Piece']:
        method = "Side.find_piece_by_coord"

        """
        Find a piece whose current position matches coord. If none of 
        the side's pieces are at the coordinate returns None.
        
        Args:
            coord (Coord): validated Coord used for search
            
        Returns:
            Piece: If a piece's current_position matches coord
            None: If no matches are found.
            
        Raises:
             CoordValidationException: if coord fails sanity checks.
        """
        try:
            validation = CoordValidator.validate(coord)
            if not validation.is_success():
                raise validation.exception

            for piece in self._roster:
                if piece.current_position == coord:
                    return Result(payload=piece)
            return Result(
                exception=PieceNotFoundException(f"{method}: {PieceNotFoundException.DEFAULT_MESSAGE}")
            )
        
        except CoordValidationException as e:
            raise SideSearchException(f"{method} {SideException.DEFAULT_MESSAGE}") from e


    def add_to_roster(self, piece: Piece):
        method = "Side.add_to_roster"

        """
        A newly constructed piece uses Side.add_piece to add itself to the side's roster. Side.roster returns
        a read-only copy of the list. This is the only mutator that can directly access the array.

        Args:
            piece (Piece): validated piece added to the side's roster

        Raises:
            NullPieceException: if the piece is null
            ConflictingSideException: if piece.side does not match the side instance
        """
        try:
            if piece is None:
                raise NullPieceException(f"{method} cannot add a null piece to the side")

            if not piece.side == self:
                raise ConflictingSideException(f"{method}: {ConflictingSideException.DEFAULT_MESSAGE}")

            if piece not in self._roster:
                  self._roster.append(piece)

        except (NullPieceException, ConflictingSideException) as e:
            raise AddPieceException(f"{method}: {AddPieceException.DEFAULT_MESSAGE}") from e


    def remove_captured_combatant(self, combatant: CombatantPiece) -> Result[CombatantPiece]:
        method = "Side.remove_captured_combatant"

        """
        Removes a captured piece from the roster

        Args:
            combatant (CombatantPiece): captured piece to remove from the roster

        Raises:
            TypeError: if the validated piece cannot be cast to CombatantPiece 
            PieceValidationException: If the piece fails sanity checks
            ConflictingSideException: If the piece is not on the correct side

            RemoveCombatantException wraps any preceding exception 
        """
        try:
            validation = self._validate_combatant(combatant)
            if not validation.is_success():
                raise validation.exception

            if not combatant.side == self:
                raise ConflictingSideException(f"{method}: {ConflictingSideException.DEFAULT_MESSAGE}")

            if combatant.captor is not None:
                raise Exception()

            if combatant not in self._roster:
                raise Exception()

            self._roster.remove(combatant)
            return Result(payload=combatant)
        except (
            TypeError,
            NullPieceException,
            ConflictingSideException
        ) as e:
            raise RemoveCombatantException(
                f"{method:}: {RemoveCombatantException.DEFAULT_MESSAGE}"
            ) from e


    def add_hostage(self, enemy: CombatantPiece):
        method = "Side.add_hostage"

        """
        A newly constructed piece uses Side.add_piece to add itself to the side's roster. Side.roster returns
        a read-only copy of the list. This is the only mutator that can directly access the array.

        Args:
            enemy (CombatantPiece): enemy to put in hostage list

        Raises:
            TypeError: if the validated piece cannot be cast to CombatantPiece 
            PieceValidationException: If the piece fails sanity checks
            ConflictingSideException: If the piece is not on the correct side

            RemoveCombatantException wraps any preceding exception 
        """
        try:
            validation = self._validate_combatant(combatant=enemy)
            if not validation.is_success():
                raise validation.exception

            if enemy.side == self:
                raise ConflictingSideException(f"{method}: {ConflictingSideException.DEFAULT_MESSAGE}")

            if enemy.captor is None:
                raise Exception()

            if not enemy.captor.side == self:
                raise Exception()

            if enemy in self._hostages:
                raise Exception()

            self._hostages.append(enemy)

        except (NullPieceException, ConflictingSideException) as e:
            raise AddPieceException(f"{method}: {AddPieceException.DEFAULT_MESSAGE}") from e


    def _validate_combatant(self, combatant: CombatantPiece) -> Result[CombatantPiece]:
        method = "Side._validate_combatant"

        validation = PieceValidator.validate(combatant)
        if not validation.is_success():
            return Result(exception=validation.exception)

        if not isinstance(validation.payload, CombatantPiece):
            return Result(exception=TypeError(f"{method} Expected a CombatantPiece, got {type(t).__name__}"))

        return Result(payload=combatant)



    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Side):
            return False
        return self._id == other.id


    def __hash__(self):
        return hash(self._id)


    def __str__(self):
        return f"Team[id:{self._id} competitor:{self._controller.name} {self._profile}"