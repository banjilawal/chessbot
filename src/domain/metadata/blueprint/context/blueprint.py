# src/domain/metadata/blueprint/context/blueprint.py

"""
Module: domain.metadata.blueprint.context.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import Blueprint, SearchContext
from err import SearchContextNullException



class ContextBlueprint(Blueprint[SearchContext]):
    """
     Role:
        1.  Metadata
    
    Responsibilities:
        1.  Provides values for hydrating a T object.
    
    Attributes:
    
    Provides:
    
    Super Class:
    """
    model_type = SearchContext
    domain_null_exception = SearchContextNullException()
    context_validator_bootstrapper: ContextValidatorBootstrapper = ContextValidatorBootstrapper()