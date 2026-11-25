# src/microservice/microservice.py

"""
Module: microservice.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from abc import ABC
from typing import Generic, TypeVar

from artifcat import Result
from transit import Dispatcher

T = TypeVar("T", bound="Result")


class Microservice(ABC, Generic[T]):
    """
    Role:
        -   API
        -   Stateless Microservice
        
    About:
        Avoids casting an entity's builders and validators by making them abstract
        properties.

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the build-validation security lifecycle.

    Attributes:
        dispatcher: Dispatcher

    Provides:

    Super Class:
    """
    _dispatcher: Dispatcher
    
    def __init__(self, dispatcher: Dispatcher):
        """
        Args:
            dispatcher: Dispatcher
        """
        self._dispatcher = dispatcher
    
    @property
    def dispatcher(self) -> Dispatcher:
        return self._dispatcher