# src/authorization/utility/utility.py

"""
Module: authorization.utility.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Dict, Generic, TypeVar

from assurance import Validator
from domain import Request

T = TypeVar("T", bound="Request")


@dataclass
class PermissionUtility(ABC, Generic[T]):
    validators: Dict[str, Validator]
    