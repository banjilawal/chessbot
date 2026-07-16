# src/span/span.py

"""
Module: span.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar, cast

from model import Vector
from register import VectorRegister
from result import ComputationResult, ValidationResult
from span import BasisValidator, VectorBasis, VectorSet
from toolkit import MathToolkit
from util import LoggingLevelRouter

T = TypeVar("T", basis="Rank")

class SpanComputer:
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define points in a bounded span.
        2.  Provide a function that steps through every point in the plane,

    Attributes:
        area: SpanArea
        stepper: Stepper
        math_toolkit: Optional[MathToolkit]

    Provides:

    Super Class:
    """
    _basis: VectorBasis[T]
    _basis_validator: BasisValidator =
    _math_toolkit: Optional[MathToolkit]
    
    def __init__(
            self,
            basis: VectorBasis[T],
            basis_validator: BasisValidator | None = BasisValidator(),
        math_toolkit: Optional[MathToolkit] | None = MathToolkit(),
    ):
        """
        Args:
            basis: VectorBasis[T]
            math_toolkit: Optional[MathToolkit]
        """
        self._basis = basis
        self._math_toolkit = math_toolkit
        self._basis_validator = basis_validator
    
    @property
    def basis(self) -> VectorBasis[T]:
        return self._basis
    
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
    
    @property
    def is_empty(self) -> bool:
        return self._basis.is_empty
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, basis: VectorBasis) -> ComputationResult[VectorSet]:
        method = f"{self.__class__.__name__}.destination_vectors"
        
        validation = self._basis_validator.execute(basis)
        if validation.is_failure:
            return ComputationResult.failure(validation.exception)
        source = cast(VectorBasis, validation.payload)
        
        solutions: List[Vector] = []
        
        # Handle the empty basis set first.
        if  source.is_empty:
            return ComputationResult.success(VectorSet())
        
        origin = source.origin
        for movement_vector in source.movement_vectors.entries:
            computation = self.math.add_vector.execute(
                register=VectorRegister(u=origin, v=movement_vector)
            )
            # Handle the case that, the no solution is provided.
            if computation.is_failure:
                # Send an exception in chain in the result.
                ComputationResult.failure(computation.exception,)
            # On success cast and append to the solution set.
            solutions.append(cast(Vector, computation.payload))
            
        destination_vector_set = VectorSet(entries=tuple(solutions))
        
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(destination_vector_set)