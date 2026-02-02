import sys
from typing import List, cast

from chess.team import Team
from chess.team.service.service import TeamService
from chess.formation import Formation, FormationKey, FormationKeyService, FormationValidator, FormationServiceException
from chess.persona import PersonaService
from chess.square import Square, SquareContext
from chess.system import GameColor, HashService, InvariantBreachException, LoggingLevelRouter, SearchResult, id_emitter


class FormationService(HashService[Formation]):
    SERVICE_NAME = "FormationService"
    _formation: Formation
    _persona_service: PersonaService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            formation: Formation = Formation(),
            validator: FormationValidator = FormationValidator(),
            super_key_service: FormationKeyService = FormationKeyService(),
            persona_service: PersonaService = PersonaService()
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   validator (FormationValidator)
            *   super_key_service (FormationKeyService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, validator=validator, super_key_service=super_key_service)
        self._formation = formation
        self._persona_service = persona_service
        
    @property
    def persona_service(self) -> PersonaService:
        return self._persona_service
        
    @property
    def formation(self) -> Formation:
        return self._formation
    
    @property
    def number_of_tokens_per_team(self) -> int:
        return cast(int, len(self._formation.__dict__) / 2)
    
    @property
    def key_service(self) -> FormationKeyService:
        """"""
        return cast(FormationKeyService, self.hash_key_service)
    
    @property
    def validator(self) -> FormationValidator:
        """"""
        return cast(FormationValidator, self.hash_validator)
    
    @classmethod
    def formation_colors(cls) -> List[GameColor]:
        """Color of the piece assigned the formation."""
        return [entry.color for entry in Formation]
    
    @classmethod
    def formation_designations(cls) -> List[str]:
        """Chess designation of the piece assigned the formation."""
        return [entry.name for entry in Formation]
    
    @classmethod
    def formation_square_names(cls) -> List[str]:
        """Name of the item a piece makes its opening from."""
        return [entry.name for entry in Formation]

    @property
    def formation_names(self) -> List[str]:
        """Full name of the formation made up of color, rank, and number."""
        return [order.name.upper() for order in Formation]
    

    @LoggingLevelRouter.monitor
    def derive_token_manifest(
            self,
            team: Team,
            token_designation: str,
            team_service: TeamService = TeamService()
    ) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  If the team fails validation send the exception chain in the SearchResult.
            2.  Find each formation's team item by their designation ane put them in a list.
            3.  if any search fails return the exception instead of the list.
        # PARAMETERS:
            *   team (Team)
            *   team_service (TeamService)
         # RETURNS:
            *   SearchResult[List[[Square]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Square] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   TypeError
            *   NullTeamContextException
            *   ZeroTeamContextFlagsException
            *   ExcessiveTeamContextFlagsException
            *   TeamContextValidationFailedException
            *   TeamContextValidationRouteException
        """
        method = "FormationService.get_team_square"
        
        # Handle the case that the team does not get certfied safe.
        team_validation = team_service.validator.validate(candidate=team)
        # Return the exception chain on failure.
        if team_validation.is_failure:
            return SearchResult.failure(
                FormationServiceException(
                    message=f"{method}: {FormationServiceException.ERROR_CODE}",
                    ex=team_validation.exception
                )
            )
        formation_search_result = self.lookup_formation(super_key=FormationKey(designation=token_designation))
        # Handle the case that the search fails.
        if formation_search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                FormationServiceException(
                    message=f"{method}: {FormationServiceException.ERROR_CODE}",
                    ex=formation_search_result.exception
                )
            )
        formation = formation_search_result.payload[0]
        square_search_result = team.squares.search(context=SquareContext(name=formation.square_name))
        # Handle the case that the square search fails.
        if square_search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                FormationServiceException(
                    message=f"{method}: {FormationServiceException.ERROR_CODE}",
                    ex=square_search_result.exception
                )
            )
        # Handle the case that no square was found.
        if square_search_result.is_empty:
            # Return the exception chain on failure.
            return SearchResult.failure(
                FormationServiceException(
                    message=f"{method}: {FormationServiceException.ERROR_CODE}",
                    ex=InvariantBreachException(f"{method}: Square {formation.square_name} not found.")
                )
            )
        hash = {
            "square": square_search_result.payload[0],
            "formation": formation,
        }
        # if square_search_result.is_failure:
        # squares = List[Square]
        # # Loop through the formations to find their squares from the team.
        # for formation in Formation:
        #     square_search = team.squares.search(context=SquareContext(name=formation.square_name))
        #
        #     # Handle the case that no item with the denomination is found.
        #     if square_search.is_empty:
        #         # Return the exception chain on failure.
        #         return SearchResult.failure(
        #             FormationServiceException(
        #                 message=f"{method}: {FormationServiceException.ERROR_CODE}",
        #                 ex=InvariantBreachException(f"{method}: Square {formation.square_name} not found.")
        #             )
        #         )
        #     # Make sure to cast then return to the caller.
        #     squares.append(cast(Square, square_search.payload[0]))
        # return SearchResult.success(squares)
            
    @LoggingLevelRouter.monitor
    def lookup_formation(self, super_key: FormationKey) -> SearchResult[List[Formation]]:
        """
        # ACTION:
            Using lookup_formation is simpler and more extendable than building searches manually from self.key_service.
            1.  If the self.key_service.lookup does not produce a payload send a FormationServiceException chain in the
                SearchResult. Otherwise, return the payload.
        # PARAMETERS:
            *   super_key (FormationKey)
        # RETURNS:
            *   SearchResult[List[Formation]] containing a list if a match is found else an exception chain.
        # RAISES:
            None
        """
        method = "FormationService.lookup_formation"
        result = self.key_service.lookup.query(super_key=super_key, super_key_validator=self.key_service.validator)
        
        # Handle the case search failed by raising an exception.
        if result.is_failure:
            return SearchResult.failure(
                FormationServiceException(
                    message=f"ServiceId:{self.id}, {method}: {FormationServiceException.ERROR_CODE}",
                    ex=result.exception,
                )
            )
        # On search success send the result to the caller.
        return result

