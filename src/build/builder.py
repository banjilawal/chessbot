# src/logic/system/build/build/exception.py

"""
Module: logic.system.build.build.build
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from system import BuildResult, LoggingLevelRouter, Validator

T = TypeVar("T")


class Builder(ABC, Generic[T]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
       
    Workers:
        -   Workers are the logic that implements a process.
        -   Processes produce a result.
        
        Naming Problems:
            -   Don't have a good naming convention for workers yet. Maybe <ProcessName>Worker? as default,
                if it's not clunky.
            -   Worker entry points are named execute. Might change them to work() and the work executes the process.
            
            Exceptions:
                -   Exceptions are only about the process.
                -   Exception naming convention is <ProcessName>Exception.

        Transaction Worker:
            -   Work on stateful data objects.
            -   Include a data object's previous state in their work product.
            -   For simplicity, speed, and side-effect avoidance use deep copy before state changing logic.
            -   Client uses original data for rollbacks if transaction fails.
   
        Build Worker Naming:
            -   Builders are a core workers in the system.
            -   The least clunky and intuitive schema is <EntityName>Builder.
            -   Developers might assume other process exceptions are about the worker and use confusing naming
                conventions for other processes and their exceptions.
            -   Despite the possible confusion <EntityName>Builder naming is worth the trade off.
        
    Responsibilities:
        1.  Creation process owners.
        2.  Execute binding logic for related entities.
        3.  Assure objects comply with business logic at point of creation.
        4.  Ensure stateful data-holding build resources meet satisfy contracts.
    
    Attributes:

    Provides:
        -   build(*args, **kwargs) -> BuildResult[T]
        
    Super Class:
    """
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def build(cls, *args, **kwargs) -> BuildResult[T]:
        pass