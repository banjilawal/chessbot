# src/geometry/span/spanner/king/king.py

"""
Module: geometry.span.spanner.king.king
Author: Banji Lawal
Created: 2026-03-10
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict, List

from system import ComputationResult
from model.math.coord import Coord, CoordService
from model.math.vector import Vector, VectorService
from math.span import KingSpannerException, CoordRay, CoordSpan, Spanner



class KingSpanner(Spanner):
    """
    Role:Worker, Computation
    # Provide a spanning set for a King

    Responsibilities:
    1. Provide a spanning set for a King

    Super Class:
        Spanner

    Provides:


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
            1.  If the origin does not pass a validation check. send and exception chain in the arithmetic
                result.
            2.  Iterate through the vectors to get rays from the origin. If any ray derivation fails
                send an exception chain in the arithmetic result. Else append to the span.
            3.  After the loop is finished send the span in the success result.

        Args:
            origin: Coord
            vectors: List[Vector]
            coord_service: CoordService
            vector_service: VectorService
            
        Raises:
            KingSpannerException
            
        Returns:
            ComputationResult[CoordSpan]
        """
        method = f"{cls.__name__}.compute"
        
        # Handle the case that the origin is not certified as a safe Coord.
        validation_result = coord_service.execute.build(candidate=origin)
        if validation_result.is_failure:
            return ComputationResult.failure(
                KingSpannerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=KingSpannerException.MSG,
                    err_code=KingSpannerException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Iterate through vectors to get the king's spanning set. ---#
        span = CoordSpan(origin=origin, rays=[])
        for vector in vectors:
            ray_computation_result = cls._king_ray(
                origin=origin,
                vector=vector,
                coord_service=coord_service,
                vector_service=vector_service,
            )
            # Handle the case that the ray arithmetic is not completed.
            if ray_computation_result.is_failure:
                # Send the exception chain on failure.
                return ComputationResult.failure(
                    KingSpannerException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=KingSpannerException.MSG,
                        err_code=KingSpannerException.ERR_CODE,
                        ex=ray_computation_result.exception
                    
                    )
                )
            # Include the ray in the span.
            span.rays.append(ray_computation_result.payload)
            
        # --- On success, send the dictionary in the success result. ---#
        return ComputationResult.success({"king": span})

    @classmethod
    def _king_ray(
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
        method = f"{cls.__name__}._king_ray"
        
        points: List[Coord] = []
        addition_result = coord_service.add_vector_to_coord(
            coord=origin,
            vector=vector,
            vector_service=vector_service
        )
        # Handle the case that the vector addition is not computed.
        if addition_result.is_failure:
            # Send the exception chain on failure.
            return ComputationResult.failure(
                KingSpannerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=KingSpannerException.MSG,
                    err_code=KingSpannerException.ERR_CODE,
                    ex=addition_result.exception
                
                )
            )
        # --- Put the new point in an array. ---#
        points.append(addition_result.payload)
        
        # --- Create a new CoordRay and send in the success result. ---#
        return ComputationResult.success(CoordRay(origin=origin, points=points))
            
        
        
        
        
        
    