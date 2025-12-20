# src/chess/catalog/lookup/context/context.py

"""
Module: chess.catalog.lookup.context.context
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""
from typing import Optional

from chess.catalog import Catalog
from chess.system import Context


class CatalogContext(Context[Catalog]):
    """
    # ROLE: Finder Filter

    # RESPONSIBILITIES:
    Provide a Catalog lookup with an attribute value to find Catalog entries with a matching attribute values.

    # PARENT:
        *   Context

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   designation (str)
        *   ransom (int)
        *   quota  (int)

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _ransom: Optional[int]
    _quota: Optional[int]
    _designation: Optional[str]
    
    def __init__(
            self,
            name: Optional[str] = None,
            ransom: Optional[int] = None,
            quota: Optional[int] = None,
            designation: Optional[str] = None,
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   name (Optional[str])
            *   ransom (Optional[int])
            *   quota (Optional[int])
            *   designation (Optional[str])

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=None, name=name)
        self._ransom = ransom
        self._quota = quota
        self._designation = designation
    
    @property
    def ransom(self) -> Optional[int]:
        return self._ransom
    
    @property
    def quota(self) -> Optional[int]:
        return self._quota
    
    @property
    def designation(self) -> Optional[str]:
        return self._designation
    
    def to_dict(self) -> dict:
        """
        # Convert the OrderContext object to a dictionary.

        # PARAMETERS:
        None

        # Returns:
        dict

        # Raises:
        None
        """
        return {
            "name":self.name,
            "quota": self._quota,
            "ransom": self._ransom,
            "designation": self._designation,
        }