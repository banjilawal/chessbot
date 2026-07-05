# src/toolkit/model/register/square/model.py

"""
Module: toolkit.model.register.square.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import SquareRegisterNullException
from model import Square, SquareRegister
from toolkit import RegisterToolkit
from validation import SquareValidator


class SquareRegisterToolkit(RegisterToolkit[Square]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for SquareRegister tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        square_validator: SquareValidator
        null_exception: SquareRegisterNullException
        model: SquareRegister

    Provides:

    Super Class:
       RegisterToolkit
    """
    square_validator: SquareValidator = SquareValidator()
    null_exception = SquareRegisterNullException = SquareRegisterNullException()
    model: SquareRegister
    
