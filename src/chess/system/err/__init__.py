# src/chess/system/err/__init__.py

"""
Module: chess.system.err.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

#=========== SYSTEM.ERR PACKAGE CONTENTS ===========#

# Packages
from .bounds import *
from .color import *
from .relational import *
from .resource import *
from .consistency import *

# Modules
from .null import NullException
from .base import ChessException
from .debug import DebugException
from .wrapper import ExceptionWrapper
from .catchall import CatchallException
from .unhandled import UnhandledRouteException
from .implementation import NotImplementedException


