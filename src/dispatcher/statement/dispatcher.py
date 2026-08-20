# src/dispatcher/statement/dispatcher.py

"""
Module: dispatcher.statement.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from command import CommandInterpreter
from command.parser import StatementParser
from request import OperationRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="OperationRequest")

class StatementDispatcher(ABC, Generic[T]):
    
    _parser: StatementParser[T]
    _interpreter: CommandInterpreter[T]
    
    def __init__(
            self,
            parser: StatementDispatcher[T],
            interpreter: CommandInterpreter[T],
    ):
        """
        Args:
            parser: StatementDispatcher[T]
            interpreter: CommandInterpreter[T]
        """
        self._parser = parser
        self._interpreter = interpreter
        
    @property
    def parser(self) -> StatementParser[T]:
        return self._parser
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> T:
        pass