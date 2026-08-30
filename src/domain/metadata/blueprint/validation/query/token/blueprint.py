# src/domain/metadata/blueprint/validation/token/blueprint.py

"""
Module: domain.metadata.blueprint.validation.query.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.model import Token, TokenQuery
from collection.stack import TokenStackService
from transit.dispatcher.validator import TokenContextValidator
from domain.metadata.blueprint import QueryValidationBlueprint
from err import (
    TokenContextNullException, TokenQueryNullException, TokenStackEmptyException, TokenStackNullException
)



@dataclass
class TokenQueryValidationBlueprint(QueryValidationBlueprint[Token]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a TokenValidation instance.

    Attributes:
        query_model_type: TokenQuery
        stack_model_type: TokenStackService
        stack_domain_null_exception: TokenStackNullException
        query_domain_null_exception: TokenQueryNullException
        empty_stack_exception: TokenStackEmptyException
        context_domain_null_exception: TokenContextNullException
        context_validator: TokenContextValidator
        priming_validator: ValidatorPrimer

    Provides:

    Super Class:
        QueryValidationBlueprint
    """
    query_model_type = TokenQuery
    stack_model_type = TokenStackService
    query_domain_null_exception = TokenQueryNullException()
    stack_domain_null_exception = TokenStackNullException()
    empty_stack_exception = TokenStackEmptyException()
    context_domain_null_exception = TokenContextNullException()
    context_validator = TokenContextValidator()


