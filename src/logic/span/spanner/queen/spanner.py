# src/logic/span/spanner/queen/queen.py

"""
Module: logic.span.spanner.queen.queen
Author: Banji Lawal
Created: 2026-03-10
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict

from logic.system import ComputationResult
from logic.coord import Coord, CoordService
from logic.span import (
    PerpendicularRayProvider, QueenSpannerException, DiagonalRayProvider, Span, Spanner, SpannerEngine
)


class QueenSpanner(Spanner):
    """
    # ROLE: Worker, Computation
    # Provide a spanning set for a Queen

    # RESPONSIBILITIES:
    1. Provide a spanning set for a Queen

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
            perpendicular_ray_provider: PerpendicularRayProvider = PerpendicularRayProvider()
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
            perpendicular_ray_provider: PerpendicularRayProvider
            
        Raises:
            QueenSpannerException
            
        Returns:
            ComputationResult[Span]
        """
        method = f"{cls.__name__}.compute"
        
        span_result = engine.compute(
            origin=origin,
            coord_service=coord_service,
            diagonal_ray_provider=diagonal_ray_provider,
            perpendicular_ray_provider=perpendicular_ray_provider,
        )
        # Handle the case that the span computation does not produce a result.
        if span_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                QueenSpannerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=QueenSpannerException.MSG,
                    err_code=QueenSpannerException.ERR_CODE,
                    ex=span_result.exception
                
                )
            )
        # --- On success, send the dictionary in the success result. ---#
        return ComputationResult.success({"queen": span_result.payload})
            
        
        
        
        
        
    