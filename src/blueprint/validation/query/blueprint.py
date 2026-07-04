# src/blueprint/blueprint.py

"""
Module: blueprint.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import TypeVar

from blueprint import Blueprint
from err import (
    ContextNullException, QueryNullException, StackEmptyException, StackNullException
)
from model import Query
from stack import StackService
from validation import ContextValidator, PrimingValidator

T = TypeVar("T")

class QueryValidationBlueprint(Blueprint[T]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Satisfy dependencies StackQueryValidator needs for determining if a candidate is
            a properly formed query.
    
    Attributes:
        query_model_type: Query
        stack_model_type: StackService
        stack_null_exception: StackNullException
        query_null_exception: QueryNullException
        context_null_exception: ContextNullException
        empty_stack_exception: StackEmptyException
        context_validator: ContextValidator
        priming_validator: ValidatorPrimer
        
    Provides:
    
    Super Class:
    """
    query_model_type: Query[T]
    stack_model_type: StackService[T]
    stack_null_exception: StackNullException
    query_null_exception: QueryNullException
    context_null_exception: ContextNullException
    empty_stack_exception: StackEmptyException
    context_validator: ContextValidator[T]
    priming_validator: PrimingValidator = PrimingValidator()