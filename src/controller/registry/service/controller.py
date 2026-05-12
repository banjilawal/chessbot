# src/controller/registry/service/controller.py

"""
Module: controller.registry.service/controller
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import List

from controller import Controller
from microservice import Microservice
from model import ServiceRegistry
from util import LoggingLevelRouter, singleton
from result import InsertionResult, SearchResult
from microservice import Microservice, ServiceRegistryToolkit
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
        -   def find_service(domain: str, service_name: str) -> SearchResult[List[Microservice]]:
        -   def domain_services(domain: str) -> SearchResult[List[dict[str, Microservice]]]:
        
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
    def register(
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
        
        if null_exception is None:
            null_exception = MicroserviceNullException()
            
        # Handle the case that, the service fails a safety check.
        service_validation_result = self._toolkit.add_service_bootstrapper.execute(
            service=service,
            null_exception=null_exception,
            name_validator=self._toolkit.name_validator,
            validation_bootstrapper=self._toolkit.validation_bootstrapper,
        )
        if service_validation_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                ServiceRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ServiceRegistryControllerException.MSG,
                    err_code=ServiceRegistryControllerException.ERR_CODE,
                    ex=service_validation_result.exception
                )
            )
        # --- After The service is validated, run the registration steps. ---#
        insertion_result = self._toolkit.register_service.execute(
            service=service,
            registry=self._registry,
        )
        # Handle the case that, the service does not get registered.
        if insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                ServiceRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ServiceRegistryControllerException.MSG,
                    err_code=ServiceRegistryControllerException.ERR_CODE,
                    ex=service_validation_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def find_service(self, service_name: str,) -> SearchResult[List[Microservice]]:
        """
        Find a service in the registry.

        Action:
            1.  Send an exception chain in the SearchResult if either of the following occur:
                    -   A param is flagged unsafe.
                    -   The search is not completed.
            2.  Otherwise, send the success result.
        Args:
            service_name: str
        Returns:
            SearchResult[List[Microservice]]
        Raises:
            ServiceRegistryControllerException
        """
        method = f"{self.__class__.__name__}.call_service"
        
        # Handle the case that, the domain or microservice+name are flagged unsafe.
        param_validation_result = self._toolkit.service_search_bootstrapper.execute(
            name=service_name,
            name_validator=self._toolkit.name_validator,
            validation_bootstrapper=self._toolkit.validation_bootstrapper,
        )
        if param_validation_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                ServiceRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ServiceRegistryControllerException.MSG,
                    err_code=ServiceRegistryControllerException.ERR_CODE,
                    ex=param_validation_result.exception
                )
            )
        # --- When the params are validated, search with them. ---#
        search_result = self._toolkit.service_search.execute(
            service_name=service_name,
            registry=self._registry,
        )
        # handle the case that, the search was not completed.
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
        