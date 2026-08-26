# src/operation/suite/operation/scalar/suite.py

"""
Module: operation.suite.operation.scalar.suite
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ScalarValidator
from fabrication import ScalarBuilder
from kit import OperationSuite, ScalarToolkit
from domain.model import Scalar


class ScalarOperationSuite(OperationSuite[Scalar]):
    """
    Role:
        -  Dependency Container
        -  Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a Scalar.

    Attributes:
        toolkit: Optional[ScalarToolkit]
        builder: Optional[ScalarBuilder]
        validator: Optional[ScalarValidator]

    Provides:

    Super Class:
        OperationSuite

    Notes:
        -  Suite for an empty class which makes managing toolkits easier.
        -  Any toolkits for a suite should be a Suite subclass.
    """
    
    def __init__(
            self,
            toolkit: Optional[ScalarToolkit] | None = None,
            builder: Optional[ScalarBuilder] | None = None,
            validator: Optional[ScalarValidator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[ScalarToolkit]
            builder: Optional[ScalarBuilder]
            validator: Optional[ScalarValidator]
        """
        super().__init__(
            toolkit=toolkit or ScalarToolkit(),
            builder=builder or ScalarBuilder(),
            validator=validator or ScalarValidator(),
        )
    
    @property
    def toolkit(self) -> ScalarToolkit:
        return cast(ScalarToolkit, super().bundle)
    
    @property
    def builder(self) -> ScalarBuilder:
        return cast(ScalarBuilder, super().builder)
    
    @property
    def validator(self) -> ScalarValidator:
        return cast(ScalarValidator, super().validator)


