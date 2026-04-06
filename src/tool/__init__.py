# src/tool/__init__.py

"""
Module: tool.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

import logging

log = logging.getLogger("chessbot")

# =========== PACKAGE CONTENTS ===========#

# Packages
from .lingeo import *
from rank import *
from .square import *

# Modules
from .tool import ToolSet