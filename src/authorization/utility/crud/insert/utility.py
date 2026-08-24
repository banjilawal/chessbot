# src/authorization/utility/crud/insert/utility.py

"""
Module: authorization.utility.crud.insert.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Dict, Generic, TypeVar

from assurance import StackInsertContextValidator
from authorization import CrudPermissionUtility
from domain import InsertContext, InsertRequest

T = TypeVar("T", bound="InsertContext")


@dataclass
class InsertPermissionUtility(CrudPermissionUtility[InsertRequest], ABC, Generic[T]):
    """
    Role:
        -   Utility

    Responsibilities:
        1.  Bundles resources the InsertAuthorizer needs to evaluate a InsertRequest.

    Attributes:
        validator: Dict[str, ContextValidator]

    Provides:

    Super Class:
        CrudPermissionUtility
    """
    validator: Dict[str, StackInsertContextValidator[T]]
    