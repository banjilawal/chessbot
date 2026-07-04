# src/model/state/registry/service.model.py

"""
Module: model.state.registry.service.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Dict

from microservice import Microservice


class ServiceRegistry:
    """
    Role
        -   Controller
        -   Publisher
    
    Responsibilities:
        1.  Dynamic, entry and removal of public microservices available for building toolkits.
        2.  Uses namespaces to improve search and minimize hash collisions.
    
    Attributes:
        invocation_counters: dict[str, int]
        registration_counters: dict[str, int]
        entries: Dict[str, Dict[str, Microservice]]
    
    Provides:
        -   def domains(self) -> List[str]:
    
    Super Class:
    """
    _invocation_counters: dict[str, int]
    _registration_counters: dict[str, int]
    _entries: Dict[str, Microservice]
    
    def __init__(self):
        self._entries = {str: Microservice}
        self._invocation_counters = {}
        self._registration_counters = {}
        
    @property
    def entries(self) -> Dict[str, Microservice]:
        return self._entries
    
    @property
    def invocation_counters(self) -> dict[str, int]:
        return self._invocation_counters
    
    @property
    def registration_counters(self) -> dict[str, int]:
        return self._registration_counters
    
