# src/exchange/service/service.py

"""
Module: exchange.service.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import Result
from exchange import Request, Service
from util import LoggingLevelRouter

T = TypeVar("T", bound="Result")

class ResponseService(ABC, Generic[T]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract the payload from a Response.result.

    Attributes:
        service: Service[T]

    Provides:
        -   def execute(self, request[T]) -> Any

    Super Class:
    """
    _service: Service[T]
    
    def __init__(self, service: Service[T]):
        """
        Args:
            service: Service[T]
        """
        self._service = service
        
    @property
    def service(self) ->Service[T]:
        return self._service