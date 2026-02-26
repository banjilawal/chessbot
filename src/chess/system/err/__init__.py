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
from .resource import *
from .consistency import *

# Modules
from .null import NullException
from .root import ChessException
from .debug import DebugException
from .wrapper import WrapperException
from .catchall import CatchallException
from .rollback import RollbackException
from .route import NoExecutionRouteException
from chess.system.err.wrapper.operation.operation import OperationException
from .implementation import MethodNotImplementedException


