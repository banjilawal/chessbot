# src/chess/hostage/builder/exception/debug/occupation/victor.py

"""
Module: chess.hostage.builder.exception.debug.occupation.victor
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.hostage import HostageManifestException
from chess.system import DebugException


class VictorNotOccupyingCapturedSquareException(HostageManifestException, DebugException):
    pass