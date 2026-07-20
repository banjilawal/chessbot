
from __future__ import annotations

from typing import Optional

from builder import Builder, LinearEndpointFactory
from register import VectorRegister
from result import BuildResult
from util import LoggingLevelRouter


class SpaceEndpointFactory(Builder[VectorRegister]):
    
    _linear_endpoint_factory: LinearEndpointFactory
    
    def __init__(
            self,
            linear_endpoint_factory: Optional[LinearEndpointFactory] | None = LinearEndpointFactory(),
    ):
        self._linear_endpoint_factory = linear_endpoint_factory
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[VectorRegister]:
        pass