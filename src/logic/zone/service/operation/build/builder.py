# src/logic/zone/service/operation/build/validator.py

"""
Module: logic.zone.service.operation.build.transaction
Author: Banji Lawal
Created: 2026-03-29
version: 1.0.0
"""

from __future__ import annotations

from logic.zone import Zone
from catalog.schema import SchemaService
from system import Builder, BuildResult, GameColor, LoggingLevelRouter


class ZoneBuilder(Builder[Zone]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Zone creation process owner.
        2.  Ensure Zone build resources meet satisfy contracts.
        3.  Assure Zone instances comply with business logic at point of creation.

     Attributes:
     
    Provides:
        -   execute(
                    row: int,
                    column: int,
                    number_validation: NumberValidator,
            ) -> BuildResult[Zone]

     Super Class:
         Builder
     """
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            color: GameColor,
            schema_service: SchemaService,
    ) -> BuildResult[Zone]:
        """
        Build a Zone.
        
        Action:
            1.  Send an exception chain in the BuildResult if either:
                    -   The row
                    -   The column
                are fail its validation checks.
            2.  Otherwise, build the Zone then, send the success reult.
        Args:
            color: GameColor
            schema_service: SchemaService
        Returns:
            BuildResult[Zone]
        Raises:
            ZoneBuildException
        """
        method = f"{cls.__name__}.build"
        return BuildResult()
