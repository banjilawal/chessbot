# src/blueprint/validation/token/blueprint.py

"""
Module: blueprint.validation.query.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from model import Token, TokenQuery
from stack import TokenStackService
from validator import TokenContextValidator
from blueprint import QueryValidationBlueprint
from err import (
    TokenContextNullException, TokenQueryNullException, TokenStackEmptyException, TokenStackNullException
)



@dataclass
class TokenQueryValidationBlueprint(QueryValidationBlueprint[Token]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a TokenValidation instance.

    Attributes:
        query_model_type: TokenQuery
        stack_model_type: TokenStackService
        stack_null_exception: TokenStackNullException
        query_null_exception: TokenQueryNullException
        empty_stack_exception: TokenStackEmptyException
        context_null_exception: TokenContextNullException
        context_validator: TokenContextValidator
        priming_validator: ValidatorPrimer

    Provides:

    Super Class:
        QueryValidationBlueprint
    """
    query_model_type = TokenQuery
    stack_model_type = TokenStackService
    query_null_exception = TokenQueryNullException()
    stack_null_exception = TokenStackNullException()
    empty_stack_exception = TokenStackEmptyException()
    context_null_exception = TokenContextNullException()
    context_validator = TokenContextValidator()


