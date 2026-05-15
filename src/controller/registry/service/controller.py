# src/controller/registry/service/controller.py

"""
Module: controller.registry.service.controller
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import List

from controller import Controller
from model import ServiceRegistry
from toolkit import ServiceRegistryToolkit
from util import LoggingLevelRouter, singleton
from result import InsertionResult, SearchResult
from microservice import Microservice
from err import MicroserviceNullException, ServiceRegistryControllerException


@singleton
class ServiceRegistryController(Controller[ServiceRegistry]):
    """
    Role
        -   Controller
        -   Integrity Maintenance
        -   Consistency Assurance
    
    Responsibilities:
        1.  Ensure ServiceRegistry stays consistent during and after microservices.
    
    Attributes:
        registry: ServiceRegistry
        toolkit: ServiceRegistryToolkit
    
    Provides:
        -   def find_service(service_name: str) -> SearchResult[List[Microservice]]:
        
        -   def register_service(
                    service: Microservice,
                    null_exception: MicroserviceNullException,
            ) -> InsertionResult:
    
    Super Class:
        Controller
    """
    _registry: ServiceRegistry
    _toolkit: ServiceRegistryToolkit
    
    def __init__(
            self,
            registry: ServiceRegistry | None = None,
            toolkit: ServiceRegistryToolkit | None = None,
    ):
        self._registry = registry or ServiceRegistry()
        self._toolkit = toolkit or ServiceRegistryToolkit()
    
    @property
    def is_empty(self) -> bool:
        return self.number_of_services == 0
    
    @property
    def number_of_services(self) -> int:
        return len(self._registry.entries.keys())
    
    @LoggingLevelRouter.monitor
    def register_service(
            self,
            service: Microservice,
            null_exception: MicroserviceNullException | None = None,
    ) -> InsertionResult:
        """
        Add a new service to the registry.
        
        Action:
            1.  Send an exception chain in the InsertionResult if any of the following occur.
                    -   service is flagged unsafe.
                    -   Writing the service into the registry raises an error.
            2.  Otherwise, add the entry to the registry and return a success result.
        Args:
            service: Microservice
            null_exception: MicroserviceNullException
        Returns:
            InsertionResult
        Raises:
            ServiceRegistryControllerException
        """
        method = f"{self.__class__.__name__}.register_service"
        
        # --- Supply any missing dependencies. ---#
        if null_exception is None:
            null_exception = MicroserviceNullException()
            
        # Handoff the insertion request to the service.
        insertion_result = self._toolkit.register_new_service.execute(
            service=service,
            registry=self._registry,
            null_exception=null_exception,
        )
        # Handle the case that, the request is not satisfied.
        if insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                ServiceRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ServiceRegistryControllerException.MSG,
                    err_code=ServiceRegistryControllerException.ERR_CODE,
                    ex=insertion_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def find_service(self, name: str, ) -> SearchResult[List[Microservice]]:
        """
        Find a service in the registry.

        Action:
            1.  Send an exception chain in the SearchResult if the search is not completed.
            2.  Otherwise, send the success result.
        Args:
            name: str
        Returns:
            SearchResult[List[Microservice]]
        Raises:
            ServiceRegistryControllerException
        """
        method = f"{self.__class__.__name__}.find_service"
        
        # Handoff the search request to the service.
        search_result = self._toolkit.service_registry_search.execute(
            microservice_name=name,
            registry=self._registry,
        )
        # Handle the case that, the request is not satisfied.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                ServiceRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ServiceRegistryControllerException.MSG,
                    err_code=ServiceRegistryControllerException.ERR_CODE,
                    ex=search_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return search_result
        