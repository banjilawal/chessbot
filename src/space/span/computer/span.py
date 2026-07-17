# src/space/span/span.py

"""
Module: space.span.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import List, Optional, cast

from container import VectorSet
from err import DestinationSpanComputerException
from model import Vector
from register import VectorRegister
from result import ComputationResult, MethodResultType
from space.span import VectorBasis
from toolkit import MathToolkit
from util import LoggingLevelRouter
from validator import BasisValidator


class DestinationSpanComputer:
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Provide a set of destination vectors spanned from a basis set of movement vectors and
            an origin.

    Attributes:
        basis_validator: BasisValidator
        math_toolkit: Optional[MathToolkit]

    Provides:
        -   def execute(vector_basis: VectorBasis) -> ComputationResult[VectorSet]
        
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
        """
        Verify the object is a String that is safe to use.

        Action:
            1.  Send an exception chain in the ComputationResult if any of the following occur.
                    -   The basis gets flagged unsafe.
                    -   VectorAdder cannot provide a solution.
            2.  Otherwise, after each VectorAdder solution is stored put them in a VectorSet then,
                sendi in the success result.
        Args:
            vector_basis: VectorBasis
        Returns:
            ComputationResult[VectorSet]
        Raises:
            DestinationSpanComputerException
        """
        method = f"{self.__class__.__name__}.destination_vectors"
        
        # Handle the case that, the vector_basis is not safe to use.
        validation = self._basis_validator.execute(vector_basis)
        if validation.is_failure:
            # Send an exception in chain in the result.
            return ComputationResult.failure(
                DestinationSpanComputerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DestinationSpanComputerException.MSG,
                    err_code=DestinationSpanComputerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=validation.exception,
                ),
            )
        # --- Cast the validation product for additional processing ---#
        basis = cast(VectorBasis, validation.payload)
        solutions: List[Vector] = []
        
        # Handle the empty basis set first.
        if  basis.is_empty:
            return ComputationResult.success(VectorSet())
        
        # --- Process nonempty basis sets. ---#
        origin = basis.origin
        for movement_vector in basis.movement_vectors.iterator:
            # Request that, a solution for the destination vector.
            computation = self.math.add_vector.execute(
                register=VectorRegister(
                    u=origin,
                    v=movement_vector
                )
            )
            # Handle the case that, the request is not fulfilled.
            if computation.is_failure:
                # Send an exception in chain in the result.
                return ComputationResult.failure(
                    DestinationSpanComputerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=DestinationSpanComputerException.MSG,
                        err_code=DestinationSpanComputerException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                        ex=computation.exception,
                    ),
                )
            # On success cast and append to destination vector to the solution set.
            solutions.append(cast(Vector, computation.payload))
            
        # Convert the solution set into a Tuple, for a VectorSet.
        destination_vector_set = VectorSet(entries=tuple(solutions))
        
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(destination_vector_set)