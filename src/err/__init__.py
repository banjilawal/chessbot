# src/err/__init__.py

"""
Module: err.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

#===========  PACKAGE CONTENTS ===========#

# Packages
from .anchor import *
from .bounds import *
from .color import *
from .resource import *
from .debug import *
from .work import *

# Modules
from .root import ChessException
from .rollback import RollbackException