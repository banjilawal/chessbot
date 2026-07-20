# src/space/builder/linear/__init__.py

"""
Module: space.builder.linear.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, cast

from bootstrapper import PrimingValidator
from container import RegisterSet
from register import VectorRegister
from result import BuildResult

from space import TargetSpanSet, RegisterBuilder
from util import IdFactory, LoggingLevelRouter


class RegisterSetLinearBuilder(RegisterBuilder[TargetSpanSet]):

    
    def __init__(
            self,
            points: TargetSpanSet,
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            points: LinearTargetSet,
            priming_validator: PrimingValidator            
        """
        super().__init__(points=points, priming_validator=priming_validator)
        
    @property
    def points(self) -> TargetSpanSet:
        return cast(TargetSpanSet, self.points)
    
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[RegisterSet]:
        method = f"{self.__class__.__name__}.execute"
        
        registers: List[VectorRegister] = []
        previous = self.points.root
        
        for point in self.points.destinations.iterator:
            current = point
            register = VectorRegister(
                id=IdFactory.next_id(class_name="VectorRegister"),
                u=previous,
                v=current
            )
            registers.append(register)
            previous = current
        BuildResult.success(
            RegisterSet(tuple(registers))
        )
