# src/span/span.py

"""
Module: span.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import List, Optional, cast

from container import VectorSet
from model import Vector
from register import VectorRegister
from result import ComputationResult
from span import VectorBasis
from toolkit import MathToolkit
from util import LoggingLevelRouter
from validator import BasisValidator


class DestinationSpanComputer:
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
    _basis_validator: BasisValidator
    _math_toolkit: Optional[MathToolkit]
    
    def __init__(
            self,
            basis_validator: BasisValidator | None = BasisValidator(),
            math_toolkit: Optional[MathToolkit] | None = MathToolkit(),
    ):
        """
        Args:
            basis_validator: BasisValidator
            math_toolkit: Optional[MathToolkit]
        """
        self._math_toolkit = math_toolkit
        self._basis_validator = basis_validator
    
    @property
    def basis_validator(self) -> BasisValidator:
        return self._basis_validator
    
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, vector_basis: VectorBasis) -> ComputationResult[VectorSet]:
        method = f"{self.__class__.__name__}.destination_vectors"
        
        # Handle the case that, the vector_basis is not safe.
        validation = self._basis_validator.execute(vector_basis)
        if validation.is_failure:
            return ComputationResult.failure(validation.exception)
        basis = cast(VectorBasis, validation.payload)
        
        solutions: List[Vector] = []
        
        # Handle the empty basis set first.
        if  basis.is_empty:
            return ComputationResult.success(VectorSet())
        
        origin = basis.origin
        for movement_vector in basis.movement_vectors:
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