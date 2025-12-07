# src/chess/checking/check/base.py

"""
Module: chess.checking.check.exception
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""


from chess.checking import CheckingException


class InCheckException(CheckingException):
    ERROR_CODE = "IN_CHECK_ERROR"
    DEFAULT_ERROR_CODE = "InCheck raised an exception."