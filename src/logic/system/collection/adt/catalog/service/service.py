# src/logic/system/collection/schema/exception/schema.py

"""
Module: logic.system.collection.schema.exception.schema
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from abc import ABC
from typing import Generic, TypeVar

from logic.system import SearchMicroservice, Validator

E = TypeVar("E", bound="Enum")


class CatalogService(ABC, Generic[E]):
    """
    Role:
        -   Data layer
        -   CRUD controller.
        -   ACID compliance.
        -   Microservice API
        -   Interface

    Responsibilities:
        1.  Preserve consistency during updates and deletes.
        2.  Stateful, scalable integrity management of objects.
        3.  Grant read access to the data-modeling objects.

    Attributes:
        id: int
        name: str
        validator: Validator[E]
        search: SearchMicroservice[E]

    Provides:

    Super class:
    """
    
    _validator: Validator[E]
    _search_service: SearchMicroservice[E]
    
    def __init__(
            self,
            id: int,
            name: str,
            validator: Validator[E],
            search_service: SearchMicroservice[E],
    ):
        super().__init__(id=id, name=name)
        self._validator = validator
        self._search_service = search_service
        
    @property
    def validator(self) -> Validator[E]:
        return self._validator
    
    
    @property
    def search_service(self) -> SearchMicroservice[E]:
        return self._search_service