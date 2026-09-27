# src/assurance/depend/wrapper/model/path/depend.py

"""
Module: assurance.depend.wrapper.model.path.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelWrapperDependency, SquareRegisterValidator
from domain import Path


class PathWrapperDependency(ModelWrapperDependency[Path]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy PathValidator's ResponseWrapper dependencies.

    Attributes:
        endpoint_validator: SquareRegisterValidator
        
    Provides:

    Super Class:
        ModelWrapperDependency
    """

    _endpoint: SquareRegisterValidator
    
    def __init__(
            self,
            endpoint: Optional[SquareRegisterValidator] | None = None,
    ):
        """
        Args:
            endpoint: Optional[SquareRegisterValidator]
        """
        super().__init__()
        self._endpoint = endpoint or SquareRegisterValidator()
        
    @property
    def endpoint(self) -> SquareRegisterValidator:
        return self._endpoint