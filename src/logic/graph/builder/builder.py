from typing import List

from logic.board import Board
from logic.edge import EdgeBuilder
from logic.graph import Graph
from logic.square import Square
from logic.system import BuildResult


class GraphBuilder:
    def build(origin: Square, incoming: List[Square], outgoing: List[Square]) -> BuildResult[Graph]:
        
        for square in incoming:
            if square.coord not in outgoing: