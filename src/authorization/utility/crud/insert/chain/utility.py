# src/authorization/utility/crud/insert/chain/utility.py

"""
Module: authorization.utility.crud.insert.chain.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Dict, Generic, TypeVar

from assurance import StackInsertContextValidator
from authorization import InsertPermissionUtility
from domain import ChainInsertContext

T = TypeVar("T", bound="ChainInsertContext")


@dataclass
class ChainInsertPermissionUtility(
    InsertPermissionUtility[T], ABC, Generic[T]
):
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
    