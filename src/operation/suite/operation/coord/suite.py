# src/operation/suite/operation/coord/suite.py

"""
Module: operation.suite.operation.coord.suite
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import CoordValidator
from fabrication import CoordBuilder
from kit import OperationSuite, CoordToolkit
from domain.model import Coord


class CoordOperationSuite(OperationSuite[Coord]):
    """
    Role:
        -  Dependency Container
        -  Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a Coord.

    Attributes:
        toolkit: Optional[CoordToolkit]
        builder: Optional[CoordBuilder]
        validator: Optional[CoordValidator]

    Provides:

    Super Class:
        OperationSuite

    Notes:
        -  Suite for an empty class which makes managing toolkits easier.
        -  Any toolkits for a suite should be a Suite subclass.
    """
    
    def __init__(
            self,
            toolkit: Optional[CoordToolkit] | None = None,
            builder: Optional[CoordBuilder] | None = None,
            validator: Optional[CoordValidator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[CoordToolkit]
            builder: Optional[CoordBuilder]
            validator: Optional[CoordValidator]
        """
        super().__init__(
            toolkit=toolkit or CoordToolkit(),
            builder=builder or CoordBuilder(),
            validator=validator or CoordValidator(),
        )
    
    @property
    def toolkit(self) -> CoordToolkit:
        return cast(CoordToolkit, super().bundle)
    
    @property
    def builder(self) -> CoordBuilder:
        return cast(CoordBuilder, super().builder)
    
    @property
    def validator(self) -> CoordValidator:
        return cast(CoordValidator, super().validator)


