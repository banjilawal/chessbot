# src/microservice/microservice.py

"""
Module: microservice.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from abc import ABC
from typing import Generic, Optional, TypeVar

from transit.controller import Controller

T = TypeVar("T", bound="StateModel")


class Microservice(ABC, Generic[T]):
    """
    Role:
        -   API
        -   Lifecycle Manager
        -   Operations Provider
        -   Stateless Microservice
        
    About:
        Avoids casting an entity's builders and validators by making them abstract
        properties.

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the build-validation security lifecycle.

    Attributes:
        id: int
        controller: Controller[T]
        name: Optional[str]

    Provides:

    Super Class:
    """
    NAME = "microservice"
    _id: int
    _name: str
    _controller: Controller[T]
    
    def __init__(
            self,
            id: int,
            controller: Controller[T],
            name: Optional[str] | None = None,
    ):
        """
        Args:
            id: int
            controller: Controller[T]
            name: Optional[str]
        """
        self._id = id
        self._name = name or self.NAME
        self._controller = controller
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def controller(self) -> Controller[T]:
        return self._controller

    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, Microservice):
                return True
        return False

    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return f"id:{self._id}, name:{self._name}"
