# src/builder/container/register/span/builder.py

"""
Module: builder.container.register.span.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, cast

from bootstrapper import PrimingValidator
from builder import RegisterBuilder
from container import RegisterSet
from model import TargetSpanSet
from register import VectorRegister
from result import BuildResult


from util import IdFactory, LoggingLevelRouter


class RegisterSetSpanBuilder(RegisterBuilder[TargetSpanSet]):

    
    def __init__(
            self,
            target: TargetSpanSet,
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            target: TargetVectorSet,
            priming_validator: PrimingValidator            
        """
        super().__init__(target=target, priming_validator=priming_validator)
        
    @property
    def target(self) -> TargetSpanSet:
        return cast(TargetSpanSet, self.target)
    
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[RegisterSet]:
        method = f"{self.__class__.__name__}.execute"
        
        registers: List[RegisterSet] = []
        for point in self.target.group.iterator:
    
            register = VectorRegister(
                id=IdFactory.next_id(class_name="VectorRegister"),
                u=self.target.hunter,
                v=point
            )
            registers.append(register)
        BuildResult.success(
            RegisterSet(tuple(registers))
        )
        return BuildResult.success(
            RegisterSet(tuple(registers))
        )
