# src/builder/container/register/linear/builder.py

"""
Module: builder.container.register.linear.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, cast



from bootstrapper import PrimingValidator
from builder import RegisterBuilder
from container import RegisterSet
from model import LinearTargetSet
from register import VectorRegister
from result import BuildResult
from util import IdFactory, LoggingLevelRouter


class RegisterSetLinearBuilder(RegisterBuilder[LinearTargetSet]):

    
    def __init__(
            self,
            points: LinearTargetSet,
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            points: LinearTargetSet,
            priming_validator: PrimingValidator            
        """
        super().__init__(points=points, priming_validator=priming_validator)
        
    @property
    def points(self) -> LinearTargetSet:
        return cast(LinearTargetSet, self.points)
    
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[RegisterSet]:
        method = f"{self.__class__.__name__}.execute"
        
        registers: List[VectorRegister] = []
        previous = self.points.hunter
        
        for point in self.points.group.iterator:
            current = point
            register = VectorRegister(
                id=IdFactory.next_id(class_name="VectorRegister"),
                u=previous,
                v=current
            )
            registers.append(register)
            previous = current
        return BuildResult.success(
            RegisterSet(tuple(registers))
        )
