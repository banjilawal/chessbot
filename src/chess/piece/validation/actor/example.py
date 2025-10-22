"""
Implements the `OccupationExecutor` class, which handles executing travel
directives in the chess engine. This includes moving pieces, capturing enemies,
and coordinating rollback logic in case of inconsistencies or failed operations.

Attributes:
  * `OccupationExecutor:` Main class responsible for executing travel directives.
  * `_attack_enemy`: Static method for processing attacks on enemy pieces.
  * `_run_scan`: Static method for handling discoveries on occupied squares.
  * `_switch_squares`: Static method the transferring team piece to team different `Square`.
"""