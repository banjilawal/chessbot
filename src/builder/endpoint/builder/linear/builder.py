# src/space/builder/linear/__init__.py

"""
Module: space.builder.linear.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional, Type, cast

from bootstrapper import PrimingValidator
from container import RegisterSet
from err import LinearTargetSetNullException
from register import VectorRegister
from result import BuildResult, MethodResultType

from space import LinearTargetSet, SpacepanSet, RegisterBuilder
from util import IdFactory, LoggingLevelRouter


class RegisterSetLinearBuilder(RegisterBuilder[LinearTargetSet]):
    _space: LinearTargetSet
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            space: LinearTargetSet,
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            priming_validator: PrimingValidator            
        """
        self._space = space
        self._priming_validator = priming_validator        
        
    @property
    def space(self) -> LinearTargetSet:
        return cast(LinearTargetSet, self.space)
    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[RegisterSet]:
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the space are not safe to use.
        validation = self._priming_validator.execute(
            candidate=self._space,
            target_model=Type[LinearTargetSet],
            null_exception=LinearTargetSetNullException(),
        )
        if validation.is_failure:
            # Send the exception chain in the result.
            return BuildResult.failure(
                RegisterSetLinearBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RegisterSetLinearBuilderException.MSG,
                    err_code=RegisterSetLinearBuilderException.ERR_CODE,
                    mthd_rslt=MethodResultType.BUILD_RESULT,
                    ex=validation.exception,
                )
            )
        
        registers: List[VectorRegister] = []
        previous = self.space.root
        
        for target in self._space.space.iterator
            current = target
            register = VectorRegister(
                id=IdFactory.next_id("VectorRegister"), 
                u=previous, 
                v=current
            )
            registers.append(register)
            previous = current
        
        BuildResult.success(RegisterSet(tuple(registers)))
