from logic.span import NodeEdgeHandlerException, SquareGraphHandler


class SpanGraphHandler:
    _node: SquareGraphHandler
    _edge: NodeEdgeHandlerException
    
    def __init__(
            self,
            node: SquareGraphHandler = SquareGraphHandler(),
            edge: NodeEdgeHandlerException = NodeEdgeHandlerException(),
    ):
        """
        Args:
            node: SpanningGrapNodeHandler
            edge: NodeEdgeHandlerException
        """
        self._node = node
        self._edge = edge
        
    @property
    def node(self) -> SquareGraphHandler:
        return self._node
    
    @property
    def edge(self) -> NodeEdgeHandlerException:
        return self._edge