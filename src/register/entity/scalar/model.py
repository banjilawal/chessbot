# src/register/entity/py

"""
Module: register.entity.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import ScalarNullException
from model import EntityRegister, Scalar


class ScalarEntityRegister(EntityRegister[Scalar]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: Scalar
        null_exception: ScalarNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: Scalar = Type[Scalar],
            null_exception: ScalarNullException = ScalarNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> Scalar:
        return cast(Scalar, self.a)
    
    @property
    def null_exception(self) -> ScalarNullException:
        return cast(ScalarNullException, self.null_exception)
    
    @property
    def scalar(self) -> Scalar:
        return self.model
    
    @property
    def is_scalar_entity_register(self) -> bool:
        return isinstance(self, ScalarEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ScalarEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
