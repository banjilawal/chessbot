# src/factory/toolkit/factory.py

"""
Module: factory.toolkit.factory
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import List, Type

from controller import WorkerRegistryController
from operation import Operation
from result import BuildResult
from toolkit import Toolkit


class ToolkitFactory:
    """
    Toolkit for constructing toolkits based on defined schemas.
    """
    
    def __init__(self, registry_controller: WorkerRegistryController):
        self._registry_controller = registry_controller
    
    def build_toolkit(self, toolkit_class: Type[Toolkit]) -> BuildResult[Toolkit]:
        """
        Construct a toolkit by fetching its required operations based on its SCHEMA.

        Args:
            toolkit_class: The toolkit class to instantiate (e.g., SquareToolkit).

        Returns:
            BuildResult containing the instantiated toolkit or a failure reason.
        """
        if not hasattr(toolkit_class, "REQUIRED_OPERATIONS"):
            return BuildResult.failure(f"Toolkit {toolkit_class} has no defined SCHEMA.")
        
        required_operations: List[Operation]= toolkit_class.REQUIRED_OPERATIONS
        required_services: List[Type[Operation]] = toolkit_class.REQUIRED_SERVICES
        
        resolved_dependencies = []
        for attr, operation in required_operations:
            # Perform resolution via registry controller
            search_result = self._registry_controller.find_worker(
                domain=operation.DOMAIN,
                operation_name=operation.OPERATION_NAME
            )
            if search_result.is_failure:
                return BuildResult.failure(
                    f"Failed to resolve operation '{operation_name}' for toolkit '{toolkit_class.__name__}'.",
                    exception=search_result.exception
                )
            
            # Store resolved operations
            resolved_dependencies.append(search_result.payload[0])
        
        # Dynamically construct the toolkit, injecting its dependencies
        toolkit_instance = toolkit_class(self._registry_controller)
        for attr, dependency in resolved_dependencies:
            setattr(toolkit_instance, attr, dependency)
        
        return BuildResult.success(toolkit_instance)