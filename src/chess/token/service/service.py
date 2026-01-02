# src/chess/token/service/service.py

"""
Module: chess.token.service.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""
from typing import cast

from chess.coord import Coord, CoordService
from chess.formation import FormationService
from chess.system import EntityService, InsertionResult, id_emitter
from chess.token import Token, TokenFactory, TokenValidator
from chess.token.service.exception.catchall import TokenServiceException


class TokenService(EntityService[Token]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Token microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Token state by providing single entry and exit points to Token
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    SERVICE_NAME = "TokenService"
    _formation_service: FormationService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: TokenFactory = TokenFactory(),
            validator: TokenValidator = TokenValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (TokenFactory)
            *   validator (TokenValidator)

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> TokenFactory:
        """get TokenFactory"""
        return cast(TokenFactory, self.entity_builder)
    
    @property
    def validator(self) -> TokenValidator:
        """get TokenValidator"""
        return cast(TokenValidator, self.entity_validator)
    
    @property
    def formation_service(self) -> FormationService:
        return self._formation_service
    
    def push_position(
            self,
            token: Token,
            position: Coord,
            coord_service: CoordService = CoordService()
    ) -> InsertionResult[Coord]:
        method = "TokenService.push_position"
        # Handle the case that the token is not certified safe.
        token_validation = self.validator.validate(token)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenService.ERROR_CODE}",
                    ex=token_validation.exception
                )
            )
        
        # Handle the case that the team is not certified safe.
        position_validation = coord_service.validate(position)
        if position_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenService.ERROR_CODE}",
                    ex=token_validation.exception
                )
            )
        
        # Handle the case that the token already occupies the position.
        if position in token.current_position:
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenService.ERROR_CODE}"
                    ex=DuplicateCoordPushException(f"{method}: {DuplicateCoordPushException.DEFAULT_MESSAGE}")
                )
            )
        push_result = token.positions.push_coord(coord=position)
        
        
        return InsertionResult.success(position)
