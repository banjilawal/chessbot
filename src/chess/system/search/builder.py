from chess.system import Builder, BuildResult
from chess.system.build.builder import T


class SearchResultBuilder(Builder):

    @classmethod
    def build(cls, *args, **kwargs) -> BuildResult[T]:
        pass