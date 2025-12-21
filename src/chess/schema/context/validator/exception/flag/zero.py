# src/chess/schema/context/validator/exception/flag/zero.py

"""
Module: chess.schema.context.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.schema import InvalidSchemaContextException

__all__ = [
    # ========================= ZERO_SCHEMA_CONTEXT_ENUM_TUPLES EXCEPTION =========================#
    "ZeroSchemaContextEnumTuplesException",
]


# ========================= ZERO_SCHEMA_CONTEXT_ENUM_TUPLES EXCEPTION =========================#
class ZeroSchemaContextEnumTuplesException(InvalidSchemaContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging
    
    # INTRODUCTION:
    The application has two types of searchable objects.
        1.  DataServices -- contain a data stack.
        2.  Metadata Tables -- static read-only hash table represented as an enum.
    Both searchables uses contexts to create a search attribute-value pair to find matches. DatasServices are
    intuitive with their CRUD operations. This introduction section gives an overview of Metadata Tables, their
    behavior and functionality. The closing section talks about how the Context flag exceptions are named for the
    Metadata tables.
    
    ## WHAT TYPES OF CLASSES USE METADATA TABLES:
    Have Classes with preset readonly instance fields with common values in a subclass exhibit different behavior per
    subclass. These classes are:
        *   Built using factories.
        *   Implement strategy patterns.
        *   Use an Enum table to get properties for different categories of data holding collections which act as
            controllers.
      
    ### USE CASES FOR THE ENUM METADATA TABLE:
        *   Build configuration.
        *   Writing search filters.
    Because these are tables forward and reverse lookups are done instead of searches.
    
        FORWARD LOOKUP: object.field_value --> Enum.MEMBER
        REVERSE LOOKUP: Enum.MEMBER --> Class

    ## ARCHITECTURE FOR ENTITY DATA SERVICE:
        *   ContextService{
                EntityContext
                EntityContextBuilder,
                EntityContextValidator,
                EntityFinder(EntityList, EntityContext, EntityValidator) -> SearchResult[Entity]
                
                EntityContextExceptions {
                    ZeroEntityContextsFlagsException
                    ExcessiveEntityContextsFlagsException
                }
            }
        *   EntityService{
                EntityBuilder,
                EntityValidator
            }
        *   EntityList
        
        
        ## ARCHITECTURE FOR ENTITY METADATA HASH TABLE SERVICE:
        *   HashContextService{
                HashContext
                HashContextBuilder,
                HashContextValidator,
                HashLookup(HashContext, HashContextValidator) -> SearchResult[HashMember]
                
                HashContextExceptions {
                    ZeroHashContextsEnuTuplesException
                    ExcessiveHashContextsEnumTuplesException
            }

        *   Hash{Category: MetadataSet}
        *   HashService{
                HashValidator,
                HashMember_EntityMapper
                ReverseHashLookup(
                    EntityDataSet,
                    HashLookup(EntityDataSet, entity.attribute, HashContextService.validator),
                ) --> SearchResult[List[Entity]]
            }
        
        
        

        
    

    # RESPONSIBILITIES:
    1.  Indicate no SchemaContext flag is provided for a forward Schema lookup.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidSchemaContextException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_SCHEMA_CONTEXT_ENUM_TUPLES_ERROR"
    DEFAULT_MESSAGE = (
        "No SchemaContext flag was selected. A SchemaContext must be enabled with an attribute-value-tuple"
        " to perform a forward Schema entry lookup."
    )