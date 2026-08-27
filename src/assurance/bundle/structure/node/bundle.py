# src/assurance/bundle/structure/node/bundle.py

"""
Module: assurance.bundle.structure.node.bundle
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

from assurance import StructureValidationBundle
from domain import Node

T = TypeVar("T", bound="Node")


@dataclass
class NodeValidationBundle(StructureValidationBundle[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles types, null-exceptions, attribute-validators, and utilities NodeIntegrityChecker needs to
            run safety checks on a validation candidate.

    Attributes:
        identity_service: IdentityService
        priming_validator: PrimingValidator
        types: VectorUnions
        nulls: VectorNullExceptionRoster
        number_validator: NumberValidator

    Provides:

    Super Class:
        StructureValidationBundle
    """