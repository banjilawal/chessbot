# src/operand/register/entity/prisoner/blueprint/operand.py

"""
Module: operand.register.entity.prisoner.blueprint.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import PrisonerBlueprint
from err import PrisonerBlueprintNullException
from operand import EntityRegister


class PrisonerBlueprintEntityRegister(EntityRegister[PrisonerBlueprint]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: PrisonerBlueprint
        null_exception: PrisonerBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: PrisonerBlueprint = Type[PrisonerBlueprint],
            null_exception: PrisonerBlueprintNullException = PrisonerBlueprintNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> PrisonerBlueprint:
        return cast(PrisonerBlueprint, self.operand)
    
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
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
