# src/chess/coord/context/service/service.py

"""
Module: chess.coord.context.service.service
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Optional

from chess.coord import CoordContext, CoordContextBuilder, CoordContextValidator
from chess.system import BuildResult, SearchContext, SearchContextService


class CoordContextService(SearchContextService[CoordContext]):
    """
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single entry point for CoordContextBuilder and CoordContextValidator objects.
    2.  Passing its self._validator to the self._builder simplifies the SearchContext lifecycle.
    3.  Protects SearchContext from direct, unprotected access.
    4.  Public facing API.

    # PROVIDES:
        *   Direct access tp CoordContextValidator
        *   Interface to CoordContextBuilder

    # ATTRIBUTES:
        *   _builder (CoordContextBuilder):
        *   _validator (CoordContextValidator):
    """
    _builder: CoordContextBuilder
    _validator: CoordContextValidator
    
    @property
    def validator(self) -> CoordContextValidator:
        """
        Validators may have extra features and logic.
        Direct access is given ta all the Validator's capabilities.
        """
        return self._validator
    
    def build(self, row: Optional[int], column: Optional[int]) -> BuildResult[SearchContext]:
        """
        # ACTION:
        1.  Pass the row and column parameters to the internal CoordContextBuilder which uses the internal validator.
        2.  The builder returns a ValidationResult containing either the CoordContext or an Exception.

        # PARAMETERS:
        At least one of the following must be provided:
            *   row (Optional[int]):
            *   column (Optional[int]):

        # Returns:
        BuildResult[CoordContext] containing either:
            - On success: CoordContext in the payload.
            - On failure: Exception.

        # RAISES:
        None
        """
        return self._builder.build(row=row, column=column, validator=self._validator)