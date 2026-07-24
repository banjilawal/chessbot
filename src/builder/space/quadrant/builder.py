# src/builder/space/quadrant/builder.py

"""
Module: builder.space.quadrant.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from builder import SpaceBuilder
from model import Vector
from result import BuildResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="QuadrantSpace")


class QuadrantSpaceBuilder(SpaceBuilder, Generic[T]):

    
    def __init__(self,):
        super().__init__()
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, origin: Vector) -> BuildResult[T]:
        pass