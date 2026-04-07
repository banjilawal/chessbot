# src/microservice/catalog/__init__.py

"""
Module: microservice.catalog.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

import logging

log = logging.getLogger("chessbot")

# =========== CATALOG PACKAGE CONTENTS ===========#

# Packages
from .formation import *
from .persona import *
from .schema import *

# Modules
from .microservice import CatalogService