# src/kit/suite/operation/register/square/suite.py

"""
Module: kit.operation.suite.register.square.suite
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from fabrication.builder import SquareBuilder
from model import SquareRegister
from kit.operation.suite import Suite
from kit.toolkit import SquareToolkit
from assurance.validator import SquareValidator


class SquareRegisterSuite(Suite[SquareRegister]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a SquareRegister.

    Attributes:
        toolkit: SquareRegisterToolkit
        builder: SquareRegisterBuilder
        validator: SquareRegisterValidator

    Provides:

    Super Class:
        Suite

    Notes:
        -   Suite for an empty class which makes managing toolkits easier.
        -   Any toolkits for a suite should be a Suite subclass.
    """
    toolkit: SquareToolkit = SquareToolkit()
    builder: SquareBuilder = SquareBuilder()
    validator: SquareValidator = SquareValidator()
    
