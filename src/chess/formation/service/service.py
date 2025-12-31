from typing import List, cast

from chess.formation import Formation, FormationSuperKey, FormationSuperKeyService, FormationValidator, FormationServiceException
from chess.system import GameColor, HashService, LoggingLevelRouter, SearchResult, id_emitter


class FormationService(HashService[Formation]):
    SERVICE_NAME = "FormationService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            validator: FormationValidator = FormationValidator(),
            super_key_service: FormationSuperKeyService = FormationSuperKeyService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   validator (FormationValidator)
            *   super_key_service (FormationSuperKeyService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, validator=validator, super_key_service=super_key_service)
    
    @property
    def key_service(self) -> FormationSuperKeyService:
        """"""
        return cast(FormationSuperKeyService, self.hash_super_key_service)
    
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
        """Name of the square a piece makes its opening from."""
        return [entry.name for entry in Formation]

    @property
    def formation_names(self) -> List[str]:
        """Full name of the formation made up of color, rank, and number."""
        return [order.name.upper() for order in Formation]
    
    @LoggingLevelRouter.monitor
    def lookup_formation(self, super_key: FormationSuperKey) -> SearchResult[List[Formation]]:
        """
        # ACTION:
            Using lookup_formation is simpler and more extendable than building searches manually from self.key_service.
            1.  If the self.key_service.lookup does not produce a payload send a FormationServiceException chain in the
                SearchResult. Otherwise, return the payload.
        # PARAMETERS:
            *   super_key (FormationSuperKey)
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

