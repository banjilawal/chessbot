from chess.graph import Vertex
from chess.square import Square, SquareValidator
from chess.system import BuildResult, Builder


class VertexBuilder(Builder[Vertex]):
     
     @classmethod
     def build(cls, square: Square, square_validator: SquareValidator = SquareValidator()) -> BuildResult[Vertex]:
         pass