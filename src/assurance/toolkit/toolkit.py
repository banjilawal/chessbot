# src/assurance/toolkit/toolkit.py

"""
Module: assurance.toolkit.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from assurance import AttributeHelperTable, CommonValidatorToolkit, NumberValidator, PrimingValidator
from authorization import BlueprintIdExtractor
from domain import NullExceptionGroup, ObjectManifest, TypeUnion
from microservice import IdentityService

T = TypeVar("T")


class ValidatorToolkit(ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Toolkits types, null-exceptions, attribute-validators, and utilities IntegrityChecker
            needs to run safety checks on a validation candidate.

    Attributes:
        metadata: ObjectManifest[T]
        helper: AttributeHelperTable[T]
        common: CommonValidatorToolkit

    Provides:

    Super Class:
    """
    _metadata: ObjectManifest[T]
    _helper: AttributeHelperTable[T]
    _common: CommonValidatorToolkit
    
    def __init__(
            self,
            helper: AttributeHelperTable[T],
            metadata: ObjectManifest[T],
            common: Optional[CommonValidatorToolkit] | None = None,
    ):
        """
        Args:
            helper: HelperTable[T]
            metadata: ObjectManifest[T]
            common: Optional[CommonValidatorToolkit]
        """
        self._helper = helper
        self._metadata = metadata
        self._common = common or CommonValidatorToolkit()
    
    @property
    def helper(self) -> AttributeHelperTable[T]:
        return self._helper
    
    @property
    def nulls(self) -> NullExceptionGroup[T]:
        return self._metadata.nulls
    
    @property
    def types(self) -> TypeUnion[T]:
        return self._metadata.types
    
    @property
    def metadata(self) -> ObjectManifest[T]:
        return self._metadata
    
    @property
    def identity_service(self) -> IdentityService:
        return self._common.identity_service
    
    @property
    def number_validator(self) -> NumberValidator:
        return self._common.number_validator
    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._common.priming_validator
    
    @property
    def blueprint_id_extractor(self) -> BlueprintIdExtractor:
        return self._common.blueprint_id_extractor