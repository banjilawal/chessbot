# src/chess/persona/service/service.py

"""
Module: chess.persona.service.service
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""
import sys
from typing import Dict, List, Optional, cast


from chess.rank import Bishop, King, Knight, Pawn, Queen, Rank, RankService, Rook
from chess.rank.factory.exception.wrapper import RankBuildFailedException
from chess.system import (
    BuildResult, ComputationResult, HashService, LoggingLevelRouter, Result, SearchResult,
    id_emitter
)
from chess.persona import (
    Persona, PersonaLookupFailedException, PersonaServiceException, PersonaKey, PersonaKeyService, PersonaValidator,
    RankQuotaPerTeamLookupFailedException
)


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
    _persona: Persona
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            persona: Persona = Persona(),
            id: int = id_emitter.service_id,
            validator: PersonaValidator = PersonaValidator(),
            super_key_service: PersonaKeyService = PersonaKeyService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   validator (PersonaValidator)
            *   super_key_service (PersonaKeyService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, validator=validator, super_key_service=super_key_service)
        self._persona = persona
        
    @property
    def persona(self) -> Persona:
        return self._persona
        
    @property
    def key_service(self) -> PersonaKeyService:
        return cast(PersonaKeyService, self.hash_key_service)
    
    @property
    def validator(self) -> PersonaValidator:
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
        minimum = sys.maxsize
        for ransom in self.ransoms:
            if ransom < minimum:
                minimum = ransom
        return minimum
    
    @property
    def max_ransom(self) -> int:
        maximum = -1 * sys.maxsize
        for ransom in self.ransoms:
            if ransom > maximum:
                maximum = ransom
        return maximum
    
    @LoggingLevelRouter.monitor
    def quota_per_rank(self, rank: Rank, rank_service: RankService = RankService()) -> ComputationResult[int]:
        """
        # ACTION:
            1   f the rank is not certified safe send an exception chain in the ComputationResult.
                Otherwise, send the quota which matches the rank in the ComputationResult's payload.
        # PARAMETERS:
            *   rank (Rank)
            *   rank_service (RankService)
        # RETURNS:
            *   ComputationResult[int] containing either:
                    - On error: Exception
                    - On success: int in the payload.
        # RAISES:
            *   PersonaServiceException
            *   RankQuotaPerTeamLookupFailedException
        """
        method = "PersonaService.quota_per_rank"
        
        # Handle the case that rank is not certified safe.
        validation = rank_service.validator.validate(candidate=rank)
        if validation.is_failure:
            return ComputationResult.failure(
                # Return exception chain on failure.
                PersonaServiceException(
                    message=f"ServiceId:{self.id} {method}: {PersonaServiceException.ERROR_CODE}",
                    ex=RankQuotaPerTeamLookupFailedException(
                        message=f"{method}: {RankQuotaPerTeamLookupFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Because of the validation all the ranks will be valid. Can forward the quota to the caller. ---#
        if rank == King: return ComputationResult.success(payload=Persona.KING.quota)
        if rank == Pawn: return ComputationResult.success(payload=Persona.PAWN.quota)
        if rank == Knight: return ComputationResult.success(payload=Persona.KNIGHT.quota)
        if rank == Bishop: return ComputationResult.success(payload=Persona.BISHOP.quota)
        if rank == Rook: return ComputationResult.success(payload=Persona.ROOK.quota)
        
        # --- Only possible case left is Queen ---#
        return ComputationResult.success(payload=Persona.QUEEN.quota)
    #
    #
    # @LoggingLevelRouter.monitor
    # def build_rank_from_persona(self, persona: Persona, rank_service: RankService = RankService()) -> BuildResult[Rank]:
    #     """
    #     # ACTION:
    #         1   f the persona is not certified safe send an exception chain in the BuildResult.
    #             Otherwise, send a rank instance in the BuildResult's payload.'
    #     # PARAMETERS:
    #         *   persona (Persona)
    #     # RETURNS:
    #         *   BuildResult[Rank] containing either:
    #                 - On error: Exception
    #                 - On success: Rankin the payload.
    #     # RAISES:
    #         *   PersonaServiceException
    #         *   BuildRankFailedException
    #     """
    #     method = "PersonaService.rank_from_persona"
    #
    #     # Handle the case that persona is not certified safe.
    #     validation = self.validator.validate(candidate=persona)
    #     if validation.is_failure:
    #         return BuildResult.failure(
    #             # Return exception chain on failure.
    #             PersonaServiceException(
    #                 message=f"ServiceId:{self.id} {method}: {PersonaServiceException.ERROR_CODE}",
    #                 ex=RankBuildFailedException(
    #                     message=f"{method}: {RankBuildFailedException.ERROR_CODE}",
    #                     ex=validation.exception
    #                 )
    #             )
    #         )
    #     # --- Use the RankService instance to build the rank. It comes with its ow n  ---#
    
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
    def lookup_persona(self, super_key: PersonaKey) -> SearchResult[List[Persona]]:
        """
        # ACTION:
            Using lookup_persona is simpler and more extendable than building searches manually from self.key_service.
            1.  If the self.key_service.lookup does not produce a payload send a PersonaServiceException chain in the
                SearchResult. Otherwise, return the payload.
        # PARAMETERS:
            *   super_key (PersonaKey)
        # RETURNS:
            *   SearchResult[List[Persona]] containing a list if a match is found else an exception chain.
        # RETURNS:
            *   SearchResult[List[Formation]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Formation] in the payload.
                    - On no matches found: Exception null, payload null
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
