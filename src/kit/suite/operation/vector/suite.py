# src/kit/suite/operation/carrier_validator/toolkit.py

"""
Module: kit.operation.suite.carrier_validator.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from assurance import VectorValidator
from fabrication import VectorBuilder
from kit import OperationSuite, VectorToolkit
from model import Vector


class VectorOperationSuite(OperationSuite[Vector]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a Vector.

    Attributes:
        toolkit: VectorToolkit
        builder: VectorBuilder
        validator: VectorValidator

    Provides:

    Super Class:
        Suite

    Notes:
        -   Suite for an empty class which makes managing toolkits easier.
        -   Any toolkits for a suite should be a Suite subclass.
    """
    toolkit: VectorToolkit = VectorToolkit()
    builder: VectorBuilder = VectorBuilder()
    validator: VectorValidator = VectorValidator()
   

