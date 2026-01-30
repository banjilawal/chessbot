# src/chess/token/context/service/service.py

"""
Module: chess.token.context.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import cast

from chess.system import ContextService, id_emitter
from chess.token import TokenContext, TokenContextBuilder, TokenContextValidator, TokenFinder


class TokenContextService(ContextService[TokenContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facingToken search microservice API.
    2.  Provides a map aware utility for searchingToken objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth forToken search results by having single entry and exit points for the
       Token search flow.

    # PARENT:
        *   ContextService

    # PROVIDES:
        *  TokenContextService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "TokenContextService"
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: TokenFinder = TokenFinder(),
            builder: TokenContextBuilder =TokenContextBuilder(),
            validator: TokenContextValidator =TokenContextValidator(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   finder (TokenFinder)
            *   builder (TokenContextBuilder)
            *   validator (TokenContextValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "TokenContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) ->TokenFinder:
        """GetTokenFinder instance."""
        return cast(TokenFinder, self.entity_finder)
    
    @property
    def builder(self) ->TokenContextBuilder:
        """GetTokenContextBuilder instance."""
        return cast(TokenContextBuilder, self.entity_builder)
    
    @property
    def validator(self) ->TokenContextValidator:
        """GetTokenContextValidator instance."""
        return cast(TokenContextValidator, self.entity_validator)
    
    