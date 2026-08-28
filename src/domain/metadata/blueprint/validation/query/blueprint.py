# src/domain/metadata/blueprint/blueprint.py

"""
Module: domain.metadata.blueprint.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import TypeVar

from domain.metadata.blueprint import Blueprint
from err import (
    SearchContextNullException, QueryNullException, StackEmptyException, StackNullException
)
from domain.model import Query
from collection.stack import StackService
from transit.dispatcher.validator import StackSearchContextValidator, PrimingValidator

T = TypeVar("T")

class QueryValidationBlueprint(Blueprint[T]):
    """
     Role:
        1.  Metadata
    
    Responsibilities:
        1.  Satisfy dependencies StackQueryValidator needs for determining if a candidate is
            a properly formed query.
    
    Attributes:
        query_model_type: Query
        stack_model_type: StackService
        stack_domain_null_exception: StackNullException
        query_domain_null_exception: QueryNullException
        context_domain_null_exception: ContextNullException
        empty_stack_exception: StackEmptyException
        context_validator: ContextValidator
        priming_validator: ValidatorPrimer
        
    Provides:
    
    Super Class:
    """
    query_model_type: Query[T]
    stack_model_type: StackService[T]
    stack_domain_null_exception: StackNullException
    query_domain_null_exception: QueryNullException
    context_domain_null_exception: SearchContextNullException
    empty_stack_exception: StackEmptyException
    context_validator: StackSearchContextValidator[T]
    priming_validator: PrimingValidator = PrimingValidator()