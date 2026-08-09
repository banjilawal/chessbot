# src/topology/generator/math.py

"""
Module: topology.generator.math
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional, cast

from collection import VectorSet
from model import Vector
from topology.recurrence import Recurrence
from result import ComputationResult

from kit.toolkit import MathToolkit
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
        -   def execute(specification: Recurrence) -> ComputationResult[VectorSet]
        
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
    def execute(self, recurrence: Recurrence) -> ComputationResult[VectorSet]:
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
            recurrence: Recurrence
        Returns:
            ComputationResult[VectorSet]
        Raises:
             AxisMappingException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the sequence gets flagged,
        validation = self._math.priming_validator.execute(
            candidate=recurrence,
            target_model=Recurrence,
            null_exception=RecurrenceNullException(),
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
        recur  = cast(Recurrence, validation.payload)
        sequence: List[Vector] = []
        cursor = recur.space.origin
        
        while cursor != recur.space.terminus:
            sequence.append(cursor)
            
            # Request that the update for the cursor.
            step = recur.space_mapping_function.next(cursor)
            
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
        