# src/toolkit/model/register/toolkit.py

"""
Module: toolkit.model.register.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from err import RegisterNullException
from model import Register
from toolkit import ModelToolkit

@dataclass
class RegisterToolkit(ModelToolkit):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Collection of workers and services that are required for Register tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        null_exception: RegisterNullException
        model: Register

    Provides:

    Super Class:
       ModelToolkit
    """
    null_exception: RegisterNullException = RegisterNullException()
    model: Register = Register
    blueprint_model = RegisterBlueprint


    