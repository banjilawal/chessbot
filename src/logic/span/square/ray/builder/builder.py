# src/logic/span/square/ray/builder/builder.py

"""
Module: logic.span.square.ray.builder.builder
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.coord import Coord
from logic.span import CoordRay, SquareRay, SquareRayBuildException
from logic.square import Square, SquareContext, SquareNotFoundException, SquareStackService
from logic.system import Builder, BuildResult, LoggingLevelRouter, SearchResult


class SquareRayBuilder(Builder[SquareRay]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            coord_ray: CoordRay,
            square_stack: SquareStackService,
    ) -> BuildResult[SquareRay]:
        """
        Map a CoordRay to a SquareRay
        Args:
            coord_ray: CoordRay
            square_stack: SquareStackService
            
        Returns:
            BuildResult[SquareRay]
        
        Raises:
              SquareRayBuildException
        """
        method = f"{cls.__class__.__name__}.build"
        
        # --- Find square which maps to the ray's origin. ---#
        origin_member_square_search_result = cls._search_square_by_coord(
            coord=coord_ray.origin,
            square_stack=square_stack
        )
        # Handle the case that the search does not succeed.
        if origin_member_square_search_result.is_failure:
            # Return the exception chain on failure.
            SearchResult.failure(
                SquareRayBuildException(
                    mthd=method,
                    op=SquareRayBuildException.OP,
                    msg=SquareRayBuildException.MSG,
                    err_code=SquareRayBuildException.ERR_CODE,
                    rslt_type=SquareRayBuildException.RSLT_TYPE,
                    ex=origin_member_square_search_result.exception,
                )
            )
        # --- Use the origin_square search result to initialize the SquareRay. ---#
        square_ray = SquareRay(origin=origin_member_square_search_result.payload[0])
        
        # --- Map the coord_ray's points to squares. ---#
        for coord in coord_ray.members:
            member_square_search_result = square_stack.query(context=SquareContext(coord))
            
            # Handle the case that the search does not succeed.
            if member_square_search_result.is_failure:
                # Return the exception chain on failure.
                SearchResult.failure(
                    SquareRayBuildException(
                        mthd=method,
                        op=SquareRayBuildException.OP,
                        msg=SquareRayBuildException.MSG,
                        err_code=SquareRayBuildException.ERR_CODE,
                        rslt_type=SquareRayBuildException.RSLT_TYPE,
                        ex=member_square_search_result.exception,
                    )
                )
             # --- Append the found square into ray's members ---#
            if member_square_search_result.payload[0] not in square_ray.members:
                square_ray.members.append(member_square_search_result.payload[0])
    
        # --- Send the built ray to the caller. ---#
        return BuildResult.success(square_ray)
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _search_square_by_coord(
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
            SquareRayBuildException
        """
        method = f"{cls.__class__.__name__}._search_square_by_coord"
        
        search_result = square_stack.query(context=SquareContext(coord=coord))
        # Handle the case that the query is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            SearchResult.failure(
                SquareRayBuildException(
                    mthd=method,
                    op=SquareRayBuildException.OP,
                    msg=SquareRayBuildException.MSG,
                    err_code=SquareRayBuildException.ERR_CODE,
                    rslt_type=SquareRayBuildException.RSLT_TYPE,
                    ex=search_result.exception,
                )
            )
        # Handle the case that, a square is not found.
        if search_result.is_empty:
            # Return the exception chain on failure.
            SearchResult.failure(
                SquareRayBuildException(
                    mthd=method,
                    op=SquareRayBuildException.OP,
                    msg=SquareRayBuildException.MSG,
                    err_code=SquareRayBuildException.ERR_CODE,
                    rslt_type=SquareRayBuildException.RSLT_TYPE,
                    ex=SquareNotFoundException(
                        var="coord",
                        val=f"{coord}",
                        msg=SquareRayBuildException.MSG,
                        err_code=SquareRayBuildException.ERR_CODE,
                    ),
                )
            )
        # --- Return the search success result. ---#
        return search_result