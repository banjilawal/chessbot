# src/toolkit/model/register/square/model.py

"""
Module: toolkit.model.register.square.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional

from model import Square
from toolkit import ModelToolkit
from validation import SquareValidator


class SquareRegisterToolkit(ModelToolkit):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for Path tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        square_validator: SquareValidator
        null_exception: PathNullException
        model: Path

    Provides:

    Super Class:
       ModelToolkit
    """
    square_validator: SquareValidator = SquareValidator()
    null_exception = SquareRegisterNullException = SquareRegistetNullException()
    model: SquareRegister
    
