# src/transit/route/fabrication/model/rank.py

"""
Module: transit.route.fabrication.model.rank
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import (
    BishopBlueprint, KingBlueprint, KnightBlueprint, PawnBlueprint, QueenBlueprint,
    Rank, RankBlueprint, RookBlueprint
)
from err import RankBlueprintNullException, RankBuildRouteMissingException, RankBuildRouterException
from fabrication import (
    BishopSubcontractor, KingSubcontractor, KnightSubcontractor, PawnSubcontractor,
    QueenSubcontractor, RookSubcontractor
)
from transit import ModelBuildRouter
from util import LoggingLevelRouter


class RankBuildRouter(ModelBuildRouter[Rank]):
    """
    Role
        - Router

    Responsibilities:
        1.  Route a RankBlueprint to its appropriate Contractor
            by Carrier type.

    Attributes:
        bishop_subcontractor: BishopSubcontractor
        king_subcontractor: KingSubcontractor
        knight_subcontractor: KnightSubcontractor
        pawn_subcontractor: PawnSubcontractor
        queen_subcontractor: QueenSubcontractor
        rook_subcontractor: RookSubcontractor

    Provides:
        -   def execute(blueprint: RankBlueprint) -> BuildResult[Rank]

    Super Class:
        BuildRouter
    """
    
    _bishop_subcontractor: BishopSubcontractor
    _king_subcontractor: KingSubcontractor
    _knight_subcontractor: KnightSubcontractor
    _pawn_subcontractor: PawnSubcontractor
    _queen_subcontractor: QueenSubcontractor
    _rook_subcontractor: RookSubcontractor
    
    def __init__(
            self,
            bishop_subcontractor: Optional[BishopSubcontractor] | None = None,
            king_subcontractor: Optional[KingSubcontractor] | None = None,
            knight_subcontractor: Optional[KnightSubcontractor] | None = None,
            pawn_subcontractor: Optional[PawnSubcontractor] | None = None,
            queen_subcontractor: Optional[QueenSubcontractor] | None = None,
            rook_subcontractor: Optional[RookSubcontractor] | None = None,
    ):
        """
        Args:
            bishop: Optional[BishopSubcontractor]
            king: Optional[KingSubcontractor]
            knight: Optional[KnightSubcontractor]
            pawn: Optional[PawnSubcontractor]
            quee: Optional[QueenSubcontractor]
            rook: Optional[RookSubcontractor]
        """
        super().__init__()
        self._bishop_subcontractor = bishop_subcontractor or BishopSubcontractor()
        self._king_subcontractor = king_subcontractor or KingSubcontractor()
        self._knight_subcontractor = knight_subcontractor or KnightSubcontractor()
        self._pawn_subcontractor = pawn_subcontractor or PawnSubcontractor()
        self._queen_subcontractor = queen_subcontractor or QueenSubcontractor()
        self._rook_subcontractor = rook_subcontractor or RookSubcontractor()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: RankBlueprint) -> BuildResult[Rank]:
        """
        Assure a candidate is a fingerprint Rank.

        Action:
            1.  Send an exception chain in the BuildResult if any of
                the following occur:
                    -   The router cannot be primed.
                    -   The endpoint cannot consume the blueprint.
                    -   No consumption route exists
            2.  Otherwise, cast the payload and send in the success result.
        Args:
            blueprint: RankBlueprint
        Returns:
            BuildResult[Rank]
        Raises:
           RankBuildRouterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the router cannot be primed.
        priming = self.priming_validator.execute(
            candidate=blueprint,
            target_model=RankBlueprint,
            null_exception=RankBlueprintNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                RankBuildRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankBuildRouterException.MSG,
                    err_code=RankBuildRouterException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # Otherwise get the payload.
        fingerprint = cast(RankBlueprint, priming.payload)
        
        # --- Route to the appropriate contractor. ---#
        result = BuildResult.failure(
            RankBuildRouteMissingException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
            )
        )
        
        # Route to bishop_build contractors.
        if isinstance(fingerprint, BishopBlueprint):
            result = self._bishop_subcontractor.execute(fingerprint)
        # Route to the king_subcontractor
        if isinstance(fingerprint, KingBlueprint):
            result = self._king_subcontractor.execute(fingerprint)
        # Route to the knight_subcontractor
        if isinstance(fingerprint, KnightBlueprint):
            result = self._knight_subcontractor.execute(fingerprint)
        # Route to pawn_subcontractor.
        if isinstance(fingerprint, PawnBlueprint):
            result = self._pawn_subcontractor.execute(fingerprint)
        # Route to the queen_subcontractor
        if isinstance(fingerprint, QueenBlueprint):
            result = self._queen_subcontractor.execute(fingerprint)
        # Route to pawn_subcontractor.
        if isinstance(fingerprint, RookBlueprint):
            result = self._rook_subcontractor.execute(fingerprint)

            
        # Handle the case that the blueprint is not consumed.
        if result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                RankBuildRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankBuildRouterException.MSG,
                    err_code=RankBuildRouterException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Send the work product to client. ---#
        model = cast(Rank, result.payload)
        return BuildResult.success(model)
        




    