# src/chess/square/context/builder/builder.py

"""
Module: chess.square.context.builder.builder
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""


from typing import Optional

from chess.board import Board
from chess.coord import Coord, CoordIntegrityService
from chess.system import Builder, BuildResult, IdentityService
from chess.square import (
    NoSquareContextFlagSetException, SquareContext, SquareContextBuildFailedException,
    TooManySquareContextFlagsSetException
)


class SquareContextBuilder(Builder[SquareContext]):
    """"""
    
    @classmethod
    def build(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            coord: Optional[Coord] = None,
            board: Optional[Board] = None,
            coord_service: CoordIntegrityService = CoordIntegrityService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[SquareContext]:
        """"""
        method = "SquareContextBuilder.build"
        try:
            params = [id, name, coord]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoSquareContextFlagSetException(
                        f"{method}: "
                        f"{NoSquareContextFlagSetException.DEFAULT_MESSAGE}"
                    )
                )
            
            if param_count > 1:
                return BuildResult.failure(
                    TooManySquareContextFlagsSetException(
                        f"{method}: "
                        f"{TooManySquareContextFlagsSetException.DEFAULT_MESSAGE}"
                    )
                )
            
            if id is not None:
                id_validation = identity_service.validate_id(candidate=id)
                if id_validation.is_failure:
                    return BuildResult.failure(id_validation.exception)
                return BuildResult.success(SquareContext(id=id))
            
            if name is not None:
                name_validation = identity_service.validate_name(candidate=name)
                if name_validation.is_failure:
                    return BuildResult.failure(name_validation.exception)
                return BuildResult.success(SquareContext(name=name))
            
            if coord is not None:
                coord_validation = coord_service.item_validator.validate(coord)
                if coord_validation.is_failure:
                    return BuildResult.failure(coord_validation.exception)
                return BuildResult.success(SquareContext(coord=coord))
        
        except Exception as ex:
            return BuildResult.failure(
                SquareContextBuildFailedException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{SquareContextBuildFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )