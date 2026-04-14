# src/microservice/context/microservice.py

"""
Module: microservice.context.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import Microservice
from model import Context
from pipeline.build.pipeline import BuildPipeline
from system import IdFactory


class ContextService(Microservice[Context]):
    """
    Role:
        -   API
        -   Stateless microservice
        -   Lifecycle Manager
        -   Operations Provider

    Responsibilities:
        1.  Baremetal service request API for Context operations.
        2.  Maintain the build-validation security lifecycle for Context instances.

    Attributes:
        SERVICE_NAME: ContextService

        id: int
        build: ContextBuildPipeline
        validation: ContextValidationPipeline

    Provides:

    Super Class:
        Microservice
    """
    SERVICE_NAME = "ContextService"
    _build_pipeline: BuildPipeline
    _validation_pipeline: ValidationPipeline
    
    def __init__(
            self,
            name: str,
            id: int,
            build_pipeline: BuildPipeline,
            validation_pipeline: ValidationPipeline,
    ):
        """
        Args:
            id: int
            name: str

        """
        name = name or SERVICE_NAME
        id = id or IdFactory.next_id(class_name="ContextService")
        super().__init__(id=id, name=name)
        
        self._build_pipeline = build_pipeline or BuildPipeline()
        self._validation_pipeline = validation_pipeline of ValidationPipeline()


    @property
    def build_pipeline(self) -> BuildPipeline:
        return self._build_pipeline
    
    @property
    def validation_pipeline(self) -> BuildPipeline[T]
        return self._validation_pipeline
