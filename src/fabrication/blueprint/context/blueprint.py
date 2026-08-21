# src/blueprint/context/blueprint.py

"""
Module: blueprint.context.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.blueprint import Blueprint
from err import ContextNullException
from domain.model import Context


class ContextBlueprint(Blueprint[Context]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Provides values for instantiating a T object.
    
    Attributes:
    
    Provides:
    
    Super Class:
    """
    model_type = Context
    null_exception = ContextNullException()
    context_validator_bootstrapper: ContextValidatorBootstrapper = ContextValidatorBootstrapper()