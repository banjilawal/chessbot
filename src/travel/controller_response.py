from dataclasses import dataclass

from travel.message_body import MessageBody

MovementQuery
@dataclass(frozen=True)
class ControllerResponse:
    requestor_id: int
    distance_granted: int