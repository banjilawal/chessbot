# src/toolkit/context/token/toolkit.py

"""
Module: toolkit.context.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import TokenContextException
from model import Token, TokenContext
from toolkit import ContextToolkit, TokenToolkit
from validation import NumberValidator


class TokenContextToolkit(ContextToolkit[Token]):
    """
    Role:
        -   Container
        -   Data Holder
        
    Responsibilities:
        1.  Collection of workers and services that are required for Board tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        DEPENDENCIES: List[Operation]
        SERVICE_DEPENDENCIES: List[Microservice]
        
        context_model_type: TokenContext
        null_context_exception: TokenContextNullException
        context_validation_primer: ValidationBootstrapper
        number_validator: NumberValidator
        
    Provides:
    
    Super Class:
        ContextToolkit
    """
    context_model_type = TokenContext
    token_toolkit: TokenToolkit = TokenToolkit()
    null_context_exception =  TokenContextException()
    number_validator: NumberValidator = NumberValidator()