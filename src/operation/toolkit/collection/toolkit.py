# src/operation/toolkit/collection/toolkit.py

"""
Module: operation.toolkit.collection.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from assurance import PrimingValidator
from microservice import IdentityService
from operation.toolkit.collection.toolkit import Toolkit

T = TypeVar("T", bound="Collection")

class CollectionToolkit(Toolkit, ABC, Generic[T]):
    """
    Role:
        - Dependency Management

    Responsibilities:
        1.  Bundles dependencies a Collection worker needs to complete its task.
        2.  Loose Coupling between Collection workers and their resources.
        3.  Simplify Entry points.

    Attributes:
        identity_service: IdentityService
        priming_validator: PrimingValidator

    Provides:

    Super Class:
        Toolkit
    """
    model: Type[T]
    carrier_model: Type[EntityCarrier[T]]
    blueprint_model: Type[Blueprint[T]]
    
    null_exception: ModelNullException
    blueprint_null_exception: BlueprintNullException
    carrier_null_exception: EntityCarrierNullException
    def __init__(
            self,
            model: Type[T],
            carrier_model:
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(identity_service=identity_service, priming_validator=priming_validator)

