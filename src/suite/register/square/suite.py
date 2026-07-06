# src/suite/register/square/suite.py

"""
Module: suite.register.square.suite
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from builder import SquareBuilder
from model import SquareRegister
from suite import ModelOperationSuite
from toolkit import SquareToolkit
from validation import SquareValidator


class SquareRegisterSuite(ModelOperationSuite[SquareRegister]):
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
    
