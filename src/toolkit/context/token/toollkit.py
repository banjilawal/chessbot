# src/toolkit/context/token/toolkit.py

"""
Module: toolkit.context.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import TokenContextNullException
from model import Token, TokenContext
from toolkit import ContextToolkit, TokenToolkit
from validation import NumberValidator


class TokenContextToolkit(ContextToolkit[Token]):
    """
    Role:
        -   Container
        -   Data Holder
        
    Responsibilities:
        1.  Aggregates workers and services required for TokenContext build and validation tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        DEPENDENCIES: List[Operation]
        SERVICE_DEPENDENCIES: List[Microservice]
        
        context_model_type: TokenContext
        null_context_exception: TokenContextNullException
        context_priming_validator: PrimingValidator
        number_validator: NumberValidator
        
    Provides:
    
    Super Class:
        ContextToolkit
    """
    context_model_type = TokenContext
    token_toolkit: TokenToolkit = TokenToolkit()
    null_context_exception =  TokenContextNullException()
    number_validator: NumberValidator = NumberValidator()