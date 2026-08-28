# src/domain/metadata/blueprint/structure/toggle/cartesian/blueprint.py

"""
Module: domain.metadata.blueprint.structure.toggle.cartesian.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain import CartesianPoint, CartesianBlueprint, CartesianToggle, ToggleBlueprint
from err import CartesianToggleNullException

@dataclass
class CartesianToggleBlueprint(ToggleBlueprint[CartesianPoint]):
    """
     Role:
        1.  Metadata
    
    Responsibilities:
        1.  Provides values for hydrating a CartesianToggle.
    
    Attributes:
        domain_class: Type[CartesianToggle]
        payload_blueprint: Type[CartesianPointBlueprint]
        domain_null_exception: CartesianToggleNullException
    
    Provides:
    
    Super Class:
        ToggleBlueprint
    """
    domain_class: Type[CartesianToggle] = CartesianToggle
    payload_blueprint: Type[CartesianBlueprint] = CartesianBlueprint
    domain_null_exception: CartesianToggleNullException = CartesianToggleNullException()


    
    
    

