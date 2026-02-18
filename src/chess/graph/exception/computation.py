from chess.graph import GraphException
from chess.system import ComputationFailedException


class GraphComputationFailedException(GraphException, ComputationFailedException):
    pass