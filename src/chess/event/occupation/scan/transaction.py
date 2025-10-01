from typing import cast

from chess.piece import Discovery, DiscoveryBuilder
from chess.event import ScanEvent, OccupationTransaction, OccupationEventException

from chess.common import ExecutionContext, TransactionResult
from chess.piece.discover.exception import AddingValidDiscoveryFailedException
from chess.transaction import TransactionException


class ScanTransaction(OccupationTransaction[ScanEvent]):
    pass

    @staticmethod
    def execute(event: ScanEvent, context: ExecutionContext) -> TransactionResult:
        method = "ScanTransaction.execute"

        try:
            build_result = DiscoveryBuilder.build(observer=event.observer, subject=event.subject)
            if not build_result.is_success():
                return TransactionResult(exception=build_result.exception)

            discovery = cast(Discovery, build_result.payload)
            if discovery not in event.observer.discoveries:
                event.observer.discoveries.record_discovery(discovery=discovery)

            if discovery not in event.observer.discoveries.items:
                return TransactionResult(
                    event=event,
                    exception=AddingValidDiscoveryFailedException(
                        f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"
                    )
                )

            return TransactionResult(event=event)
        except TransactionException as e:
            raise TransactionException(f"{method}: {e.message}") from e