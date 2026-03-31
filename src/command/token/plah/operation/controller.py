# src/command/root/service/operation/controller.py

"""
Module: command.root.service.operation.controller
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations



class CommandOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations CommandService supports.
        
    Attributes:
        builder: CommandBuilder
        validator: CommandValidator

    Provides:
    
    Super Class:
    """
    _builder: CommandBuilder
    _validator: CommandValidator
    
    def __init__(
            self,
            build: CommandBuilder = CommandBuilder(),
            validation: CommandValidator = CommandValidator(),
    ):
        """
        Args:
            build: CommandBuilder
            validation: CommandValidator
        """
        self._builder = builder
        self._validator = validator
        
    @property
    def builder(self) -> CommandBuilder:
        return self._builder
        
    @property
    def validator(self) ->CommandValidator:
        return self._validator