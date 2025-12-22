# src/chess/catalog/validator/validator.py

"""
Module: chess.catalog.validator
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Any, cast

from chess.system import LoggingLevelRouter, ValidationResult, Validator
from chess.catalog import Catalog, InvalidCatalogException, NullCatalogException



class CatalogValidator(Validator[Catalog]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Simplify Searches based on rank metadata.
    2.  Verifies a candidate is not null and is an actual Catalog Enum.
    3.  Only have to write the two verification checks for a Catalog once. This gives cleaner code.
    4.  Verifies names and colors used in filtering and branching logic gets arguments in bounds.

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any,) -> ValidationResult[Catalog]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check the candidate is a Catalog enum
        3.  If both checks pass cast the candidate to a Catalog and return in a
            ValidationResult.

        # PARAMETERS:
            *   candidate (Any)

        # Returns:
        ValidationResult[Catalog] containing either:
            - On success:   Catalog in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullCatalogException
            *   InvalidCatalogException
        """
        method = "CatalogValidator.validate"
        
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    NullCatalogException(f"{method} {NullCatalogException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Catalog):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected Catalog, got {type(candidate).__name__} instead.")
                )
            # If no errors are detected cast the candidate to a Catalog object then return in
            # a ValidationResult.
            return ValidationResult.success(cast(Catalog, candidate))
        
        # Finally, catch any missed exception, wrap an InvalidPieceException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCatalogException(ex=ex, message=f"{method} {InvalidCatalogException.DEFAULT_MESSAGE}")
            )