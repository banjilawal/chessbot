# src/microservice/catalog/__init__.py

"""
Module: microservice.catalog.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

import logging

log = logging.getLogger("chessbot")

# =========== MICROSERVICE.CATALOG PACKAGE ===========#

# Packages
from .formation import *
from .persona import *
from .schema import *

# Modules
from .microservice import CatalogService