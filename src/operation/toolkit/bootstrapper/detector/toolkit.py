# src/operation/toolkit/carrier_validator/carrier_validator/toolkit.py

"""
Module: operation.toolkit.carrier_validator.carrier_validator.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from operation.toolkit.bootstrapper.detector.toolkit import BootstrapperToolkit


class DetectorBootstrapperToolkit(BootstrapperToolkit):
    """
    Role:
        - Dependency Management

    Responsibilities:
        1.  Aggregates workers and services a bootstrapperful carrier_validator requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        DEPENDENCIES: List[Operation] = []
        SERVICE_DEPENDENCIES: List[Microservice] = []

        identity_service: IdentityService
        priming_validator: PrimingValidator
        blueprint_id_validator: BlueprintIdValidator

        _items: Dict[str, Any]

    Provides:
        - def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:
        - def _resolve_service_dependencies() -> SearchResult[List[Dict[str, Microservice]]]:
        - def _resolve_dependencies(self) -> SearchResult[List[Dict[str, Operation]]]

    Super Class:
        Toolkit

    Notes:
        -  BootstrapperToolkit for an empty class which makes managing toolkits easier.
        -  Any toolkits for a carrier_validator should be a BootstrapperToolkit subclass.
    """

