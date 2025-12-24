# src/chess/formation/map.py

"""
Module: chess.formation.map
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional


from chess.formation.formation import Formation
from chess.system import Context, GameColor

"""
# ROLE: Filter, Search, Selection, Reverse/Forward Lookups

Lookups are performed on the Schema table.

## FORWARD LOOKUPS:
A forward lookup takes an attribute-value tuple and searches the hashtable entries for a matching tuple.
    *   If the attribute does not exist the Lookup fails, raising an error.
    *   If the no entry has the match value for its attribute the lookup fails, raising an error.
    *   The first entry that matches the search tuple the lookup succeeds, returning the entry.
All entries in the hashtable have unique instances of an attribute-value tuple so there are no search collisions.

The attribute-value is used as SuperKey. to search each entry's metadata list.

## REVERSE LOOKUP:
A reverse lookup takes a schema entry and returns a different metadata hashtable with a transitive relationship.
Teams do not need reverse lookups. Searches by a team schema property do not need a reverse lookup. A use case
might be looking up formations of openings for a set of pieces. Assuring the Arena tuples of PlayerAgent-Team
are unique.

# RESPONSIBILITIES:
The for A SchemaSuperKey is used tForward Schema lookups use a SchemaSuperKet ro
1.  Provides information to complete run forward-lookups on the Schema
1.  Define a SuperKey from an attribute-value pair. The attribute must exist in the schema.
2.  A forward lookup for a Schema variant requires a SchemaSuperKey.

# PARENT:
    *   Context

# PROVIDES:
None

# LOCAL ATTRIBUTES:
    *   color (Optional[GameColor])

# INHERITED ATTRIBUTES:
    *   See Context class for inherited attributes.
"""
class FormationSuperKey(Context[Formation]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    Provide an BattleOrderFinder with an attribute value to find BattleOrders with a matching value in
    their version of the attribute.

    # PARENT:
        *   Context

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   square_name (Optional[str])
        *   designation (Optional[str])
        *   color (Optional[ColorColor])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _square: Optional[str]
    _color: Optional[GameColor]
    
    def __init__(
            self,
            square: Optional[str] = None,
            designation: Optional[str] = None,
            color: Optional[GameColor] = None,
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   square_name (Optional[str])
            *   designation (Optional[str])
            *   color (Optional[Color])

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=None, name=None)
        self._color = color
        self._square = square
        self._designation = designation
    
    @property
    def color(self) -> Optional[GameColor]:
        return self._color
    
    @property
    def square(self) -> Optional[str]:
        return self._square
    
    @property
    def designation(self) -> Optional[str]:
        return self._designation
    
    def to_dict(self) -> dict:
        """
        # ACTION
            1.  Convert the SchemaSuperKey object to a dictionary.
        # PARAMETERS:
            *   None
        # RETURNS:
            *   dict
        # RAISES:
            *   None
        """
        return {
            "color": self._color,
            "square_name": self._square,
            "designation": self._designation,
        }