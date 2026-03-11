# src/logic/span/spanner/pawn/exception/pawn.py

"""
Module: logic.span.spanner.pawn.exception.pawn
Author: Banji Lawal
Created: 2026-03-10
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict, List

from logic.token import PawnToken
from logic.system import ComputationResult
from logic.coord import Coord, CoordService
from logic.vector import Vector, VectorService
from logic.span import PawnSpannerException, PawnVectorSets, Ray, Span, Spanner

class PawnSpanner(Spanner):
    """
    # ROLE: Worker, Computation
    # Provide a spanning set for a Pawn

    # RESPONSIBILITIES:
    1. Provide a spanning set for a Pawn

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
            pawn_token: PawnToken,
            coord_service: CoordService = CoordService(),
            vector_sets: PawnVectorSets = PawnVectorSets(),
            vector_service: VectorService = VectorService(),
    ) -> ComputationResult[Dict[str, Span]]:
        """
        Action:
            1.  If the pawn's origin is not certified as safe send and exception chain in the
                computation result.
            2.  Handoff solution development to process_vector_dictionary with the PawnVectorSet that 
                matches if the pawn
                    *   has been deployed only.
                    *   has made its opening move.

        Args:
            pawn_token: PawnToken
            vector_sets: PawnVectorSets
            coord_service: CoordService
            vector_service: VectorService
            
        Raises:
            PawnSpannerException
            
        Returns:
            ComputationResult[Span]
        """
        method = f"{cls.__name__}.compute"
        
        # Handle the case that the origin is not certified as a safe Coord.
        validation_result = coord_service.validator.validate(candidate=pawn_token.current_position)
        if validation_result.is_failure:
            return ComputationResult.failure(
                PawnSpannerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PawnSpannerException.MSG,
                    err_code=PawnSpannerException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Produce the spanning sets for a token that's new to the board. ---#
        if pawn_token.is_deployed:
            return cls._process_vector_dictionary(
                origin=pawn_token.current_position,
                vector_hash=vector_sets.developed_vector_sets,
                coord_service=coord_service,
                vector_service=vector_service,
            )
        # --- Otherwise produce the spanning sets for a pawn that's made its first move ---#
        return cls._process_vector_dictionary(
            origin=pawn_token.current_position,
            vector_hash=vector_sets.opening_vector_sets,
            coord_service=coord_service,
            vector_service=vector_service,
        )

    @classmethod
    def _process_vector_dictionary(
        cls,
        origin: Coord,
        coord_service: CoordService,
        vector_service: VectorService,
        vector_hash: Dict[str, List[Vector]],
    ) -> ComputationResult[Dict[str, Span]]:
        """
        Action:
            1.  For each key generate the spanning set. On success add to the dictionary. Otherwise,
                send an exception chain in the computation result.
            2.  After the loop has finished send the success result.

        Args:
            origin: Coord
            coord_service: CoordService
            vector_service: VectorService
            vector_hash: Dict[str, List[Vector]]

        Raises:
            PawnSpannerException

        Returns:
            ComputationResult[Span]
        """
        method = f"{cls.__name__}._process_vector_dictionary"
    
        span_hash = Dict[str, Span] = {}
        for key in vector_hash.keys():
            span_result = cls._span_helper(
                origin=origin,
                vectors=vector_hash[key],
                coord_service=coord_service,
                vector_service=vector_service,
            )
            # Handle the case that the span is not produced.
            if span_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    PawnSpannerException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=PawnSpannerException.MSG,
                        err_code=PawnSpannerException.ERR_CODE,
                        ex=span_result.exception
                    
                    )
                )
            # Add the span and its key to the hashtable.
            span_hash[key] = span_result.payload
            
        # --- Send the success resul to the client. ---#
        return ComputationResult.success(span_hash)
            
    @classmethod
    def _span_helper(
            cls,
            origin: Coord,
            vectors: List[Vector],
            coord_service: CoordService,
            vector_service: VectorService,
    ) -> ComputationResult[Span]:
        """
        Action:
            1.  Iterate through the vectors to get rays from the origin. If any ray derivation fails
                send an exception chain in the computation result. Else append to the span.
            2.  After the loop is finished send the span in the success result.

        Args:
            origin: Coord
            vectors: List[Vector]
            coord_service: CoordService
            vector_service: VectorService

        Raises:
            PawnSpannerException

        Returns:
            ComputationResult[Span]
        """
        method = f"{cls.__name__}._span_helper"
        
        span = Span(origin=origin, rays=[])
        for vector in vectors:
            ray_result = cls._pawn_ray(
                origin=origin,
                vector=vector,
                coord_service=coord_service,
                vector_service=vector_service,
            )
            # Handle the case that the ray computation is not completed.
            if ray_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    PawnSpannerException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=PawnSpannerException.MSG,
                        err_code=PawnSpannerException.ERR_CODE,
                        ex=ray_result.exception
                    
                    )
                )
            # Append the ray to the attack span.
            span.rays.append(ray_result.payload)
                
            # --- Send the success resul to the client. ---#
            return ComputationResult.success(span)

    @classmethod
    def _pawn_ray(
            cls,
            origin,
            vector: Vector,
            coord_service: CoordService,
            vector_service: VectorService,
    ) -> ComputationResult[Ray]:
        """
        Action:
            1.  If adding the vector to the array fails send an exception chain in the ComputationResult.
            2.  If the addition was successful
                    *   Append the addition's result to points array.
                    *   Create a ray using the origin and points array
                Then send the success result.
        """
        method = f"{cls.__name__}._pawn_ray"
        
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
                PawnSpannerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PawnSpannerException.MSG,
                    err_code=PawnSpannerException.ERR_CODE,
                    ex=addition_result.exception
                
                )
            )
        # --- Put the new point in an array. ---#
        points.append(addition_result.payload)
        
        # --- Create a new Ray and send in the success result. ---#
        return ComputationResult.success(Ray(origin=origin, points=points))
            
        
        
        
        
        
    