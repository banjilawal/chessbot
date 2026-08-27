# src/authorization/utility/crud/delete/stack/utility.py

"""
Module: authorization.utility.crud.delete.stack.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Dict, Generic, TypeVar

from assurance import StackDeleteContextValidator
from authorization import DeletePermissionUtility
from domain import StackDeleteContext

T = TypeVar("T", bound="StackDeleteContext")


@dataclass
class StackDeletePermissionUtility(DeletePermissionUtility[T], ABC, Generic[T]):
    """
    Role:
        - Utility

    Responsibilities:
        1.  Bundles resources the DeleteAuthorizer needs to evaluate a DeleteRequest.

    Attributes:
        validator: Dict[str, ContextValidator]

    Provides:

    Super Class:
        CrudPermissionUtility
    """
    validator: Dict[str, StackDeleteContextValidator[T]]
    