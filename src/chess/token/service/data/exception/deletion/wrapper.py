# src/chess/token/service/data/exception/deletion/wrapper.py

"""
Module: chess.token.service.data.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""


from chess.system import InsertionFailedException


class TokenDeletionFailedException(InsertionFailedException):
    ERROR_CODE ="TOKEN_DELETION_FAILURE"
    DERIVATIVE = "Token deletion failed."