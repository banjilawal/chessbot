from typing import List

from chess.graph import Node, NodeService
from chess.system import DeletionResult, InsertionResult, LoggingLevelRouter, StackService


class NodeStack(StackService[Node]):
    _id: int
    _items: List[Node]
    _service: NodeService
    
    def __init__(self, service: NodeService):
        self._service = service
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def integrity_service(self) -> NodeService:
        return self._service
    
    @LoggingLevelRouter.monitor
    def push(self, item: Node) -> InsertionResult:
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Node]:
        pass