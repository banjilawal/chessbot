# src/model/state/player/model/state/owner.py

"""
Module: model.state.player.model.owner
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from model import StateModel


class Player(StateModel):
    """
    Role:Controller

    Responsibilities:
    1.  Directs movement of tokens in a Team's roster on a Board.
    2.  Forwards requests from the user to a Game.
    
    Super Class:
    None

    # PROVIDES:
        *   current_team: -> Optional[Team]

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   designation (string)
        *   games (UniqueGameDataService)
        *   team_assignment (TeamDatabase)

    # INHERITED ATTRIBUTES:
    None
    """
    _id: int
    _name: str
    _current_team: Team
    _teams: TeamDatabase
    
    def player(
            self,
            id: int,
            name: str,
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   teams (TeamDatabase)
        # RETURNS:
            None
        Raises:
        """
        method = "PlayerQueryService.owner"
        self._id = id
        self._name = name
        self._teams = TeamDatabase()
        self._current_team = self._teams.current_team
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name
    
    @property
    def teams(self) -> TeamDatabase:
        return self._teams
    
    @property
    def current_team(self) -> Optional[Team]:
        return self._teams.current_team
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Player):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self.id)
    
    # def __str__(self):
    #     total_games = self.team_service.size()
    #     total_games_str = f"total games:{total_games}" if total_games > 0 else ""
    #
    #     current_side = "" if self._current_team is None else \
    #         f" curren_team:[{self._current_team.id}, {self._current_team.team_schema.color}"
    #     return (
    #         f"Owner[id:{self.timestamp}"
    #         f" designation:{self._name}"
    #         f"{current_side}"
    #         f"{total_games_str}"
    #         f"]"
    #     )
    
    # owner.order_move(
    #   owner=TeamFinder.searcher(
    #     data_owner=self._team_name,
    #     search_category=SearchCategory.ROSTER,
    #     map=TeamSearchContext(visitor_name="BN1")
    #   ),
    #   square_name="C8"
    # )
    #
    # # Which internally uses your transactional system:
    # # 1. SearchRouter returns Result[Token]
    # # 2. Validates inputs
    # # 3. Creates MoveEvent
    # # 4. Executes via TravelTransaction
    # # 5. Returns TransactionResult with rollback safety
    
    def move_token(self, token_name: str, destination: Coord):
        method = "Player.move_token"
        
        try:
            validation = NameValidator.search_service(token_name)
            if not validation.is_success():
                raise validation.exception
            
            result = self._current_team.find_token_by_name(token_name)
            if not result.is_success():
                raise result.exception
            
            token = cast(Token, result.payload)
            
            # if discover is None:
            #   raise TokenNotFoundException(
            #     f"{method}: {TokenNotFoundException.MSG} at index {array_index}"
            #   )
            
            if token.current_position is None:
                raise TokenCoordNullException(f"{method}: {TokenCoordNullException.MSG}")
            
            if isinstance(token, CombatantToken) and token.victor is not None:
                raise PrisonerEscapeException(f"{method}: Cannot move {token.designation} it has been captured.")
            
            validation = CoordValidator.search_service(destination)
            if not validation.is_success():
                raise validation.exception
            
            if token.current_position == destination:
                raise AlreadyAtDestinationException(f"{method}: {AlreadyAtDestinationException.MSG}")
            
            token.rank.walk(token=token, destination=destination)
        
        except (NullTokenException, ConflictingTeamException) as e:
            raise AddTokenException(f"{method}: {AddTokenException.MSG}")
