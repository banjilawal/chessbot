# src/exchange/request/authorization/request.py

"""
Module: exchange.request.authorization.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import AuthorizableResult
from domain import Actionable, Actor
from exchange import Request

T = TypeVar("T", bound="AuthorizableResult")


class AuthorizationRequest(Request[T], Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides information an Authorizer needs to execute a client's job.

     Attributes:
        applicant: Actor
        activity: Actionable

     Provides:
     
     Super Class:
        Request
     """
    _applicant: Actor
    _activity: Actionable
    
    def __init__(self, id: int, applicant: Actor, activity: Actionable):
        """
        Args:
            id: int
            applicant: Actor
            activity: Actionable
        """
        super().__init__(id=id)
        self._applicant = applicant
        self._activity = activity
        
    @property
    def applicant(self) -> Applicant:
        return self._applicant
    
    @property
    def activity(self) -> Actionable:
        return self._activity
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AuthorizationRequest):
            return self.id == other.id
        return False