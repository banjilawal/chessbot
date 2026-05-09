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
from err import EmptyDependencyListException, OperationListNullException, ToolkitFactoryException
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
        method = f"{self.__class__.__name__}.build_toolkit"
        
        # Handle the case that, the operation dependency list is null.
        if not hasattr(toolkit_class, "REQUIRED_OPERATIONS"):
            # Send the exception chain on failure.
            return BuildResult.failure(
                ToolkitFactoryException(
                    cls_mthd=method,
                    cls_name=toolkit_class.__name__,
                    msg=ToolkitFactoryException.MSG,
                    err_code=ToolkitFactoryException.ERR_CODE,
                    ex=OperationListNullException(
                        cls_mthd=method,
                        cls_name=toolkit_class.__name__,
                        msg=OperationListNullException.MSG,
                        err_code=OperationListNullException.ERR_CODE
                    )
                )
            )
        # Handle the case that, the toolkit does not have any operations.
        if len(toolkit_class.REQUIRED_OPERATIONS) == 0:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ToolkitFactoryException(
                    cls_mthd=method,
                    cls_name=toolkit_class.__name__,
                    msg=ToolkitFactoryException.MSG,
                    err_code=ToolkitFactoryException.ERR_CODE,
                    ex=EmptyDependencyListException(
                        cls_mthd=method,
                        cls_name=toolkit_class.__name__,
                        msg=EmptyDependencyListException.MSG,
                        err_code=EmptyDependencyListException.ERR_CODE
                    )
                )
            )
        
        resolved_dependencies = []
        for attr, requirement in toolkit_class.REQUIRED_OPERATIONS:
            # Perform resolution via registry controller
            search_result = self._registry_controller.find_worker(
                domain=requirement.DOMAIN,
                operation_name=requirement.OPERATION_NAME
            )
            # Handle the case that, the registry search does not produce a hit or encounters an error.
            if search_result.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    ToolkitFactoryException(
                        cls_mthd=method,
                        cls_name=toolkit_class.__name__,
                        msg=ToolkitFactoryException.MSG,
                        err_code=ToolkitFactoryException.ERR_CODE,
                        ex=search_result.exception
                    )
                )
            # Store resolved operations
            resolved_dependencies.append(search_result.payload[0])
        
        # Dynamically construct the toolkit, injecting its dependencies
        toolkit_instance = toolkit_class(self._registry_controller)
        for attr, dependency in resolved_dependencies:
            setattr(toolkit_instance, attr, dependency)
        
        return BuildResult.success(toolkit_instance)