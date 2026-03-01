from typing import List

from chess.board import Board
from chess.edge import EdgeBuilder
from chess.graph import Graph
from chess.square import Square
from chess.system import BuildResult


class GraphBuilder:
    def build(origin: Square, incoming: List[Square], outgoing: List[Square]) -> BuildResult[Graph]:
        
        for square in incoming:
            if square.coord not in outgoing: