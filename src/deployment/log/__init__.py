# src/deployment/log/__init__.py

"""
Module: deployment.log.__init__
Author: Banji Lawal
Created: 2025-08-24
version: 1.0.0
"""

import logging

log = logging.getLogger("chessbot")

# =========== LOG PACKAGE CONTENTS ===========#

# Packages
None

# Modules
from .mode import LogLevelMode
from .level import LogLevelSetter