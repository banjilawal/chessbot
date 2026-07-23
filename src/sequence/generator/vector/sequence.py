# src/sequence/generator/vector/sequence.py

"""
Module: sequence.generator.vector.sequence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional, cast

from container import VectorSet
from err import NullException
from model import Vector
from result import ComputationResult
from sequence import VectorSequenceSpec
from toolkit import MathToolkit
from util import LoggingLevelRouter


class VectorSequenceGenerator:
    """
    Role:
        -   Computation
        -   Integrity Assurance

    Responsibilities:
        Define x_step and slope for getting the next vector northeast of origin.
            -   x_step = -1,
            -   slope = 1

    Attributes:
        math: Optional[MathToolkit]

    Provides:
        -   def execute(specification: VectorSequenceSpec) -> ComputationResult[VectorSet]
        
    Super Class:
        QuadrantMapFunction
    """
    _math: MathToolkit
    
    def ___init__(
            self,
            math: Optional[MathToolkit] | None = MathToolkit()
    ):
        """
        Args:
            math: Optional[MathToolkit]
        """
    
    
    @LoggingLevelRouter.monitor
    def execute(self, specification: VectorSequenceSpec) -> ComputationResult[VectorSet]:
        """
        Get the next Vector using addition.

        Action:
            1.  Set
                    x_next = x_current + x_step
                    y_next = (2 * slope * y_current) + slope
            2.  If VectorBuilder cannot create a safe Vector from x_next, y_next, send
                an exception chain in the ComputationResult.
            3.  Otherwise, cast the build product, then send in the success result.
        Args:
            vector: Vector
        Returns:
            ComputationResult[Vector]
        Raises:
             AxisMappingException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the sequence gets flagged,
        validation = self._math.priming_validator.execute(
            candidate=specification,
            target_model=VectorSequenceSpec,
            null_exception=NullException(),
        )
        if validation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                VectorSequenceGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorSequenceGeneratorException.MSG,
                    err_code=VectorSequenceGeneratorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=validation.exception,
                ),
            )
        # --- Cast the validation product and setup for the iteration. ---#
        spec = cast(VectorSequenceSpec, validation.payload)
        sequence: List[Vector] = []
        cursor = spec.space.origin
        terminus = spec.space.terminus
        
        while cursor != terminus:
            sequence.append(cursor)
            
            # Request that the update for the cursor.
            step = spec.mapping_function.next(cursor)
            
            # Handle the case that, the request is not satisfied.
            if step.is_failure:
                # Send an exception chain in the result.
                return ComputationResult.failure(
                    VectorSequenceGeneratorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorSequenceGeneratorException.MSG,
                        err_code=VectorSequenceGeneratorException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                        ex=step.exception,
                    ),
                )
            cursor = cast(Vector, step.payload)
            
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(
            VectorSet(items=tuple(sequence))
        )
        