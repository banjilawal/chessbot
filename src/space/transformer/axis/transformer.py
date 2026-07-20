# src/space/ray/computer/axis/space/ray.py

"""
Module: space.ray.computer.axis.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from container import LinearTargetSet, TargetVectorSet
from err import AxisSpanTransformerException
from result import ComputationResult
from space import Axis, LinearSpanTransformer
from util import LoggingLevelRouter
from validator import AxisValidator


class AxisSpanTransformer(LinearSpanTransformer[Axis]):
    """
    Role:
        -   Transformer
        -   Integrity assurance

    Responsibilities:
        1.  Produce a TargetVectorSet from an Axis.

    Attributes:
        linear_space: Axis
        validator: AxisValidator

    Provides:
        -   def execute(self,) -> ComputationResult[TargetVectorSet]

    Super Class:
        LinearSpanTransformer
    """
    
    def __init__(
            self,
            linear_space: Axis,
            validator: AxisValidator | None = AxisValidator()
    ):
        """
        Args:
            linear_space: Axis
            validator: AxisValidator
        """
        super().__init__(linear_space=linear_space, validator=validator)
        
    @property
    def linear_space(self) -> Axis:
        return cast(Axis, self.linear_space)
    
    @property
    def validator(self) -> AxisValidator:
        return cast(AxisValidator, self.validator)
    
    @LoggingLevelRouter.monitor
    def execute(self,) -> ComputationResult[TargetVectorSet]:
        """
        Create a TargetVectorSet from a LinearSpace.

        Action:
            1.  Send an exception chain in the ComputationResult if 
                    -   The linear_space is null or the wrong type.
                    -   The linear space is empty.
                    -   linear_space.destination_vectors does not produce a solution.
            2.  Otherwise, create a SpanSVectorSet from solution's fields.
            3.  Send the SpanVecorSet in the ComputationResult.
        Args:
        Returns:
            ComputationResult[TargetVectorSet]
        Raises:
             AxisSpanTransformerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Request the linear destination set. ---#
        solution = self.linear_space.target_vectors()
        
        # Handle the case that, request is not granted.
        if solution.is_failure:
            # Send the exception chain in the result.
            return ComputationResult.failure(
                AxisSpanTransformerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisSpanTransformerException.MSG,
                    err_code=AxisSpanTransformerException.ERR_CODE,
                    mthd_rslt_type=AxisSpanTransformerException.MTHD_RSLT_TYPE,
                    ex=solution.exception,
                )
            )
        # On success extract the linear solutions.
        linear_vectors = cast(LinearTargetSet, solution.payload).remove_root_destination()
        
        # Create a spanned vector set
        span_destination_set = TargetVectorSet(
            root=linear_vectors.hunter,
            entries=linear_vectors.entries
        )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(span_destination_set)
