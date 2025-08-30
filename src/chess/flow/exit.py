from abc import ABC
from typing import cast

from chess.request.validators import ExitRequestValidator
from chess.flow.base import Flow


from chess.request.exit import ExitRequest
from chess.token.model import Piece


class ExitFlow(Flow, ABC):

    @staticmethod
    def enter_flow(request: ExitRequest):
        permission_result = ExitRequestValidator.validate(request)
        if not permission_result.is_success():
            raise permission_result.exception

        client = cast(Piece, permission_result.request.client)

