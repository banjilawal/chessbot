# src/toolkit/operand/toolkit.py

"""
Module: toolkit.operand.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from operation import CoordValidator, ScalarValidator, VectorValidator
from pipeline import ScalarBuildPipeline, VectorBuildPipeline
from pipeline.build.coord import CoordBuildPipeline
from toolkit import Toolkit
from model import VectorOperand


@dataclass
class VectorOperandToolkit(Toolkit[VectorOperand]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Collection of workers and validators that are required for VectorOperand tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.
    
    Attributes:
        coord_validator: CoordValidator
        vector_validator: VectorValidator
        scalar_validator: ScalarValidator
    
    Provides:
    
    Super Class:
        Toolkit
    """
    _coord_builder: CoordBuildPipeline
    _vector_builder: VectorBuildPipeline
    _scalar_builder: ScalarBuildPipeline
    _coord_validator: CoordValidator
    _vector_validator: VectorValidator
    _scalar_validator: ScalarValidator
    
    def __init__(
            self,
            coord_builder: CoordBuildPipeline | None = None,
            vector_builder: VectorBuildPipeline | None = None,
            scalar_builder: ScalarBuildPipeline | None = None,
            coord_validator: CoordValidator | None = None,
            vector_validator: VectorValidator | None = None,
            scalar_validator: ScalarValidator | None = None,
    ):
        """
        Args:
            coord_builder: CoordBuildPipeline
            vector_builder: VectorBuildPipeline
            scalar_builder: ScalarBuildPipeline
            coord_validator: CoordValidator
            vector_validator: VectorValidator
            scalar_validator: ScalarValidator
        """
        super().__init__()
        self._coord_builder = coord_builder or CoordBuildPipeline()
        self._vector_builder = vector_builder or VectorBuildPipeline()
        self._scalar_builder = scalar_builder or ScalarBuildPipeline()
        self._coord_validator = coord_validator or CoordValidator()
        self._vector_validator = vector_validator or VectorValidator()
        self._scalar_validator = scalar_validator or ScalarValidator()
        
    @property
    def coord_builder(self) -> CoordBuildPipeline:
        return self._coord_builder
    
    @property
    def vector_builder(self) -> VectorBuildPipeline:
        return self._vector_builder
    
    @property
    def scalar_builder(self) -> ScalarBuildPipeline:
        return self._scalar_builder
    
    @property
    def coord_validator(self) -> CoordValidator:
        return self._coord_validator
    
    @property
    def vector_validator(self) -> VectorValidator:
        return self._vector_validator
    
    @property
    def scalar_validator(self) -> ScalarValidator:
        return self._scalar_validator
    
