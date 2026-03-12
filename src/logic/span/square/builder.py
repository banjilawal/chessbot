# src/logic/span/square/builder.py

"""
Module: logic.span.square.builder
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations

from typing import List

from logic.coord import Coord
from logic.span.square.exception import SquareSpanBuildException
from logic.square import Square, SquareContext, SquareNotFoundException, SquareStackService
from logic.span import CoordRay, CoordSpan, SquareRay, SquareSpan
from logic.system import BuildResult, Builder, ComputationResult, LoggingLevelRouter, SearchResult


class SquareSpanBuilder(Builder[SquareSpan]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, coord_span: CoordSpan, square_stack: SquareStackService) -> BuildResult[SquareSpan]:
        """
        Args:
            coord_span: CoordSpan
            square_stack: SquareStackService
            
        Returns:
            BuildResult[SquareSpan]
            
        Raises:
            SquareSpanBuildException
        """
        method = f"{cls.__class__.__name__}.build"
        
        # --- Find square which maps to the ray's origin. ---#
        square_span_origin_result = cls._square_from_coord(
            coord=coord_span.origin,
            square_stack=square_stack
        )
        # Handle the case that the search does not succeed.
        if square_span_origin_result.is_failure:
            # Return the exception chain on failure.
            SearchResult.failure(
                SquareSpanBuildException(
                    mthd=method,
                    op=SquareSpanBuildException.OP,
                    msg=SquareSpanBuildException.MSG,
                    err_code=SquareSpanBuildException.ERR_CODE,
                    rslt_type=SquareSpanBuildException.RSLT_TYPE,
                    ex=square_span_origin_result.exception,
                )
            )
        # --- Hand off the SquareSpan production to the helper. ---#
        return cls._square_span_build_helper(
            coord_span=coord_span,
            square_stack=square_stack,
            origin_square=square_span_origin_result.payload[0]
        )

    @classmethod
    @LoggingLevelRouter.monitor
    def _square_span_build_helper(
            cls,
            coord_span: CoordSpan,
            origin_square: Square,
            square_stack: SquareStackService
    ) -> BuildResult[SquareSpan]:
        """
        Args:
            origin_square: Square
            coord_span: CoordSpan
            square_stack: SquareStackService
            
        Returns:
            BuildResult[SquareSpan]
            
        Raises:
            SquareSpanBuildException
        """
        method = f"{cls.__class__.__name__}.square_span_build_helper"
        
        # --- Use the origin_square search result to initialize the SquareRay. ---#
        square_span = SquareSpan(origin=origin_square, rays=[])
        
        # --- Derive the SquareRays from the CoordRays---#
        for coord_ray in coord_span.rays:
            derivation_result = cls._derive_square_ray(
                coord_ray=coord_ray,
                square_stack=square_stack,
            )
            # Handle the case that the derivation does not produce a result.
            if derivation_result.is_failure:
                # Return the exception chain on failure.
                BuildResult.failure(
                    SquareSpanBuildException(
                        mthd=method,
                        op=SquareSpanBuildException.OP,
                        msg=SquareSpanBuildException.MSG,
                        err_code=SquareSpanBuildException.ERR_CODE,
                        rslt_type=SquareSpanBuildException.RSLT_TYPE,
                        ex=derivation_result.exception,
                    )
                )
            # --- Append the square_ray derivation to its span. ---#
            square_span.rays.append(derivation_result.payload)
        
        # --- Send the square_span to the caller. ---#
        return BuildResult.success(square_span)
        
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _derive_square_ray(
            cls,
            coord_ray: CoordRay,
            square_stack: SquareStackService,
    ) -> ComputationResult[SquareRay]:
        """
        Map a CoordRay to a SquareRay
        Args:
            coord_ray: CoordRay
            square_stack: SquareStackService
            
        Returns:
            BuildResult[SquareRay]
        
        Raises:
              SquareSpanBuildException
        """
        method = f"{cls.__class__.__name__}._derive_square_ray"
        
        # --- Find square which maps to the ray's origin. ---#
        square_ray_origin_result = cls._square_from_coord(
            coord=coord_ray.origin,
            square_stack=square_stack
        )
        # Handle the case that the search does not succeed.
        if square_ray_origin_result.is_failure:
            # Return the exception chain on failure.
            SearchResult.failure(
                SquareSpanBuildException(
                    mthd=method,
                    op=SquareSpanBuildException.OP,
                    msg=SquareSpanBuildException.MSG,
                    err_code=SquareSpanBuildException.ERR_CODE,
                    rslt_type=SquareSpanBuildException.RSLT_TYPE,
                    ex=square_ray_origin_result.exception,
                )
            )
        # --- Use the origin_square search result to initialize the SquareRay. ---#
        square_ray = SquareRay(origin=square_ray_origin_result.payload[0], points=[])
        
        # --- Map the coord_ray's points to squares. ---#
        for coord in coord_ray.points:
            square_search_result = cls._square_from_coord(
                coord=coord,
                square_stack=square_stack
            )
            # Handle the case that the search does not succeed.
            if square_search_result.is_failure:
                # Return the exception chain on failure.
                SearchResult.failure(
                    SquareSpanBuildException(
                        mthd=method,
                        op=SquareSpanBuildException.OP,
                        msg=SquareSpanBuildException.MSG,
                        err_code=SquareSpanBuildException.ERR_CODE,
                        rslt_type=SquareSpanBuildException.RSLT_TYPE,
                        ex=square_search_result.exception,
                    )
                )
             # --- Append the found square into square_ray's members ---#
            if square_search_result.payload[0] not in square_ray.points:
                square_ray.points.append(square_search_result.payload[0])
    
        # --- Send the built square_ray to the caller. ---#
        return ComputationResult.success(square_ray)
        
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _square_from_coord(
            cls,
            coord: Coord,
            square_stack: SquareStackService
    ) -> SearchResult[List[Square]]:
        """
        Find a square at the Coord.
        
        Args:
            coord: Coord
            square_stack: SquareStackService
            
        Returns:
            SearchResult[SquareSpan]
            
        Raises:
            SquareNotFoundException
            SquareSpanBuildException
        """
        method = f"{cls.__class__.__name__}.square_from_coord"
        
        search_result = square_stack.query(context=SquareContext(coord=coord))
        # Handle the case that the query is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            SearchResult.failure(
                SquareSpanBuildException(
                    mthd=method,
                    op=SquareSpanBuildException.OP,
                    msg=SquareSpanBuildException.MSG,
                    err_code=SquareSpanBuildException.ERR_CODE,
                    rslt_type=SquareSpanBuildException.RSLT_TYPE,
                    ex=search_result.exception,
                )
            )
        # Handle the case that, a square is not found.
        if search_result.is_empty:
            # Return the exception chain on failure.
            SearchResult.failure(
                SquareSpanBuildException(
                    mthd=method,
                    op=SquareSpanBuildException.OP,
                    msg=SquareSpanBuildException.MSG,
                    err_code=SquareSpanBuildException.ERR_CODE,
                    rslt_type=SquareSpanBuildException.RSLT_TYPE,
                    ex=SquareNotFoundException(
                        var="coord",
                        val=f"{coord}",
                        msg=SquareSpanBuildException.MSG,
                        err_code=SquareSpanBuildException.ERR_CODE,
                    ),
                )
            )
        # --- Return the search success result. ---#
        return search_result