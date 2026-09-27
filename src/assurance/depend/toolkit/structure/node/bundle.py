# src/assurance/depend/toolkit/structure/node/toolkit.py

"""
Module: assurance.depend.toolkit.structure.node.toolkit
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

from assurance import StructureValidatorToolkit
from domain import Node

T = TypeVar("T", bound="Node")


@dataclass
class NodeValidatorToolkit(StructureValidatorToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Toolkits types, null-exceptions, attribute-validators, and utilities NodeIntegrityChecker needs to
            run safety checks on a validation candidate.

    Attributes:
        identity_service: IdentityService
        priming_validator: PrimingValidator
        types: VectorUnions
        nulls: VectorNullExceptionRoster
        number_validator: NumberValidator

    Provides:

    Super Class:
        StructureValidatorToolkit
    """