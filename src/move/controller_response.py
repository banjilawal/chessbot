from dataclasses import dataclass

from move.message_body import MessageBody


@dataclass(frozen=True)
class ControllerResponse:
    requestor_id: int
    response: MessageBody