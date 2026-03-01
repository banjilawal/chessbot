# src/logic/checking/check/exception.py

"""
Module: logic.checking.check.exception
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""


from logic.checking import CheckingException


class InCheckException(CheckingException):
    ERR_CODE = "IN_CHECK_EXCEPTION"
    DEFAULT_ERR_CODE = "InCheck raised an exception."