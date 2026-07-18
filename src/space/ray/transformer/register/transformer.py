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
from space import TargetSpanSet
from util import IdFactory


class LinearSpaceRegisterSetBuilder:
    _linear_sett: TargetSpanSet
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            linear_sett: TargetSpanSet,
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            linear_sett: LinearVectorSet,
            priming_validator: PrimingValidator            
        """
        self._linear_sett = linear_sett
        self._priming_validator = priming_validator
        
        
    def execute(self) -> BuildResult[RegisterSet]:
        method = f"{self.__class__.__name__}.execute"
        
        registers: List[VectorRegister] = []
        previous = self._linear_sett.root
        current = previous
        
        for vector in self._linear_sett.destinations.iterator:
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
        
        

        

        
        
    # def _validation(self, candidate: Any) -> ValidationResult[LinearTargetSet]:
    #     method = f"{self.__class__.__name__}"
    #     
    #     priming = self._priming_validator.execute(
    #         candidate=self._linear_sett,
    #         target_model=Type[LinearTargetSet],
    #         null_exception=NullException(),
    #     )
    #     if priming.is_failure:
    #         return ValidationResult.failure(priming.exception)
    #     linear_sett = cast(LinearTargetSet, priming.payload)
    #     
    #     if linear_sett.is_empty:
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
    #     self._linear_sett = temp