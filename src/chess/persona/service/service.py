# src/chess/persona/service/service.py

"""
Module: chess.persona.service.service
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Dict, List, Optional, cast


from chess.rank import Bishop, King, Knight, Pawn, Queen, Rank, Rook
from chess.system import HashService, LoggingLevelRouter, SearchResult, id_emitter
from chess.persona import Persona, PersonaServiceException, PersonaSuperKey, PersonaSuperKeyService, PersonaValidator

class PersonaService(HashService[Persona]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Persona search microservice API.
    2.  Provides a map aware utility for searching Persona objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Persona search results by having single entry and exit points for the
        Persona search flow.

    # PARENT:
        *   ContextService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "PersonaService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            validator: PersonaValidator = PersonaValidator(),
            super_key_service: PersonaSuperKeyService = PersonaSuperKeyService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   validator (PersonaValidator)
            *   super_key_service (PersonaSuperKeyService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, validator=validator, super_key_service=super_key_service)
        
    @property
    def key_service(self) -> PersonaSuperKeyService:
        return cast(PersonaSuperKeyService, self.hash_super_key_service)
    
    @property
    def persona_validator(self) -> PersonaValidator:
        """"""
        return cast(PersonaValidator, self.hash_validator)
    
    @property
    def names(self) -> List[str]:
        """Returns a list of all permissible persona names in upper case."""
        return [persona.name.upper() for persona in Persona]
    
    @property
    def designations(self) -> List[str]:
        """Returns a list of all permissible persona designations in upper case."""
        return [entry.designation.upper() for entry in Persona]
    
    @property
    def quotas(self) -> List[int]:
        """Returns a list of all the unique team_quotas in the persona."""
        return [entry.quota for entry in Persona]
    
    @property
    def ransoms(self) -> List[int]:
        """Returns a list of all the unique ransoms in the persona."""
        return [entry.ransom for entry in Persona]
    
    @property
    def min_ransom(self) -> int:
        minimum = 100
        for ransom in self.ransoms:
            if ransom < minimum:
                minimum = ransom
        return minimum
    
    @property
    def max_ransom(self) -> int:
        maximum = -100
        for ransom in self.ransoms:
            if ransom > maximum:
                maximum = ransom
        return maximum

    
    @classmethod
    def rank_from_persona(cls, entry: Persona) -> Optional[Rank]:
        """Get the Rank which the persona entry builds."""
        if entry == Persona.KING: return King()
        if entry == Persona.PAWN: return Pawn()
        if entry == Persona.KNIGHT: return Knight()
        if entry == Persona.BISHOP: return Bishop()
        if entry == Persona.ROOK: return Rook()
        if entry == Persona.QUEEN: return Queen()
        return None
    
    @classmethod
    def persona_from_rank(cls, rank: Rank) -> Optional[Persona]:
        """Get the Persona from its corresponding Rank."""
        if isinstance(rank, King): return Persona.KING
        if isinstance(rank, Pawn): return Persona.PAWN
        if isinstance(rank, Knight): return Persona.KNIGHT
        if isinstance(rank, Bishop): return Persona.BISHOP
        if isinstance(rank, Rook): return Persona.ROOK
        if isinstance(rank, Queen): return Persona.QUEEN
        return None
        
    @LoggingLevelRouter.monitor
    def lookup_persona(self, super_key: PersonaSuperKey) -> SearchResult[List[Persona]]:
        """
        # ACTION:
            Using lookup_persona is simpler and more extendable than building searches manually from self.key_service.
            1.  If the self.key_service.lookup does not produce a payload send a PersonaServiceException chain in the
                SearchResult. Otherwise, return the payload.
        # PARAMETERS:
            *   super_key (PersonaSuperKey)
        # RETURNS:
            *   SearchResult[List[Persona]] containing a list if a match is found else an exception chain.
        # RAISES:
            None
        """
        method = "PersonaService.lookup_persona"
        result = self.key_service.lookup.query(super_key=super_key, super_key_validator=self.key_service.validator)
        
        # Handle the case search failed by raising an exception.
        if result.is_failure:
            return SearchResult.failure(
                PersonaServiceException(
                    message=f"ServiceId:{self.id}, {method}: {PersonaServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On search success send the result to the caller.
        return result
