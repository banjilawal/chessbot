# src/logic/span/spanner/bishop/bishop.py

"""
Module: logic.span.spanner.bishop.bishop
Author: Banji Lawal
Created: 2026-03-10
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict

from logic.system import ComputationResult
from logic.coord import Coord, CoordService
from logic.span import BishopSpannerException, DiagonalRayProvider, Span, Spanner, SpannerEngine

class BishopSpanner(Spanner):
    """
    # ROLE: Worker, Computation
    # Provide a spanning set for a Bishop

    # RESPONSIBILITIES:
    1. Provide a spanning set for a Bishop

    # PARENT:
        Spanner

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
        *   See Spanner class for inherited attributes
    """
    
    @classmethod
    def compute(
            cls,
            origin: Coord,
            engine: SpannerEngine = SpannerEngine(),
            coord_service: CoordService = CoordService(),
            diagonal_ray_provider: DiagonalRayProvider = DiagonalRayProvider(),
    ) -> ComputationResult[Dict[str, Span]]:
        """
        Action:
            1.  Handoff validation and calculation to the engine.
            2.  On engine failure send an exception chain in the ComputationResult. Otherwise, forward
                the result to the client.
        Args:
            origin: Coord
            engine: SpannerEngine
            coord_service: CoordService
            diagonal_ray_provider: DiagonalRayProvider
            
        Raises:
            BishopSpannerException
            
        Returns:
            ComputationResult[Span]
        """
        method = f"{cls.__name__}.compute"
        
        span_result = engine.compute(
            origin=origin,
            coord_service=coord_service,
            diagonal_ray_provider=diagonal_ray_provider,
        )
        # Handle the case that the span computation does not produce a result.
        if span_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                BishopSpannerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BishopSpannerException.MSG,
                    err_code=BishopSpannerException.ERR_CODE,
                    ex=span_result.exception
                
                )
            )
        # --- On success, send the dictionary in the success result. ---#
        return ComputationResult.success({"bishop": span_result.payload})
            
        
        
        
        
        
    