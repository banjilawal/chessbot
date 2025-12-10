# src/chess/board/searcher/context/builder

"""
Module: chess.board.searcher.context.builder
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord, CoordValidator
from chess.system import BuildResult, Builder, IdValidator, NameValidator, LoggingLevelRouter
from chess.board import (
    BoardSearchContext, BoardSearchContextBuildFailedException, NoBoardSearchOptionSelectedException,
    MoreThanOneBoardSearchOptionPickedException,
)


class BoardSearchContextBuilder(Builder[BoardSearchContext]):
    """
    # ROLE: Builder, Data Integrity Guarantor

    # RESPONSIBILITIES:
    1.  Manage construction of BoardSearch instances that can be used safely by the client.
    2.  Ensure params for BoardSearch creation have met the application's safety contract.
    3.  Provide pluggable factories for creating different TeamSearchContext products.


    # PROVIDES:
    ValidationResult[TeamSearchContext] containing either:
        - On success:   TeamSearchContext in the payload.
        - On failure:   Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            id: Optional[int],
            name: Optional[str],
            coord: Optional[Coord],
            id_validator: type[IdValidator] = IdValidator,
            name_validator: type[NameValidator] = NameValidator,
            coord_validator: type[CoordValidator] = CoordValidator
    ) -> BuildResult[BoardSearchContext]:
        """
        # Action:
            1.  Use dependency injected validators to verify correctness of parameters required to
                builder a TeamSearchContext instance.
            2.  If the parameters are safe the TeamSearchContext is built and returned.

        # Parameters:
            *   id (Optional[int]):                     Selected if searcher target is an id.
            *   name (Optional[str]):                   Selected if searcher target is a name.
            *   target (Optional[Coord]):                Selected if searcher target is a target.
            *   id_validator (type[IdValidator]):       Validates an id-searcher-target
            *   name_validator (type[NameValidator]):   Validates a name-searcher-target
            *   builder (type[CoordBuilder]):     Validates a target-searcher-target

        # Returns:
        BuildResult[TeamSearchContext] containing either:
            - On success:   TeamSearchContext in the payload.
            - On failure:   Exception.

        # Raises:
            *   BoardSearchContextBuildFailedException
            *   NoBoardSearchOptionSelectedException
            *   MoreThanOneBoardSearchOptionPickedException
        """
        method = "BoardSearchContextBuilder.builder"
        
        try:
            params = [id, name, coord]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoBoardSearchOptionSelectedException(
                        f"{method}: {NoBoardSearchOptionSelectedException.DEFAULT_MESSAGE}"
                    )
                )
            
            if param_count > 1:
                return BuildResult.failure(
                    MoreThanOneBoardSearchOptionPickedException(
                        f"{method}: {MoreThanOneBoardSearchOptionPickedException.DEFAULT_MESSAGE}"
                    )
                )
            
            if id is not None:
                return cls.build_id_search_context(id=id, id_validator=id_validator)
            
            if name is not None:
                return cls.build_name_search_context(name=name, name_validator=name_validator)
            
            if coord is not None:
                return cls.build_coord_search_context(coord=coord, coord_validator=coord_validator)
        
        except Exception as ex:
            return BuildResult.failure(
                BoardSearchContextBuildFailedException(
                    f"{method}: {BoardSearchContextBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_id_search_context(
            cls,
            id: int,
            id_validator: type[IdValidator] = IdValidator
    ) -> BuildResult[BoardSearchContext]:
        """
        # Action:
        Build an id-TeamSearchContext if IdValidator verifies searcher target is safe.

        # Parameters:
          *     id (int):                           target id
          *     id_validator (type[IdValidator]):   validates target.

        # Returns:
          ValidationResult[TeamSearchContext] containing either:
                - On success:   TeamSearchContext in the payload.
                - On failure:   Exception.

        # Raises:
            *   InvalidBoardSearchContextException
        """
        method = "BoardSearchContextBuilder.build_id_search_context"
        try:
            id_validation = id_validator.validate(id)
            if id_validation.is_failure():
                return BuildResult.failure(id_validation.exception)
            
            return BuildResult.success(payload=BoardSearchContext(id=id_validation.payload))
        
        except Exception as ex:
            return BuildResult.failure(
                BoardSearchContextBuildFailedException(
                    f"{method}: {BoardSearchContextBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_name_search_context(
            cls,
            name: str,
            name_validator: type[NameValidator] = NameValidator
    ) -> BuildResult[BoardSearchContext]:
        """
        # Action:
        Build a name-TeamSearchContext if NameValidator verifies searcher target is safe.

        # Parameters:
            *   name (str):                             target name
            *   name_validator (type[NameValidator]):   validates target.

        # Returns:
          ValidationResult[TeamSearchContext] containing either:
                - On success:   TeamSearchContext in the payload.
                - On failure:   Exception.

        # Raises:
            *   InvalidBoardSearchContextException
        """
        method = "BoardSearchContextBuilder.build_name_search_context"
        
        try:
            name_validation = name_validator.validate(name)
            if name_validation.is_failure():
                return BuildResult.failure(name_validation.exception)
            
            return BuildResult.success(payload=BoardSearchContext(name=name_validation.payload))
        
        except Exception as ex:
            return BuildResult.failure(
                BoardSearchContextBuildFailedException(
                    f"{method}: {BoardSearchContextBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_coord_search_context(
            cls,
            coord: Coord,
            coord_validator: type[CoordValidator] = CoordValidator
    ) -> BuildResult[BoardSearchContext]:
        """
        # Action:
        Build a target-TeamSearchContext if CoordValidator verifies searcher target is safe.

        # Parameters:
          *     target (Coord):                              target Coord
          *     validator (type[CoordValidator]):     validates target.

        # Returns:
        ValidationResult[TeamSearchContext] containing either:
            - On success:   TeamSearchContext in the payload.
            - On failure:   Exception.

        # Raises:
            *   InvalidBoardSearchContextException
        """
        method = "BoardSearchContextBuilder.build_coord_search_context"
        
        try:
            coord_validation = coord_validator.validate(coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            return BuildResult.success(payload=BoardSearchContext(name=coord_validation.payload))
        
        except Exception as e:
            return BuildResult.failure(
                BoardSearchContextBuildFailedException(
                    f"{method}: {BoardSearchContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
