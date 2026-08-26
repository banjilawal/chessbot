# src/authorization/utility/crud/utility.py

"""
Module: authorization.utility.crud.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Dict, Generic, TypeVar

from assurance import Validator
from authorization import PermissionUtility
from domain import CrudRequest


T = TypeVar("T", bound="CrudRequest")


@dataclass
class CrudPermissionUtility(PermissionUtility[T], ABC, Generic[T]):
    """
    Role:
        -  Utility

    Responsibilities:
        1.  Bundles resources the CrudAuthorizer needs to evaluate a CrudRequest.

    Attributes:
        validator: Dict[str, ContextValidator]

    Provides:

    Super Class:
        PermissionUtility
    """
    validator: Dict[str, Validator]
    