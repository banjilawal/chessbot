# src/authorization/utility/crud/search/stack/utility.py

"""
Module: authorization.utility.crud.search.stack.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Dict, Generic, TypeVar

from assurance import StackSearchContextValidator
from authorization import SearchPermissionUtility
from domain import ModelSearchContext

T = TypeVar("T", bound="ModelSearchContext")


@dataclass
class StackSearchPermissionUtility(SearchPermissionUtility[T], ABC, Generic[T]):
    """
    Role:
        -  Utility

    Responsibilities:
        1.  Bundles resources the SearchAuthorizer needs to evaluate a SearchRequest.

    Attributes:
        validator: Dict[str, ContextValidator]

    Provides:

    Super Class:
        CrudPermissionUtility
    """
    validator: Dict[str, StackSearchContextValidator[T]]
    