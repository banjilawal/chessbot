# src/assurance/depend/service/model/scalar/depend.py

"""
Module: assurance.depend.service.model.scalar.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from assurance import ModelDependency
from domain import Scalar


class ScalarDependency(ModelDependency[Scalar]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy ScalarValidator's ResponseService dependencies.

    Attributes:

    Provides:

    Super Class:
        ModelDependency
    """
    
    def __init__():
        super().__init__()