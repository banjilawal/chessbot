# src/pattern/traversal/traversal.py

"""
Module: pattern.traversal.category.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional, Tuple, Type, cast

from container import VectorSet
from err import TraversalPatternException
from err.null.recurrence.group import RecurrenceTableGroupNullException
from pattern import MovementPattern, PatternGenerator
from recurrence import RecurrenceTableGroup
from result import ComputationResult
from util import LoggingLevelRouter
from validator import PrimingValidator


class TraversalPattern(MovementPattern):
    """
    Role:
        -   Iteration


    Responsibilities:
        1.  Stepping function which gives the next vector in a series.

    Attributes:
        stepper: Stepper
        math_toolkit: Optional[MathToolkit]

    Provides:

    Super Class:
    """
    _priming_validator: PrimingValidator
    _recurrence_table_group: RecurrenceTableGroup[T]
    _pattern_generator: Optional[PatternGenerator]
    
    def __init__(
            self,
            recurrence_table_group: RecurrenceTableGroup,
            priming_validator: Optional[PrimingValidator] | None = PrimingValidator(),
            pattern_generator: Optional[PatternGenerator] | None = PatternGenerator(),
    ):
        """
        Args:
            recurrence_table_group: RecurrenceTableGroup[T]
            pattern_generator: Optional[PatternGenerator]
        """
        self._recurrence_table_group = recurrence_table_group
        self._pattern_generator = pattern_generator
        self._priming_validator = priming_validator
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @property
    def pattern_generator(self) -> PatternGenerator:
        return self._pattern_generator
        
    @property
    def recurrence_table_group(self) -> RecurrenceTableGroup[T]:
        return self._recurrence_table_group
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            recurrence_table_group: RecurrenceTableGroup[T]
    ) -> ComputationResult[Tuple[VectorSet]]:
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the recurrence_table_group is not safe to use.
        validation = self.priming_validator.execute(
            candidate=recurrence_table_group,
            target_model=Type[RecurrenceTableGroup],
            null_exception=RecurrenceTableGroupNullException(),
        )
        if validation.is_failure:
            # Send the exception chain in the result.
            return ComputationResult.failure(
                TraversalPatternException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TraversalPatternException.MSG,
                    err_code=TraversalPatternException.ERR_CODE,
                    ex=validation.exception
                )
            )
        # Cast the validation product for additional processing.
        recurrence_tables = cast(RecurrenceTableGroup, validation.payload)
        
        computation = self.pattern_generator.execute(
            recurrence_table_group=recurrence_tables
        )
        # Handle the case that the computation does not produce a result.
        if computation.is_failure:
            # Send the exception chain in the result.
            return ComputationResult.failure(
                TraversalPatternException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TraversalPatternException.MSG,
                    err_code=TraversalPatternException.ERR_CODE,
                    ex=validation.exception
                )
            )
        pattern = cast(Tuple[VectorSet], computation.payload)
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(pattern)
        
        # return self._pattern_generator.execute(recurrence_table_group=recurrence_sets)
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Get the series of targets on a line between the origin and terminus

    Attributes:
        stepper: Stepper
        math_toolkit: Optional[MathToolkit]

    Provides:
        -   def distance() -> ComputationResult[Scalar]
        -   def target_vectors() -> ComputationResult[LinearTargetSet]:

    Super Class:
       .Pattern
    """
    #
    # _stepper: Stepper
    # _math_toolkit: Optional[MathToolkit]
    #
    # def __init__(
    #         self,
    #         stepper: Stepper,
    #         math_toolkit: Optional[MathToolkit] | None = MathToolkit(),
    # ):
    #     """
    #     Args:
    #         stepper: Stepper
    #         math_toolkit: Optional[MathToolkit]
    #     """
    #     self._stepper = stepper
    #     self._math_toolkit = math_toolkit
    #
    # @property
    # def stepper(self) -> Stepper:
    #     return self._stepper
    #
    # @property
    # def math(self) -> MathToolkit:
    #     return self._math_toolkit
    #
    #
    # @abstractmethod
    # @LoggingLevelRouter.monitor
    # def next(self, vector: Vector) -> ComputationResult[Vector]:
    #     pass
    #
    #
    # @LoggingLevelRouter.monitor
    # def execute(self, endpoints: VectorRegister) -> ComputationResult[LinearTargetSet]:
    #     """
    #     Get DestinationVectors from the origin to the terminus
    #
    #     Action:
    #         1.  Send an exception chain in the ComputationResult if the stepper aborts.
    #         2.  Otherwise, send the computed vector in the success result.
    #     Args:
    #     Returns:
    #         ComputationResult[LinearVectorSet]
    #     Raises:
    #          LinearMovementException
    #     """
    #     method = f"{self.__class__.__name__}.next"
    #
    #     # --- Set up looping variables ---#
    #     cursor = endpoints.u
    #     solutions: List[Vector] = []
    #
    #     # --- Less than is not a good choice for iterating through vectors.  ---#
    #     while cursor != endpoints.v:
    #         # --- Request the next Vector for the stepper. ---#
    #         computation = self._stepper.next(cursor)
    #
    #         # Handle the case that, the computation is aborted.
    #         if computation.is_failure:
    #             # Send an exception chain in the result.
    #             return ComputationResult.failure(
    #                 TraversalPatternExceptionException(
    #                     cls_mthd=method,
    #                     cls_name=self.__class__.__name__,
    #                     msg=TraversalPatternExceptionException.MSG,
    #                     err_code=TraversalPatternExceptionException.ERR_CODE,
    #                     mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
    #                     ex=computation.exception,
    #                 ),
    #             )
    #         # --- Cast and append the curso to the list. ---#
    #         cursor = cast(Vector, computation.payload)
    #         solutions.append(cursor)
    #
    #     # Create the DestinationVector set.
    #
    # target_set = VectorSet(tuple(solutions))
    # # --- Forward the work product to the caller. ---#
    # return ComputationResult.success(
    #     LinearTargetSet(
    #         endpoints=endpoints, group=target_set
    #     )
    # )