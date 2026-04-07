# src/worker/__init__.py

"""
Module: worker.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

import logging

log = logging.getLogger("chessbot")

# =========== PACKAGE CONTENTS ===========#

# Packages
from .lingeo import *


# Modules
from .worker import Worker