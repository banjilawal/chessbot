# src/blueprint/container/register/blueprint.py

"""
Module: blueprint.container.register.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Tuple, Type, cast

from blueprint import ContainerBlueprint
from container import RegisterSet
from err import RegisterSetNullException
from register import Register


class RegisterSetBlueprint(ContainerBlueprint[Register]):
    """
    Role:
        -   Container
        -   DTO
        
    Responsibilities:
        1.  Provides values for instantiating a Register object.
        2.  DTO
    
    Attributes:
        entries: Tuple[Register, ...],
        container_class: Type[RegisterSet],
        null_exception: RegisterSetNullException
    
    Provides:
    
    Super Class:
        ContainerBlueprint
    """
    
    def __init__(
            self,
            entries: Tuple[Register],
            container_class: Type[RegisterSet] = RegisterSet,
            null_exception: RegisterSetNullException | None = RegisterSetNullException(),
    ):
        """
        Args:
            entries: Tuple[Register],
            container_class: Type[RegisterSet],
            null_exception: RegisterSetNullException
        """
        super().__init__(
            entries=entries,
            container_class=container_class,
            null_exception=null_exception,
        )
        
    @property
    def entries(self) -> Tuple[Register]:
        return cast(Tuple[Register], self.entries)
    
    @property
    def container_class(self) -> RegisterSet:
        return cast(RegisterSet, self.container_class)
    
    @property
    def null_exception(self) -> RegisterSetNullException:
        return cast(RegisterSetNullException, super().null_exception)
