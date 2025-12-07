# src/chess/system/builder/result/base.py

"""
Module: chess.system.builder.result.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import ResultException


class EmptyBuildResultException(ResultException):
    """BuildResult must contain either a payload or an exception"""
    ERROR_CODE = "EMPTY_BUILD_RESULT_ERROR"
    DEFAULT_MESSAGE = "BuildResult must contain either a payload or an exception. It cannot be empty."