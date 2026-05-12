# src/operation/registry/service/search/name.operation.py

"""
Module: operation.registry.service.search.name.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import List

from result import SearchResult
from model import ServiceRegistry
from util import LoggingLevelRouter
from operation import Operation, ServiceRegistryOperation



class ServiceRegistryNameSearch(ServiceRegistryOperation):
    OPERATION_NAME = "registry_service_search"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            domain: str,
            operation_name: str,
            registry: ServiceRegistry,
    ) -> SearchResult[List[Operation]]:
        method = f"{cls.__name__}.execute"
        
        if domain.upper() not in registry.domains:
            return SearchResult.empty()
        if operation_name.upper() not in registry.entries[domain].keys():
            return SearchResult.empty()
        operation = registry.entries[domain][operation_name]
        return SearchResult.success(List[operation])