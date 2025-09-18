from typing import TypeVar, cast, Sequence, TYPE_CHECKING

from chess.piece import Piece
from chess.common import IdValidator
from chess.search import SearchResult
from chess.commander import Commander, CommanderValidator
from chess.team import TeamProfile, NullTeamProfileException
from chess.exception import (
    NullNumberException, NullStringException, IdValidationException, BrokenRelationshipException
)

class Team:
    _id:int
    _commander: 'Commander'
    _profile: TeamProfile
    _roster: list['Piece']
    _hostages: list['Piece']

    def __init__(self, team_id: int, commander: 'Commander', profile: TeamProfile):
        method = "Team.__init__"

        if profile is None:
            raise NullTeamProfileException(f"{method}: {NullTeamProfileException.DEFAULT_MESSAGE}")

        id_validation = IdValidator.validate(team_id)
        if not id_validation.is_success():
            raise id_validation.exception

        commander_validation = CommanderValidator.validate(commander)
        if not commander_validation.is_success():
            raise commander_validation.exception

        self._id = cast(int, id_validation.payload)
        self._commander = cast(Commander, commander_validation.payload)
        self._profile = profile
        self._roster = []


        if self not in commander.teams.items:
            commander.teams.push_side(self)

        if self not in commander.teams.items:
            raise BrokenRelationshipException(f"{method}:{BrokenRelationshipException.DEFAULT_MESSAGE}")


    @property
    def id(self) -> int:
        return self._id


    @property
    def commander(self) -> 'Commander':
        return self._commander


    @property
    def profile(self) -> TeamProfile:
        return self._profile


    @property
    def roster(self) -> Sequence['Piece']:
        """
        Returns a read-only view of the team's roster. The returned sequence is safe to
        iterate and index, but mutating it will not affect the original roster.
        """

        return self._roster.copy()


    @property
    def hostages(self) -> Sequence['Piece']:
        """
        Returns a read-only view of the team's rostages. The returned sequence is safe to
        iterate and index, but mutating it will not affect the original hostage list.
        """

        return self._hostages.copy()


    def find_by_roster_number(self, roster_number: int) -> SearchResult['Piece']:
        method = f"{self.__class__.__name__}.find_by_roster"

        """
        Find a piece with the roster_number. 

        Args:
           roster_number (int): There are 16 chess pieces per team. jersey_range = [0,15]

        Returns:
            SearchResult: If the piece with jersey is found 

        Raises:
             NullNumberException
             PieceNotFountException
        """
        try:
            if roster_number is None:
                raise NullNumberException(f"{method}: {NullNumberException.DEFAULT_MESSAGE}")

            piece = next((member for member in self._roster if member.roster_number == roster_number), None)
            if piece is not None:
                return SearchResult(payload=piece)

            # returns empty search result
            return  SearchResult()

        except Exception as e:
            return SearchResult(exception=e)


    def find(self, piece_id: int) -> SearchResult['Piece']:
        method = "Team.find_piece_by_id"

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
            raise TeamSearchException(f"{method}: {TeamSearchException.DEFAULT_MESSAGE}")


    def find_piece_by_name(self, name: str) -> Result['Piece']:
        method = "Team.find_piece_by_name"

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
            raise TeamSearchException(f"{method} {TeamException.DEFAULT_MESSAGE}") from e


    def find_piece_by_coord(self, coord: Coord) -> Result['Piece']:
        method = "Team.find_piece_by_coord"

        """
        Find a piece whose current position matches coord. If none of 
        the team's pieces are at the coord returns None.
        
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
            raise TeamSearchException(f"{method} {TeamException.DEFAULT_MESSAGE}") from e


    def add_to_roster(self, piece: Piece):
        method = "Team.add_to_roster"

        """
        A newly constructed piece uses Team.add_piece to add itself to the team's roster. Team.roster returns
        a read-only copy of the list. This is the only mutator that can directly access the array.

        Args:
            piece (Piece): validated piece added to the team's roster

        Raises:
            NullPieceException: if the piece is null
            InvalidTeamAssignmentException: if piece.team does not match the team instance
        """
        try:
            if piece is None:
                raise NullPieceException(f"{method} cannot add a null piece to the team")

            if not piece.team == self:
                raise ConflictingTeamException(f"{method}: {ConflictingTeamException.DEFAULT_MESSAGE}")

            if piece not in self._roster:
                  self._roster.append(piece)

        except (NullPieceException, ConflictingTeamException) as e:
            raise AddPieceException(f"{method}: {AddPieceException.DEFAULT_MESSAGE}") from e




    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Team):
            return False
        return self._id == other.id


    def __hash__(self):
        return hash(self._id)


    def __str__(self):
        return f"Team[id:{self._id} commander:{self._commander.name} {self._profile}"