# src/transit/route/fabrication/rank.py

"""
Module: transit.route.fabrication.rank
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Bishop, King, Knight, Pawn, Queen, Rank, RankBlueprint, Rook
from err import RankBlueprintNullException, RankBuildRouteMissingException, RankBuildRouterException
from transit import BuildRouter
from util import LoggingLevelRouter


class RankBuildRouter(BuildRouter[Rank]):
    """
    Role
        - Router

    Responsibilities:
        1.  Route a RankBlueprint to its appropriate Contractor
            by Carrier type.

    Attributes:
        bishop: BishopSubcontractor
        king: KingSubcontractor
        knight: KnightSubcontractor
        pawn: PawnSubcontractor
        queen: QueenSubcontractor
        rook: RookSubcontractor

    Provides:
        -   def execute(blueprint: RankBlueprint) -> BuildResult[Rank]

    Super Class:
        BuildRouter
    """
    
    _bishop: BishopSubcontractor
    _king: KingSubcontractor
    _knight: KnightSubcontractor
    _pawn: PawnSubcontractor
    _queen: QueenSubcontractor
    _rook: RookSubcontractor
    
    def __init__(
            self,
            bishop: Optional[BishopSubcontractor] | None = None,
            king: Optional[KingSubcontractor] | None = None,
            knight: Optional[KnightSubcontractor] | None = None,
            pawn: Optional[PawnSubcontractor] | None = None,
            queen: Optional[QueenSubcontractor] | None = None,
            rook: Optional[RookSubcontractor] | None = None,
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
        self._bishop_subcontractor = king_subcontractor or BishopSubcontractor()
        self._king_subcontractor = king_subcontractor or KingSubcontractor()
        self._knight_subcontractor = knight_subcontractor or KnightSubcontractor()
        self._pawn_subcontractor = pawn_subcontractor or PawnSubcontractor()
        self._queen_subcontractor = king_subcontractor or QueenSubcontractor()
        self._rook_subcontractor = pawn_subcontractor or RookSubcontractor()
    
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
        if isinstance(fingerprint, Bishop):
            result = self._bishop_subcontractor.execute(fingerprint)
        # Route to the king_subcontractor
        if isinstance(fingerprint, King):
            result = self._king_subcontractor.execute(fingerprint)
        # Route to the knight_subcontractor
        if isinstance(fingerprint, Knight):
            result = self._king_subcontractor.execute(fingerprint)
        # Route to pawn_subcontractor.
        if isinstance(fingerprint, Pawn):
            result = self._pawn_subcontractor.execute(fingerprint)
        # Route to the king_subcontractor
        if isinstance(fingerprint, Queen):
            result = self._queen_subcontractor.execute(fingerprint)
        # Route to pawn_subcontractor.
        if isinstance(fingerprint, Rook):
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
        




    