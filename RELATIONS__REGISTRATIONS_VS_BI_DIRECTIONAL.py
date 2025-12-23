"""
=========================================================================
========= ENTITY RELATIONSHIPS: BI_DIRECTIONAL VS REGISTRATIONS =========
=========================================================================
For the application the ideal relations are binary. They may be either
bidirectional or unidirectional. The highest order relations are trinities.
Anything higher than that implies a poor design choice. Any triple relations
should be converted from a symmetric to transitive.

This document focuses on the types of binary relations.
    *   bidirectional
    *   unidirectional
    *   registrations

The differences mainly manifest in the
    **  TYPE OF SEARCHABLE: DataSet vs EntityMetadataHash
    **  EXCEPTION SUBCLASS: RegistrationException vs RelationExceptions.
    
There is a subtle difference between bidirectional and registration exception.

## WHAT IS A BIDIRECTIONAL RELATIONSHIP?:
========================================
This is simply a relationship between two entities that does not involve a data set.
The parties will have may have either

### TYPES OF BIDIRECTIONAL RELATIONSHIPS:
........................................

    1.  ONE-TO-ONE RELATIONSHIP:
    ...........................
        -   One side is a storage resource with permanent single slots, i.e Square, Arena.
        -   Other side is resource client that occupies and leaves the storage slot i.e Piece, Team
    
    2.  MANY-TO-ONE POINTER RELATIONSHIP:
    .....................................
        -   The one-side does not own a resource, collection, storage it provides.
        -   The each member in the many-set points to the one-sider.
        -   Neither side owns the relationship.
        -   One way only, one-side is unaware of the manys.
    3.  ONE-COLLECTION-OWNED-BY ONE RELATIONSHIP:
    .............................................
        -   owning-side has a collection of the many
        -   many-side-member can belong to a single collection owner. that is,
                many_side_entity_2.owner == owner_a
                many_side_entity_2.owner != owner_b
                many_side_entity_1.owner_a == owner_b

### TYPICAL USE CASES FOR BIDIRECTIONAL RELATIONSHIP:
.....................................................

    ALIVENESS:
    ..........
        Verifying a transient relationship between an entity occupying another. The transient occupier needs
        to launch a transaction from the hosting
        entity.
    
        EXAMPLE: -->    Verifying a Piece is active if it is occupying a Square.

    FINDER FILTERING:
    .................
        Using the one-side to filter items in a many-sides by one-side along with some other unique attribute
        they all have with the shared attribute that at least one collection member has.
    
        EXAMPLE: -->    Filtering Team datasets by Game (shared attribute) and globally unique (id), or
                        locally unique (designation, color)
                        
### BI_DIRECTIONAL_EXCEPTION SUPER CLASS:
........................................
    PARENT: ChessException
    ,,,,,,,,,,,,,,,,,,,,,,,,
    PURPOSE:
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        1.  Indicate if a required bidirectional relationship does not exist.
    
## WHAT IS A REGISTRATION RELATIONSHIP
======================================
THere are two conditions.
    1.  many_side_entity.owner == owner
    2.  many_side_entity in owner.many_items_dataset.
    
### REGISTRATION_EXCEPTION SUPER CLASS:
........................................
    PARENT: NoBidirectionalRelationshipException
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    
    PURPOSE:
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        1.  Indicate if an item has its owner set correctly but the item does not exist in the Owner's collection.
        2.  Indicate a bidirectional relationship is broken on the owning side
        3.  Raised when Entity.owner == owner but the Owner does not find the item in its dataset.
"""