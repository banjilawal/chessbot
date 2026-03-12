# src/logic/span/spanner/knight/exception/knight.py

"""
Module: logic.span.spanner.knight.exception.knight
Author: Banji Lawal
Created: 2026-03-10
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict, List

from logic.system import ComputationResult
from logic.coord import Coord, CoordService
from logic.vector import Vector, VectorService
from logic.span import KnightSpannerException, CoordRay, CoordSpan, Spanner

class KnightSpanner(Spanner):
    """
    # ROLE: Worker, Computation
    # Provide a spanning set for a Knight

    # RESPONSIBILITIES:
    1. Provide a spanning set for a Knight

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
            vectors: List[Vector],
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
    ) -> ComputationResult[Dict[str, CoordSpan]]:
        """
        Action:
            1.  If the origin is not certified as safe send and exception chain in the computation
                result.
            2.  Iterate through the vectors to get rays from the origin. If any ray derivation fails
                send an exception chain in the computation result. Else append to the span.
            3.  After the loop is finished send the span in the success result.

        Args:
            origin: Coord
            vectors: List[Vector]
            coord_service: CoordService
            vector_service: VectorService
            
        Raises:
            KnightSpannerException
            
        Returns:
            ComputationResult[CoordSpan]
        """
        method = f"{cls.__name__}.compute"
        
        # Handle the case that the origin is not certified as a safe Coord.
        validation_result = coord_service.validator.validate(candidate=origin)
        if validation_result.is_failure:
            return ComputationResult.failure(
                KnightSpannerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=KnightSpannerException.MSG,
                    err_code=KnightSpannerException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Iterate through vectors to get the knight's spanning set. ---#
        span = CoordSpan(origin=origin, rays=[])
        for vector in vectors:
            ray_result = cls._knight_ray(
                origin=origin,
                vector=vector,
                coord_service=coord_service,
                vector_service=vector_service,
            )
            # Handle the case that the ray computation is not completed.
            if ray_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    KnightSpannerException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=KnightSpannerException.MSG,
                        err_code=KnightSpannerException.ERR_CODE,
                        ex=ray_result.exception
                    
                    )
                )
            # Include the ray in the span.
            span.rays.append(ray_result.payload)
        
        # --- On success, send the dictionary in the success result. ---#
        return ComputationResult.success({"knight": span})
        

    @classmethod
    def _knight_ray(
            cls,
            origin,
            vector: Vector,
            coord_service: CoordService,
            vector_service: VectorService,
    ) -> ComputationResult[CoordRay]:
        """
        Action:
            1.  If adding the vector to the array fails send an exception chain in the ComputationResult.
            2.  If the addition was successful
                    *   Append the addition's result to points array.
                    *   Create a ray using the origin and points array
                Then send the success result.
        """
        method = f"{cls.__name__}._knight_ray"
        
        points: List[Coord] = []
        addition_result = coord_service.add_vector_to_coord(
            coord=origin,
            vector=vector,
            vector_service=vector_service
        )
        # Handle the case that the vector addition is not computed.
        if addition_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                KnightSpannerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=KnightSpannerException.MSG,
                    err_code=KnightSpannerException.ERR_CODE,
                    ex=addition_result.exception
                
                )
            )
        # --- Put the new point in an array. ---#
        points.append(addition_result.payload)
        
        # --- Create a new CoordRay and send in the success result. ---#
        return ComputationResult.success(CoordRay(origin=origin, points=points))
            
        
        
        
        
        
    