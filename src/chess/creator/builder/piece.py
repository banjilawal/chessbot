from enum import Enum
from typing import cast

from assurance.exception.validation.piece import PieceValidationException
from chess.common.result import Result
from assurance.throw_helper import ThrowHelper
from assurance.validators.piece import PieceValidator
from chess.creator.builder.side import SideBuilder
from chess.creator.emit import id_emitter
from chess.rank.base import Rank
from chess.rank.bishop import Bishop

from chess.token.model import Piece


class PieceBuilder(Enum):

    @staticmethod
    def build(piece_id:int=id_emitter.piece_id, name:str="BN-1", rank:Rank=Bishop(), side=SideBuilder.build().payload) -> Result[Piece]:
        method = "PieceBuilder.build"
        try:
            # print(piece_id," ", side, " ", rank, " ", name)
            candidate = Piece(piece_id=piece_id, name=name, rank=rank, side=side)
            validation = PieceValidator.validate(candidate)
            if not validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, validation)

            piece = cast(Piece, validation.payload)
            return Result(payload=piece)

        except PieceValidationException as e:
            raise PieceValidationException(f"{method}: {PieceValidationException.DEFAULT_MESSAGE}") from e

        except Exception as e:
            return Result(payload=None, exception=e)


def main():
    build_result = PieceBuilder.build()
    if build_result.is_success():
        piece = build_result.payload
        print(f"Successfully built piece: {piece}")
    else:
        print(f"Failed to build piece: {build_result.exception}")
    #
    build_result = PieceBuilder.build(1, None)
    if build_result.is_success():
        piece = build_result.payload
        print(f"Successfully built piece: {piece}")
    else:
        print(f"Failed to build piece: {build_result.exception}")

if __name__ == "__main__":
    main()