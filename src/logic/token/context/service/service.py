# src/logic/token/context/service/service.py

"""
Module: logic.token.context.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import cast

from logic.system import ContextService, id_emitter
from logic.token import TokenContext, TokenContextBuildProcess, TokenContextValidationProcess, TokenFinder


class TokenQueryService(ContextService[TokenContext]):
    """
    Role:Search Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facingToken search microservice API.
    2.  Provides a map aware utility for searchingToken objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth forToken search results by having single entry and exit points for the
       Token search flow.

    Super Class:
        *   ContextService

    # PROVIDES:
        *  TokenQueryService


    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "TokenQueryService"
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: TokenFinder = TokenFinder(),
            builder: TokenContextBuildProcess =TokenContextBuildProcess(),
            validator: TokenContextValidationProcess =TokenContextValidationProcess(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   finder (TokenFinder)
            *   builder (TokenContextBuildProcess)
            *   validator (TokenContextValidationProcess)
        # RETURNS:
            None
        Raises:
            None
        """
        method = "TokenQueryService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) ->TokenFinder:
        """GetTokenFinder instance."""
        return cast(TokenFinder, self.entity_finder)
    
    @property
    def build(self) ->TokenContextBuildProcess:
        """GetTokenContextBuilder instance."""
        return cast(TokenContextBuildProcess, self.entity_builder)
    
    @property
    def validation(self) ->TokenContextValidationProcess:
        """GetTokenContextValidator instance."""
        return cast(TokenContextValidationProcess, self.entity_validator)
    
    