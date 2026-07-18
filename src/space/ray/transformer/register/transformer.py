# src/space/ray/computer/register/__init__.py

"""
Module: space.ray.computer.register.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from bootstrapper import PrimingValidator
from container import RegisterSet
from register import VectorRegister
from result import BuildResult
from space import LinearDestinationSet
from util import IdFactory


class LinearSpaceRegisterSetBuilder:
    _destination_set: LinearDestinationSet
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            destination_set: LinearDestinationSet,
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            destination_set: LinearVectorSet,
            priming_validator: PrimingValidator            
        """
        self._destination_set = destination_set
        self._priming_validator = priming_validator
        
        
    def execute(self) -> BuildResult[RegisterSet]:
        method = f"{self.__class__.__name__}.execute"
        
        registers: List[VectorRegister] = []
        previous = self._destination_set.root
        current = previous
        
        for vector in self._destination_set.destinations:
            current = vector
            register = VectorRegister(
                id=IdFactory.next_id(class_name="VectorRegister"),
                u=previous,
                v=current,
            )
            registers.append(register)
            previous = current
        return BuildResult.success(
            RegisterSet(tuple(registers))
        )
        
        

        

        
        
    # def _validation(self, candidate: Any) -> ValidationResult[LinearDestinationSet]:
    #     method = f"{self.__class__.__name__}"
    #     
    #     priming = self._priming_validator.execute(
    #         candidate=self._destination_set,
    #         target_model=Type[LinearDestinationSet],
    #         null_exception=NullException(),
    #     )
    #     if priming.is_failure:
    #         return ValidationResult.failure(priming.exception)
    #     destination_set = cast(LinearDestinationSet, priming.payload)
    #     
    #     if destination_set.is_empty:
    #         return BuildResult.failure(
    #             LinearSpaceRegisterBuilderException(
    #                 cls_mthd=method,
    #                 cls_name=self.__class__.__name__,
    #                 msg=LinearSpaceRegisterBuilderException.MSG,
    #                 err_code=LinearSpaceRegisterBuilderException.ERR_CODE,
    #                 mthd_rslt_type=MethodResultType.BUILD_RESULT,
    #                 ex=EmptyLinearVectorSetException(
    #                     cls_mthd=method,
    #                     cls_name=self.__class__.__name__,
    #                     msg=EmptyLinearVectorSetException.MSG,
    #                     err_code=EmptyLinearVectorSetException.ERR_CODE,
    #                 )
    #             )
    #         )
    #     self._destination_set = temp