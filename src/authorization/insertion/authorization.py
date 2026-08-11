# src/authorization/insertion/authorization.py

"""
Module: authorization.insertion.authorization
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from authorization import Authorization

T = TypeVar("T", bound="Collection")

class InsertionAuthorization(Authorization[InsertionRequest], ABC, Generic[T]):
