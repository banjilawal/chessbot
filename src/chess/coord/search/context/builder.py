# src/chess/coord/search/context/builder.py

"""
Module: chess.coord.search.context.builder
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord, CoordValidator
from chess.system import BuildResult, Builder, CoordValidator, CoordValidator, LoggingLevelRouter
from chess.coord import (
    CoordSearchContext, CoordSearchContextBuildFailedException, NoCoordSearchOptionSelectedException,
    MoreThanOneCoordSearchOptionPickedException,
)


class CoordSearchContextBuilder(Builder[CoordSearchContext]):
    """
    # ROLE: Builder

    # RESPONSIBILITIES:
        1. Manage conintuction of CoordSearch instances that can be used safely by the client.
        2. Ensure params for CoordSearch creation have met the application's safety contract.
        3. Provide pluggable factories for creating different CoordSearchContext products.


    # PROVIDES:
      ValidationResult[CoordSearchContext] containing either:
            - On success: CoordSearchContext in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            row: Optional[int],
            column: Optional[int],
            coord: Optional[Coord],
            coord_validator: type[CoordValidator] = CoordValidator
    ) -> BuildResult[CoordSearchContext]:
        """
        # Action:
            1. Use dependency injected validators to verify correctness of parameters required to
                build a CoordSearchContext instance.
            2. If the parameters are safe the CoordSearchContext is built and returned.

        # Parameters:
            * row (Optional[int]): selected if search target is an id.
            * column (Optional[int]): selected if search target is a column.
            * coord (Optional[Coord]): selected if search target is a coord.
            * coord_validator (type[CoordValidator]): validates an id-search-target

        # Returns:
          BuildResult[CoordSearchContext] containing either:
                - On success: CoordSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * CoordSearchContextBuildFailedException
            * NoCoordSearchOptionSelectedException
            * MoreThanOneCoordSearchOptionPickedException
        """
        method = "CoordSearchContextBuilder.build"
        
        try:
            params = [row, column, coord]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoCoordSearchOptionSelectedException(
                        f"{method}: {NoCoordSearchOptionSelectedException.DEFAULT_MESSAGE}"
                    )
                )
            
            if param_count > 1:
                return BuildResult.failure(
                    MoreThanOneCoordSearchOptionPickedException(
                        f"{method}: {MoreThanOneCoordSearchOptionPickedException.DEFAULT_MESSAGE}"
                    )
                )
            
            if row is not None:
                return cls.build_row_search_context(row=row, coord_validator=coord_validator)
            
            if column is not None:
                return cls.build_ncolumn_search_context(column=column, coord_validator=coord_validator)
            
            if coord is not None:
                return cls.build_coord_search_context(coord=coord, coord_validator=coord_validator)
        
        except Exception as ex:
            return BuildResult.failure(
                CoordSearchContextBuildFailedException(
                    f"{method}: {CoordSearchContextBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_row_search_context(
            cls,
            row: int,
            coord_validator: type[CoordValidator] = CoordValidator
    ) -> BuildResult[CoordSearchContext]:
        """
        # Action:
        Build an id-CoordSearchContext if CoordValidator verifies search target is safe.

        # Parameters:
          * row (int): target id
          * coord_validator (type[CoordValidator]): validates target.

        # Returns:
          ValidationResult[CoordSearchContext] containing either:
                - On success: CoordSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * InvalidCoordSearchContextException
        """
        method = "CoordSearchContextBuilder.build_id_search_context"
        try:
            row_validation = coord_validator.validate_row(row)
            if row_validation.is_failure():
                return BuildResult.failure(row_validation.exception)
            
            return BuildResult.success(payload=CoordSearchContext(id=row))
        
        except Exception as ex:
            return BuildResult.failure(
                CoordSearchContextBuildFailedException(
                    f"{method}: {CoordSearchContextBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_column_search_context(
            cls,
            column: int,
            coord_validator: type[CoordValidator] = CoordValidator
    ) -> BuildResult[CoordSearchContext]:
        """
        # Action:
        Build a column-CoordSearchContext if CoordValidator verifies search target is safe.

        # Parameters:
          * column (int): target column
          * coord_validator (type[CoordValidator]): validates target.

        # Returns:
          ValidationResult[CoordSearchContext] containing either:
                - On success: CoordSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * InvalidCoordSearchContextException
        """
        method = "CoordSearchContextBuilder.build_column_search_context"
        
        try:
            column_validation = coord_validator(column)
            if column_validation.is_failure():
                return BuildResult.failure(column_validation.exception)
            
            return BuildResult.success(payload=CoordSearchContext(column=column))
        
        except Exception as ex:
            return BuildResult.failure(
                CoordSearchContextBuildFailedException(
                    f"{method}: {CoordSearchContextBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_coord_search_context(
            cls,
            coord: Coord,
            coord_validator: type[CoordValidator] = CoordValidator
    ) -> BuildResult[CoordSearchContext]:
        """
        # Action:
        Build a coord-CoordSearchContext if CoordValidator verifies search target is safe.

        # Parameters:
          * coord (Coord): target Coord
          * coord_validator (type[CoordValidator]): validates target.

        # Returns:
          ValidationResult[CoordSearchContext] containing either:
                - On success: CoordSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * InvalidCoordSearchContextException
        """
        method = "CoordSearchContextBuilder.build_coord_search_context"
        
        try:
            coord_validation = coord_validator.validate(coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            return BuildResult.success(payload=CoordSearchContext(column=coord_validation.payload))
        
        except Exception as e:
            return BuildResult.failure(
                CoordSearchContextBuildFailedException(
                    f"{method}: {CoordSearchContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
