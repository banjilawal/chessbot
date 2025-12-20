# src/chess/dyad/service/exception.py

"""
Module: chess.dyad.service.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException
from chess.dyad import SchemaAgentPairException

class SchemaAgentPairServiceException(SchemaAgentPairException, ServiceException):
    pass