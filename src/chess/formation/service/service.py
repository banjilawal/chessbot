# src/chess/team/team_schema/service/service.py

"""
Module: chess.team.team_schema.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from enum import member
from typing import List, cast

from chess.formation import BattleOrderContext, BattleOrderContextValidator
from chess.system import (
    Builder, EntityService, GameColor, GameColorValidator, IdentityService, LoggingLevelRouter, NotImplementedException,
    Result,
    SearchResult, id_emitter
)
from chess.team import BattleOrderContextService, BattleOrderValidator
from chess.team.schema import BattleOrder


class BattleOrderService(EntityService[BattleOrder]):
    """
    # ROLE: Service, Utility

    # RESPONSIBILITIES:
    1.  Public facing Team State Machine microservice API.
    2.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    3.  Is authoritative, single source of truth for Team state by providing single entry and exit points to Team
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   allowed_colors() -> List[GameColor]:
        *   allowed_names() -> List[str]:
        *   enemy_schema(team_schema: BattleOrder) -> Result[BattleOrder]:

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    DEFAULT_NAME = "BattleOrderService"
    _context_service: BattleOrderContextService
    
    def __init__(
            self,
            builder: Builder[BattleOrder] = None,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            validator: BattleOrderValidator = BattleOrderValidator(),
            context_service: BattleOrderContextService = BattleOrderContextService(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._context_service = context_service
        
    @property
    def context_service(self) -> BattleOrderContextService:
        return self._context_service
    
    @property
    def validator(self) -> BattleOrderValidator:
        return cast(BattleOrderValidator, self._validator)
    
    @property
    def builder(self) -> None:
        """BattleOrderService does not support building entities."""
        method = "BattleOrderService.builder"
        raise NotImplementedException(f"{method}: BattleOrderService does not support building entities.")
    
    @property
    def allowed_names(self) -> List[str]:
        return [member.name for member in BattleOrder]
    
    @property
    def black_battle_orders(self) -> List[BattleOrder]:
        return [member for member in BattleOrder if member.color == GameColor.BLACK]
    
    @property
    def white_battle_orders(self) -> List[BattleOrder]:
        return [member for member in BattleOrder if member.color == GameColor.WHITE]
    
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            context: BattleOrderContext,
            context_validator: BattleOrderContextValidator = BattleOrderContextValidator(),
    ) -> SearchResult[List[BattleOrder]]:
        """
        # Action:
        1.  Use context_validator to certify the provided context.
        2.  Context attribute routes the search. Attribute value is the search target.
        3.  The outcome of the search is sent back to the caller in a SearchResult object.

        # Parameters:
            *   context (BattleOrderContext)
            *   context_validator (BattleOrderContextValidator)

        # Returns:
        SearchResult[List[BattleOrder]] containing either:
            - On success: List[battleOrder] in the payload.
            - On failure: Exception.

        # Raises:
            *   BattleOrderFinderException
        """
        method = "BattleOrderFinder.find"
        try:
            # certify the context is safe.
            context_validation = context_validator.validate(candidate=context)
            if context_validation.is_failure:
                return SearchResult.failure(context_validation.exception)
            # After context is verified select the search method based on the which flag is enabled.
            
            # Entry point into searching by name value.
            if context.name is not None:
                return cls._find_by_name(name=context.name)
            # Entry point into searching by square value.
            if context.square is not None:
                return cls._find_by_square(name=context.square)
            # Entry point into searching by color value.
            if context.color is not None:
                return cls._find_by_color(color=context.color)

        # Finally, if some exception is not handled by the checks wrap it inside an BattleOrderFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                BattleOrderFinderException(ex=ex, message=f"{method}: {BattleOrderFinderException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(
            cls,
            name: str,
            identity_service: IdentityService = IdentityService()
    ) -> SearchResult[List[BattleOrder]]:
        method = "BattleOrderService._find_by_piece_name"
        try:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                return SearchResult.failure(validation.exception)
            
            matches = [member for member in BattleOrder if member.name.upper() == name.upper()]
            if len(matches) == 0:
                return SearchResult.empty()
            if len(matches) >= 1:
                return SearchResult.success(matches)
            return SearchResult.failure(
                OrderNameBoundsException(f"{method}: {OrderNameBoundsException.DEFAULT_MESSAGE}")
            )
        except Exception as ex:
            return SearchResult.failure(
                BattleOrderServiceException(ex=ex, message=f"{method}: {BattleOrderServiceException.DEFAULT_MESSAGE}")
            )

    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_square(
            cls,
            name: str,
            identity_service: IdentityService = IdentityService()
    ) -> SearchResult[List[BattleOrder]]:
        method = "BattleOrderService._find_by_square_name"
        try:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                return SearchResult.failure(validation.exception)
            
            matches = [member for member in BattleOrder if member.square.upper() == name.upper()]
            if len(matches) == 0:
                return SearchResult.empty()
            if len(matches) >= 1:
                return SearchResult.success(matches)
            return SearchResult.failure(
                OrderSquareBoundsException(f"{method}: {OrderSquareBoundsException.DEFAULT_MESSAGE}")
            )
        except Exception as ex:
            return SearchResult.failure(
                BattleOrderServiceException(ex=ex, message=f"{method}: {BattleOrderServiceException.DEFAULT_MESSAGE}")
            )

    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_color(
            cls,
            color: GameColor
    ) -> List[BattleOrder]:
        method = "BattleOrderService._find_by_color"
        try:
            matches = [member for member in BattleOrder if member.color == color]
            if len(matches) == 0:
                return SearchResult.empty()
            if len(matches) >= 1:
                return SearchResult.success(matches)
            return SearchResult.failure(
                OrderColorBoundsException(f"{method}: {OrderColorBoundsException.DEFAULT_MESSAGE}")
            )
        except Exception as ex:
            return SearchResult.failure(
                BattleOrderServiceException(ex=ex, message=f"{method}: {BattleOrderServiceException.DEFAULT_MESSAGE}")
            )