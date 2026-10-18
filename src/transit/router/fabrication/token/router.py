# src/transit/route/fabrication/token/router.py

"""
Module: transit.route.fabrication.token.router
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import (
    CombatantTokenBlueprint, KingTokenBlueprint, PawnTokenBlueprint, Token,
    TokenBlueprint
)
from err import (
    TokenBlueprintNullException, MissingTokenBuildRouteException, TokenBuildRouterException
)
from fabrication import (
    CombatantTokenSubcontractor, KingTokenSubcontractor, 
    BuildRouter, PawnTokenSubcontractor
)
from util import LoggingLevelRouter


class TokenBuildRouter(BuildRouter[Token]):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Routes TokenBlueprint subclasses to the appropriate assembler.

    Attributes:
        king_subcontractor: KingTokenSubcontractor
        pawn_subcontractor: PawnTokenSubcontractor
        combatant_subcontractor: CombatantTokenSubcontractor
        
    Provides:
            -   def execute(blueprint: TokenBlueprint) -> BuildResult[Token]

    Super Class:
        BuildRouter
    """
    
    _king_subcontractor: KingTokenSubcontractor
    _pawn_subcontractor: PawnTokenSubcontractor
    _combatant_subcontractor: CombatantTokenSubcontractor

    
    def __init__(
            self,
            king_subcontractor: Optional[KingTokenSubcontractor] | None = None,
            pawn_subcontractor: Optional[PawnTokenSubcontractor] | None = None,
            combatant_subcontractor: Optional[CombatantTokenSubcontractor] | None = None,
    ):
        """
        Args:
            king_subcontractor: Optional[KingTokenSubcontractor]
            pawn_subcontractor: Optional[PawnTokenSubcontractor]
            combatant_subcontractor: Optional[CombatantTokenSubcontractor]
        """
        super().__init__()
        self._king_subcontractor = king_subcontractor or KingTokenSubcontractor()
        self._pawn_subcontractor = pawn_subcontractor or PawnTokenSubcontractor()
        self._combatant_subcontractor = combatant_subcontractor or CombatantTokenSubcontractor()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TokenBlueprint) -> BuildResult[Token]:
        """
        Routes a TokenBlueprint to a Subcontractor for construction.

        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                -   The blueprint is null or the wrong type.
                -   No subcontractor exists for the blueprint.
                -   The subcontractor fails.
            2.  Otherwise, cast the subcontract's product to an Token then send in the
                success result.
        Args:
             blueprint: Blueprint[Token]
        Returns:
            BuildResult[Token]
        Raises:
            TokenBuildRouterException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the case that the router cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=TokenBlueprint,
            null_exception=TokenBlueprintNullException(),
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuildRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuildRouterException.MSG,
                    err_code=TokenBuildRouterException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # Otherwise cast the payload for additional processing.
        fingerprint = cast(TokenBlueprint, validation.payload)
        
        # Initialize the default failure result
        result = BuildResult.failure(
            MissingTokenBuildRouteException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=MissingTokenBuildRouteException.MSG,
                err_code=MissingTokenBuildRouteException.ERR_CODE,
            )
        )
        # --- Route to the appropriate token_build subcontractor. ---#
        if isinstance(fingerprint, PawnTokenBlueprint):
            result = self._pawn_subcontractor.execute(fingerprint)
        if isinstance(fingerprint, KingTokenBlueprint):
            result = self._king_subcontractor.execute( fingerprint)
        if isinstance(fingerprint, CombatantTokenBlueprint):
            result = self._combatant_subcontractor.execute(fingerprint)
        
        # Handle the case that the subcontractor does make a product.
        if result.is_failure:
            # Handle the case that no route exists for the fingerprint.
            return BuildResult.failure(
                TokenBuildRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuildRouterException.MSG,
                    err_code=TokenBuildRouterException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        model = cast(Token, result.payload)
        return BuildResult.success(model)

        
        
        