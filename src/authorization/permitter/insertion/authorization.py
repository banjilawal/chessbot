# src/authorization/insertion/authorization.py

"""
Module: authorization.insertion.authorization
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from authorization import RequestAdjudicator, RequestAuthorizer
from request import InsertionRequest

T = TypeVar("T", bound="Collection")

class InsertionPermitter(RequestAuthorizer[InsertionRequest], ABC, Generic[T]):
    
    _adjudicator: RequestAdjudicator[T]
