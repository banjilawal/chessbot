"""
=====================================================================================
====== THE SEARCHABLE SERVICES FORWARD/REVERSE MAP LOOKUPS VS DATASET SEARCHES =======
======================================================================================
The application has two types of searchable objects.
    1.  DataServices -- contain a data stack.
    2.  Metadata Tables -- static read-only hash table represented as an enum.

Both searchables uses contexts to create a search attribute-value pair to find matches. DatasServices are
intuitive with their CRUD operations. This introduction section gives an overview of Metadata Tables, their
behavior and functionality. The closing section talks about how the Context flag exceptions are named for the
Metadata tables.

OVERVIEW OF METADATA HASH TABLES
================================

## WHAT TYPES OF CLASSES USE METADATA TABLES:
--------------------------------------------
Have Classes with preset readonly instance fields with common values in a subclass exhibit different behavior per
subclass. These classes are:
    *   Built using factories.
    *   Implement strategy patterns.
    *   Use an Enum table to get properties for different categories of data holding collections which act as
        controllers.

## USE CASES FOR THE METADATA HASH TABLE:
-----------------------------------------
    *   Build configuration.
    *   Writing search filters.
Both use cases do forward and reverse lookups unlike dataset searches.
    *   FORWARD LOOKUP: object.field_value --> Enum.MEMBER
    *   REVERSE LOOKUP: Enum.MEMBER --> Class

## COMPARISON OF ENTITY_DATA AND METADATA_HASH SERVICES
-------------------------------------------------------

### ARCHITECTURE FOR ENTITY DATA SERVICE:
````````````````````````````````````````
    *   ContextService{
            EntityContext
            EntityContextBuilder,
            EntityContextValidator,
            EntityFinder(EntityList, EntityContext, EntityValidator) -> SearchResult[Entity]
            ................................................................................
            EntityContextExceptions {
                ZeroEntityContextsFlagsException
                ExcessiveEntityContextsFlagsException
            }
            ..........................................
        }
        ..............................................
    *   EntityService{
            EntityBuilder,
            EntityValidator
        }
        ................................................
    *   EntityList
    ....................................................

## ARCHITECTURE FOR METADATA HASH SERVICE:
``````````````````````````````````````````
*   HashContextService{
        HashContext
        HashContextBuilder,
        HashContextValidator,
        HashLookup(HashContext, HashContextValidator) -> SearchResult[HashMember]
        .........................................................................
        HashContextExceptions {
            ZeroHashMapKeysException
            ExcessiveHashMapKeysException
        .............................................
    }
    ................................................
*   Hash{Category: MetadataSet}
    ...............................................
*   HashService{
        HashValidator,
        HashMember_EntityMapper
        ReverseHashLookup(
            EntityDataSet,
            HashLookup(EntityDataSet, entity.attribute, HashContextService.validator),
        ) --> SearchResult[List[Entity]]
    }
    .................................................................................
   """