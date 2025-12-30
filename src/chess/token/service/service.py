# src/chess/token/service/service.py

"""
Module: chess.token.service.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""
from typing import cast

from chess.system import EntityService, id_emitter
from chess.token import Token, TokenFactory, TokenValidator


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
        *   builder:    -> TokenFactory
        *   validator:  -> TokenValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    DEFAULT_NAME = "TokenService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
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

        # Returns:
        None

        # Raises:
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
    
