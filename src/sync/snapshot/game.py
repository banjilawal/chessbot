# src/sync/snapshot/sync.py

"""
Module: sync.snapshot.sync
Created: 2026-04-03
version: 0.0.2
"""

from typing import Optional

from domain import Sync


class Snapshot:
    """
    Role: Persistence, Messanger, Data Transport Object, Error Transport Object,

    Responsibilities:
    1.  Capture a snapshot of the Sync by recording Sync.arena state after an owner plays their turn.
    2.  Recording the Sync winner if the sync completed and there was no tie.
    3.  Enforcing mutual exclusion. A Snapshot can either carry payload or exception. Not both.

    Super Class:
        *   Result

    # PROVIDES:
    Snapshot

    # LOCAL ATTRIBUTES:
        *   arena (Arena)
        *   timestamp (int)
        *   sync_state (SyncState)
        *   winner (Optional[Player])

    # INHERITED ATTRIBUTES:
        *   See Result class for inherited attributes.
    """
    _sync: Sync
    _timestamp: int

    
    def __init__(
            self,
            sync: Sync,
            timestamp: int,
    ):
        """
        Args:
            sync: Sync,
            timestamp: int
        """
        self._timestamp = timestamp
        self._sync = sync
    
    @property
    def timestamp(self) -> int:
        return self.timestamp
    
    @property
    def sync(self) -> Sync:
        return self._sync
    
    @property
    def sync_state(self) -> Optional[SyncState]:
        return self._sync_state
    
    @property
    def sync_is_ready(self) -> bool:
        return self.exception is None and self._winner is None and self._sync_state == SyncState.CREATED
    
    @property
    def sync_is_running(self) -> bool:
        return self.exception is None and self._winner is None and self._sync_state == SyncState.RUNNING
    
    @property
    def sync_is_aborted(self) -> bool:
        return self.exception is None and self._winner is None and self._sync_state == SyncState.ABORTED
    
    @property
    def sync_is_won(self) -> bool:
        """Return True if the sync is won."""
        return self.exception is None and self._winner is not None and self._sync_state == SyncState.WON
    
    @property
    def sync_is_tied(self) -> bool:
        """Return True if the sync is tied."""
        return self.exception is None and self.winner is None and self._sync_state == SyncState.STALEMATE
    
    @property
    def sync_failed(self) -> bool:
        """Return True if the sync raised an exception."""
        return (
                self.exception is not None and
                (self._sync_state == SyncState.FAILURE or self._sync_state == SyncState.ROLLED_BACK)
        )
    
    @classmethod
    def won(cls, timestamp: int, arena: Arena, winner: PlayerAgent) -> Snapshot:
        return cls(timestamp=timestamp, arena=arena, winner=winner, sync_state=SyncState.WON)
    
    @classmethod
    def aborted(cls, timestamp: int, arena: Arena) -> Snapshot:
        return cls(timestamp=timestamp, arena=arena, sync_state=SyncState.ABORTED)
    
    @classmethod
    def tied(cls, timestamp: int, arena: Arena) -> Snapshot:
        return cls(timestamp=timestamp, arena=arena, sync_state=SyncState.STALEMATE)
    
    @classmethod
    def errored(cls, timestamp: int, arena: Arena, exception: Exception) -> Snapshot:
        return cls(timestamp=timestamp, arena=arena, exception=exception, sync_state=SyncState.FAILURE)
    
    @classmethod
    def rolled_back(cls, timestamp: int, arena: Arena, rollback_exception: RollbackException) -> Snapshot:
        return cls(timestamp=timestamp, arena=arena, exception=rollback_exception, sync_state=SyncState.ROLLED_BACK)
    
    @classmethod
    def empty(cls) -> Result:
        """Should not be called."""
        method = "Snapshot.empty"
        return Result(
            exception=MethodImplementationException(
                f"{method}: {MethodImplementationException.MSG}. Snapshot must "
                f"always have at least a payload and SyncState."
            )
        )
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Snapshot):
            return self._timestamp == other.timestamp
        return False
    
    def __hash__(self):
        return hash(self._timestamp)
