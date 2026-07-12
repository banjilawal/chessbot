# src/suite/register/operand/suite.py

"""
Module: suite.register.operand.suite
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import PointRegister
from suite import ModelOperationSuite
from toolkit import CartesianRegisterToolkit
from validator import CartesianRegisterValidator


class CartesianRegisterSuite(ModelOperationSuite[PointRegister]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a CartesianRegister.

    Attributes:
        toolkit: CartesianRegisterToolkit
        builder: CartesianRegisterBuilder
        validator: CartesianRegisterValidator

    Provides:

    Super Class:
        Suite

    Notes:
        -   Suite for an empty class which makes managing toolkits easier.
        -   Any toolkits for a suite should be a Suite subclass.
    """
    toolkit: CartesianRegisterToolkit = CartesianRegisterToolkit()
    builder: CartesianRegisterBuilder = CartesianRegisterBuilder()
    validator: CartesianRegisterValidator = CartesianRegisterValidator()

    
