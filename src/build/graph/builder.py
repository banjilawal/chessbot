from typing import List

from graph.graph import Graph
from logic.square import Square
from system import BuildResult


class GraphBuilder:
    def build(origin: Square, incoming: List[Square], outgoing: List[Square]) -> BuildResult[Graph]:
        
        for square in incoming:
            if square.coord not in outgoing: