# src/chess/system/transaction/exception/base.py

"""
Module: chess.system.transaction.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    #====================== TRANSACTION EXCEPTION #======================#
    'TransactionException',
]


#====================== TRANSACTION EXCEPTION #======================#
class TransactionException(ChessException):
    """
    # ROLE: Exception Wrapper
  
    # RESPONSIBILITIES:
    1.  Parent of exception raised by Transaction objects
    2.  Catchall for Transaction errors not covered by lower level  Transaction exception.
  
    # PARENT:
        *   ChessException
  
    # PROVIDES:
    TransactionException
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TRANSACTION_ERROR"
    DEFAULT_MESSAGE = "Transaction raised an exception."