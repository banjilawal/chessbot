# src/operation/registry/service/search/domain.operation.py

"""
Module: operation.registry.service.search.domain.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Dict, List

from result import SearchResult
from model import ServiceRegistry
from util import LoggingLevelRouter
from operation import Operation, ServiceRegistryOperation


class ServiceRegistryDomainSearch(ServiceRegistryOperation):
    OPERATION_NAME = "service_registry_domain_search"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            domain: str,
            registry: ServiceRegistry,
    ) -> SearchResult[Dict[str, Operation]]:
        method = f"{cls.__name__}.execute"
        
        if domain.upper() not in registry.domains:
            return SearchResult.empty()
        services = registry.entries[domain.upper()]
        return SearchResult.success(services)