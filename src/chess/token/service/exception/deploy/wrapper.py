# src/chess/token/service/exception/deploy/wrapper.py

"""
Module: chess.token.service.exception.deploy.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import OperationFailedException
from chess.token import TokenException


class TokenDeploymentFailedException(TokenException, OperationFailedException):
    pass