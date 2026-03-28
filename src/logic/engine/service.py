# src/logic/engine/transaction.py

"""
Module: logic.engine.service
Author: Banji Lawal
Created: 2025-11-18
version: 1.0.0
"""


from typing import Any

from logic.engine import Engine
from logic.engine.builder import EngineBuildTransaction
from logic.engine.validator import EngineValidationTransaction
from logic.system import BuildResult, ValidationResult


class EngineService:
    _id: int
    _engine: Engine
    _builder: EngineBuildTransaction
    _validator: EngineValidationTransaction
    
    def __init__(self, engine_id: int, builder: EngineBuildTransaction, validator: EngineValidationTransaction):
        self._id = engine_id
        self._builder = builder
        self._validator = validator
        
    
    @property
    def id(self) -> int:
        return self._id
    
    
    @property
    def engine(self) -> Engine:
        return self._engine
    
    
    def build_engine(self, *args, **kwargs) -> BuildResult[Engine]:
        return self._builder.execute()
    
    
    def validate_engine(self, candidate: Any) -> ValidationResult[Engine]:
        return self._validator.execute(candidate=candidate)