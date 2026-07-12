# src/validator/carrier/__init__.py

"""
Module: validator.carrier.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar
from xml.dom.minidom import Entity

from carrier import EntityCarrier
from primary import RootCertifier
from result import ValidationResult
from toolkit import ModelToolkit, Toolkit
from validator import Validator

T = TypeVar("T", bound="Model")


class CarrierValidator(Validator, Generic[EntityCarrier[T]]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Model instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: ModelToolkit[T]
        
    Provides:
        -   execute(self, candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    _root_certifier: RootCertifier[T]
    _toolkit: ModelToolkit[T]
    
    def __init__(
            self, 
            toolkit: ModelToolkit[T],
            root_certifier: RootCertifier[T],
    ):
        self._toolkit = toolkit
        self._root_certifier = root_certifier
        
    @property
    def toolkit(self) -> ModelToolkit[T]:
        return self._toolkit

    @property
    def root_certifier(self) -> RootCertifier[T]:
        return self._root_certifier
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult:
        pass
    
    
        
        
