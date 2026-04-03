# src/logic/vector/validator.py

"""
Module: logic.vector.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations

from typing import List

from logic.system import ComputationResult, LoggingLevelRouter, NumberValidator
from logic.system.worker import Worker
from logic.vector import Vector, VectorService


class VectorAdder(Worker):
    """
    Role:
        -   Worker
        -   Computation

    Responsibilities:
        1.  Add up a series of vectors.

    Attributes:

    Properties:
        -   def work(
                    vectors: List[Vector],
                    vector_service: VectorService = VectorService(),
                    number_validator: NumberValidator = NumberValidator(),
            ) -> ComputationResult[Vector]

    Super Class:
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def work(
            cls,
            vectors: List[Vector],
            vector_service: VectorService = VectorService(),
            number_validator: NumberValidator = NumberValidator(),
    ) -> ComputationResult[Vector]:
        """
        Add up a series of vectors.
        
        Action:
            1.  Send and exception in the ComputationResult any of these
                conditions occur.
                    -   The list ois null.
                    -   The list is empty.
                    -   Any of the members is flagged unsafe.
                    -   Build a new vector fails.
            2.  Otherwise, the destination vector is computed.
            3.  Send the success result.
        Args:
            vectors: List[Vector],
            vector_service: VectorService = VectorService(),
            number_validator: NumberValidator = NumberValidator(),
        Returns:
            ComputationResult[Vector]
        Raises:
            TypeError
            VectorAdditionException
            NullVectorListException
            EmptyVectorListAdditionException
        """
        method = f"{cls.__name__}.work"
        
        # Handle the case that, the list does not exist.
        if vectors is None:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorAdditionException(
                    mthd=method,
                    title=cls.__name__,
                    op=VectorAdditionException.OP,
                    msg=VectorAdditionException.MSG,
                    err_code=VectorAdditionException.ERR_CODE,
                    rslt_type=VectorAdditionException.RSLT_TYPE,
                    ex=NullVectorListException(
                        msg=VectorAdditionException.MSG,
                        err_code=VectorAdditionException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the list is empty
        if len(vectors) == 0:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorAdditionException(
                    mthd=method,
                    title=cls.__name__,
                    op=VectorAdditionException.OP,
                    msg=VectorAdditionException.MSG,
                    err_code=VectorAdditionException.ERR_CODE,
                    rslt_type=VectorAdditionException.RSLT_TYPE,
                    ex=EmptyVectorListAdditionException(
                        msg=EmptyVectorListAdditionException.MSG,
                        err_code=EmptyVectorListAdditionException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, one of the vectors is not safe to use.
        for vector in vectors:
            validation_result = vector_service.validate(candidate=vector)
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    VectorAdditionException(
                        mthd=method,
                        title=cls.__name__,
                        op=VectorAdditionException.OP,
                        msg=VectorAdditionException.MSG,
                        err_code=VectorAdditionException.ERR_CODE,
                        rslt_type=VectorAdditionException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
        # --- Create the return target ---#
        vector = Vector(x=0, y=0)
        
        for delta in vectors:
            summation_result = vector_service.builder.build(
                x=vector.x + delta.x,
                y=vector.y + delta.y,
                number_validator=number_validator,
            )
            # Handle the case that, the summation is cancelled.
            if summation_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    VectorAdditionException(
                        mthd=method,
                        title=cls.__name__,
                        op=VectorAdditionException.OP,
                        msg=VectorAdditionException.MSG,
                        err_code=VectorAdditionException.ERR_CODE,
                        rslt_type=VectorAdditionException.RSLT_TYPE,
                        ex=summation_result.exception
                    )
                )
            # --- Update the current vector. ---#
            vector = summation_result.payload
        
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(vector)

    