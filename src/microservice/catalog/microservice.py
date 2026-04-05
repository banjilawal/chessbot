# src/logic/system/collection/schema/exception/schema.py

"""
Module: logic.system.collection.schema.exception.schema
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar


E = TypeVar("E", bound="Enum")


class CatalogService(ABC, Generic[E]):
    """
    Role:
        -   Data layer
        -   Microservice API
        -   Interface

    Responsibilities:
        1.  Extracts, manipulates consults unique invariant tuples which
            determine fixed properties and roles of stateless data-holders.

    Attributes:
        id: int
        name: str
        validator: Validator[E]
        search: SearchMicroservice[E]

    Provides:

    Super class:
        Microservice
    """
    
    def __init__(
            self,
            id: int,
            name: str,
    ):
        super().__init__(id=id, name=name)
   
    @property
    @abstractmethod
    def validator(self) -> Validator[E]:
        pass
    
    
    @property
    @abstractmethod
    def search_service(self) -> SearchMicroservice[E]:
        pass