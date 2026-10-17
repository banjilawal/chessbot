# src/transit/route/fabrication/model/token/router.py

"""
Module: transit.route.fabrication.model.token.router
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import CombatantTokenBlueprint, KingTokenBlueprint, PawnTokenBlueprint, Token, TokenBlueprint
from err import TokenBlueprintNullException, MissingTokenBuildRouteException, TokenBuildRouterException
from fabrication import (
    CombatantTokenSubcontractor, KingTokenSubcontractor, 
    ModelBuildRouter, PawnTokenSubcontractor
)
from util import LoggingLevelRouter


class TokenBuildRouter(ModelBuildRouter[Token]):
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
        ModelBuildRouter
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
        """
        super().__init__()
        self._king_subcontractor = king_subcontractor or KingTokenSubcontractor()
        self._pawn_subcontractor = pawn_subcontractor or PawnTokenSubcontractor()
        self._combatant_subcontractor = combatant_subcontractor or CombatantTokenSubcontractor()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TokenBlueprint) -> BuildResult[Token]:
        """
        Routes a TokenBlueprint subclass to its corresponding SubBuilder.

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
        # Otherwise get the payload.
        fingerprint = cast(TokenBlueprint, validation.payload)
        
        # --- Route to the appropriate token_build subcontractor. ---#
        if isinstance(fingerprint, PawnTokenBlueprint):
            return self._pawn_subcontractor.execute(fingerprint)
        if isinstance(fingerprint, KingTokenBlueprint):
            return self._king_subcontractor.execute( fingerprint)
        if isinstance(fingerprint, CombatantTokenBlueprint):
            return self._combatant_subcontractor.execute(fingerprint)
        
        # Handle the case that no route exists for the fingerprint.
        return BuildResult.failure(
            TokenBuildRouterException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=TokenBuildRouterException.MSG,
                err_code=TokenBuildRouterException.ERR_CODE,
                ex=MissingTokenBuildRouteException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=MissingTokenBuildRouteException.MSG,
                    err_code=MissingTokenBuildRouteException.ERR_CODE,
                )
            )
        )
        
        
        