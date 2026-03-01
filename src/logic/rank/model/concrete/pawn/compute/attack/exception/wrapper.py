# src/logic/rank/model/concrete/pawn/compute/attack/exception/wrapper.py

"""
Module: logic.rank.model.concrete.pawn.compute.attack.exception.wrapper
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""



__all__ = [
    # ======================# PAWN_ATTACK_SPAN_COMPUTATION_FAILURE #======================#
    "PawnAttackSpanComputationException",
]

from logic.system import ComputationException


# ======================# PAWN_ATTACK_SPAN_COMPUTATION_FAILURE #======================#
class PawnAttackSpanComputationException(ComputationException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that prevent the Pawn's attack spanning set computation from producing a result.

    # PARENT:
        *   SpanComputationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PAWN_ATTACK_SPAN_COMPUTATION_FAILURE"
    MSG = "Pawn attack span computation failed."