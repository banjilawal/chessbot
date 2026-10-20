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

from artifcat import Result
from domain import Applicant, Permittable
from exchange import Request

T = TypeVar("T", bound="Result")


class AuthorizationRequest(Request[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about a job.

     Attributes:
        applicant: Applicant
        permit: Permittable

     Provides:
     
     Super Class:
        Request
     """
    _applicant: Applicant
    _permit: Permittable
    
    def __init__(self, id: int, applicant: Applicant, permit: Permittable):
        """
        Args:
            id: int
            applicant: Applicant
            permit: Permittable
        """
        super().__init__(id=id)
        self._applicant = applicant
        self._permit = permit
        
    @property
    def applicant(self) -> Applicant:
        return self._applicant
    
    @property
    def permit(self) -> Permittable:
        return self._permit
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AuthorizationRequest):
            return self.id == other.id
        return False