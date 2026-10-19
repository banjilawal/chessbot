# src/authorization/loader/__init__.py

"""
Module: authorization.loader.__init__
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

T = TypeVar("T")

class AuthorizationLoader(ABC, Generic[T]):
    pass