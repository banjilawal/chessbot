# src/register/entity/py

"""
Module: register.entity.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import NullException
from model import Model, Register


class EntityRegister(Register[Any]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: Model
        null_exception: NullException
            
    Provmodeles:

    Super Class:
    """
    
    def __init__(self, model: Any, null_exception: NullException,):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(a=model, b=null_exception)
        
    @property
    def model(self) -> Any:
        return cast(Any, self.a)
    
    @property
    def null_exception(self) -> NullException:
        return cast(NullException, self.null_exception)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
