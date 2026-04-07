# src/operation/__ini__.py

"""
Module: operation.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

import logging

log = logging.getLogger("chessbot")

# =========== PACKAGE ===========#

# Packages
from operation.build.bootstrapper import *
from operation.build.creator import *
from .token import *

# Modules
from .operation import Operation