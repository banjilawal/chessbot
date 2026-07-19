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

from space import TargetVectorSet, TargetSpanSet, RegisterBuilder
from util import IdFactory, LoggingLevelRouter


class RegisterSetSpanBuilder(RegisterBuilder[TargetS]):

    
    def __init__(
            self,
            points: TargetVectorSet,
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            points: TargetVectorSet,
            priming_validator: PrimingValidator            
        """
        super().__init__(points=points, priming_validator=priming_validator)
        
    @property
    def points(self) -> TargetSpanSet:
        return cast(TargetSpanSet, self.points)
    
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[RegisterSet]:
        method = f"{self.__class__.__name__}.execute"
        
        registers: List[RegisterSet] = []
        for point in self.points.destinations.iterator:
    
            register = VectorRegister(
                id=IdFactory.next_id(class_name="VectorRegister"),
                u=self.points.root,
                v=point
            )
            registers.append(register)
        BuildResult.success(
            RegisterSet(tuple(registers))
        )
        return BuildResult.success(
            RegisterSet(tuple(registers))
        )
