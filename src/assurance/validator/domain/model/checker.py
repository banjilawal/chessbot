# src/assurance/validator/domain/model/checker.py

"""
Module: assurance.validator.domain.model.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from assurance import Validator
from domain import DataModel


T = TypeVar("T", bound="DataModel")


class ModelValidator(Validator, ABC, Generic[T]):
    """
    Role
        -   Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null EntityCarrier.
        2.  Run safety checks on models and blueprints inside an EntityCarrier's payload.

    Attributes:
        bundle: ModelValidationBundle[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[Blueprint[T]|T]:

    Super Class:
        IntegrityChecker
    """
    
    
