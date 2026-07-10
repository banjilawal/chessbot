# src/register/entity/prisoner/blueprint/py

"""
Module: register.entity.prisoner.blueprint.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import PrisonerBlueprint
from err import PrisonerBlueprintNullException
from model import EntityRegister


class PrisonerBlueprintEntityRegister(EntityRegister[PrisonerBlueprint]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: PrisonerBlueprint
        null_exception: PrisonerBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: PrisonerBlueprint = Type[PrisonerBlueprint],
            null_exception: PrisonerBlueprintNullException = PrisonerBlueprintNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> PrisonerBlueprint:
        return cast(PrisonerBlueprint, self.model)
    
    @property
    def null_exception(self) -> PrisonerBlueprintNullException:
        return cast(PrisonerBlueprintNullException, self.null_exception)
    
    @property
    def is_prisoner_blueprint_entity_register(self) -> bool:
        return isinstance(self, PrisonerBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PrisonerBlueprintEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
