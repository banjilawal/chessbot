# src/builder/container/register/builder.py

"""
Module: builder.container.register.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, TypeVar

from builder import ContainerBuilder
from container import RegisterSet
from model import TargetVectorSet
from register import VectorRegister
from result import BuildResult
from util import IdFactory, LoggingLevelRouter

T = TypeVar("T", bound="Register")

class RegisterSetBuilder(ContainerBuilder[RegisterSet]):
    
    _target_vector_set: TargetVectorSet
    # _validator: TargetSetValidator
    
    def __init__(
            self,
            target_vector_set: TargetVectorSet,
            # target_set_validator: TargetSetValidator | None = TargetSetValidator(),
    ):
        super().__init__()
        self._target_vector_set = target_vector_set
    #     self._target_set_validator = target_set_validator
    #
    # @property
    # def target_set_validator(self) -> TargetSetValidator[T]:
    #     return self._target_set_validator

    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[RegisterSet]:
        method = f"{self.__class__.__name__}.execute"
        
        # # Handle the case that, the target_vector_set is not safe to use.
        # validation = target_set_validator.execute(self._target_vector_set)
        # if validation.is_failure:
        #     return BuildResult.failure(
        #         RegisterSetBuilderException(
        #             cls_mthd=method,
        #             cls_name=self.__class__.__name__,
        #             msg=RegisterSetBuilderException.MSG,
        #             err_code=RegisterSetBuilderException.ERR_CODE,
        #             ex=certification.exception,
        #         )
        #
        #     )
        # targets = cast(TargetVectorSet, validation.payload)
        
        registers: List[VectorRegister] = []
        previous = self._target_vector_set.hunter
        
        for target in self._target_vector_set.group.iterator:
            current = target
            register = VectorRegister(
                id=IdFactory.next_id(class_name="VectorRegister"),
                u=previous,
                v=current
            )
            registers.append(register)
            previous = current

        return BuildResult.success(
            RegisterSet(items=tuple(registers))
        )