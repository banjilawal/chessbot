# src/blueprint/space/blueprint.py

"""
Module: blueprint.space.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, Optional, Type, TypeVar, cast

from blueprint import SpaceBlueprint
from err import LinearSpaceNullException, VectorRegisterException
from register import VectorRegister
from space import LinearStepper

T = TypeVar("T", bound="Linear")

class LinearBlueprint(SpaceBlueprint, Generic[T]):
    """
     Role:
         -   Space
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a Space object
         2.  DTO

     Attributes:
        endpoints: VectorRegister,
        stepper: LinearStepper,
        null_exception: Optional[LinearSpaceNullException]
         
     Provides:

     Super Class:
        SpaceBlueprint
     """
    _endpoints: VectorRegister
    _stepper: LinearStepper
    
    def __init__(
            self,
            model_class: Type[T],
            endpoints: VectorRegister,
            stepper: LinearStepper,
            null_exception: Optional[LinearSpaceNullException] |
                            None = LinearSpaceNullException(),
    ):
        """
        Args:
            model_class: Type[T],
            endpoints: VectorRegister,
            stepper: LinearStepper,
            null_exception: Optional[LinearSpaceNullException]
        """
        super().__init__(model_class=model_class, null_exception=null_exception,)
        self._endpoints = endpoints
        stepper._stepper = stepper
        
    @property
    def endpoints(self) -> VectorRegister:
        return self._endpoints
    
    @property
    def stepper(self) -> LinearStepper:
        return self.stepper
    
    @property
    def model_class(self) -> Type[T]:
        return cast(Type[T], self.model_class)
    
    @property
    def null_exception(self) -> LinearSpaceNullException:
        return cast(LinearSpaceNullException, self._null_exception)