# src/shell/parser/parser.py

"""
Module: shell.parser.parser
Author: Banji Lawal
Created: 2026-03-01
version: 1.0.0
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar

from command.statement import UserStatement

T = TypeVar("T", bound="Command")

class StatementParser(ABC, Generic[T]):
    _key: Type[T]
    
    
    def __init__(self, key: Type[T]):
        self._key = key
        
    @property
    def key(self) -> Type[T]:
        return self._key
    
    def execute(self, cipher: UserStatement) -> ParseResult[T]:
        pass