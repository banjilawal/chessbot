# src/shell/menu/menu.py

"""
Module: shell.menu.menu
Author: Banji Lawal
Created: 2026-03-01
version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from microservice import Microservice
from domain.exchange.request import Request
from command.statement import UserStatement
from util import LoggingLevelRouter

T = TypeVar("T", bound="Microservice")


class CommandMenu(ABC, Generic[T]):
    _dispatchers: dict[str, StatementDispatcher] = []


    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> Request:
        validation = statement_validator.execute(job)
        
        if validation.is_failure:
            return InterpretationResult.failure(validation.exception)
        statement = cast(UserStatement, validation.payload)
        
        if statement.name not in self._dispatchers.keys():
            return InterpretationResult.failure(f"Command {statement.name} not found")
        
        parse = dispatchers[statement.name].execute(statement)
        if parse.is_failure:
            return InterpretationResult(parse.exception)
        request = cast(Request, parse.payload)
        
        return InterpreationResult(request)
        
        
    