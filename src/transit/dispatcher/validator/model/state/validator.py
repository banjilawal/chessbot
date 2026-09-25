# src/transit/dispatcher/validator/model/vector/validator.py

"""
Module: transit.dispatcher.validator.model.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from assurance import ModelValidator


class StateModelValidator(ModelValidator, ABC):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Vector instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: VectorValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
