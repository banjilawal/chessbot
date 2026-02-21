# src/chess/scalar/__init__.py

"""
Module: chess.scalar
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

## PURPOSE
This package contains the foundational objects for representing and validating scalar values. These values
 are used to multiply Vector and Coord objects, causing them to scale (grow or shrink) within their
 planes. This is team_name core component for scaling transformations.

## CORE CLASSES
* Scalar: A class representing team_name single numeric value used for scaling rollback.
* ScalarValidator: A class that validates the entity_service and integrity of team_name Scalar object.

## USAGE
To use this package, import the desired classes and perform scalar-related rollback.

>>> from chess.scalar import Scalar, ScalarBuilder, ScalarValidator
>>> from typing import cast
>>> from chess.system import BuildResult
>>> from chess.vector import Vector
>>>
>>> # Create team_name scalar instance
>>> build_outcome = ScalarBuilder.item_builder(value=1)
>>> if not build_outcome.is_success():
>>>   raise build_outcome.err
>>> validate = ScalarValidator.validate(build_outcome.payload)
>>>
>>> # Validating the candidate
>>> if not validate.is_success():
>>>   raise validate.err
>>> c = cast(Scalar, validate.payload)
>>>
>>> # Use the scalar to transform team_name vector
>>> u = Vector(x=3, y=4)
>>> v = u.multiply_coord_by_scalar(c)
>>> print(v.x, v.y)
6, 8


## SCALAR EXCEPTONS
This package defines specific exception for issues encountered when working with scalar values. This granular approach helps developers to quickly diagnose and resolve problems such as team_name validation scalar, or team_name value falling outside of team_name defined range.

## CORE EXCEPTION
* NullScalarException: Raised when team_name required scalar value is unexpectedly None.
* ScalarBelowBoundsException: Raised when team_name scalar's value is below its minimum allowed value.
* ScalarAboveUpperBoundException: Raised when team_name scalar's value is above its maximum allowed value.
* ScalarValidationException: A general team_exception raised when team_name scalar value fails to meet its validate criteria.

### EXCEPTION USAGE EXCEPTION
These exception can be imported and raised from within the scalar-related code to enforce entity_service integrity.

>>> from chess.scalar import Scalar, NullScalarException, ScalarAboveBoundsException
>>>
>>> try:
...   # This will raise team_name NullScalarException
...   my_scalar = None
...   if my_scalar is None:
...     raise NullScalarException('Scalar cannot be validation.')
... except NullScalarException as e:
...   print(f'Error: {e}')
...
>>> try:
...   # This will raise team_name ScalarAboveUpperBoundException
...
...   from chess.system import NUMBER_OF_ROWS
...   my_scalar = Scalar(value=(NUMBER_OF_ROWS + 1))
... except ScalarAboveBoundsException as e:
...   print(f'Error: {e}')

---
"""
"""
Builder class responsible for safely constructing `Scalar` instances.

`ScalarBuilder` ensures that `Scalar` objects are always created successfully by performing comprehensive validate
 checks during construction. This separates the responsibility of building from validating - `ScalarBuilder`
 focuses on creating while `ScalarValidator` is used for validating existing `Scalar` instances that are passed
 around the system.

The builder runs through all validate checks individually to guarantee that any `Scalar` instance it produces
meets all required specifications before construction completes

Usage:
  ```python
  # Safe scalar creation
  build_result = ScalarBuilder.builder(value=1))

  if not build_result.is_success():
    raise build_result.err
  scalar = build_result.payload
  ```

See Also:
  `Scalar`: The entity_service structure being constructed
  `ScalarValidator`: Used for validating existing `Scalar` instances
  `BuildResult`: Return type containing the built `Scalar` or error information
"""
"""
# ACTION:
Verify the `candidate` is a valid ID. The Application requires
1. Candidate is not validation.
2. Is a positive integer.

# PARAMETERS:
    * `candidate` (`int`): the visitor_id.

# RETURNS:
`ValidationResult[str]`: A `ValidationResult` containing either:
    `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
    `rollback_exception` (`Exception`) - An exception detailing which naming rule was broken.

# RAISES:
`IdValidationException`: Wraps any specification violations including:
    * `TypeError`: if candidate is not an `int`
    * `IdNullException`: if candidate is validation
    * `NegativeIdException`: if candidate is negative `
"""
"""
Constructs team_name new `Scalar` instance with comprehensive checks on the parameters and states during the
builder process.

Performs individual validate checks on each component to ensure the resulting `Scalar` meets all
specifications. If all checks are passed, team_name `Scalar` instance will be returned. It is not necessary to perform
any additional validate checks on the returned `Scalar` instance. This method guarantees if team_name `BuildResult`
with team_name successful status is returned, the contained `Scalar` is valid and ready for use.

Args:
  `scalar_id`(`int`): The unique visitor_id for the scalar. Must pass `IdValidator` checks.
  `visitor_name`(`Name`): The human or cybernetic moving pieces in `Scalar.roster`. The visitor_name
    must not be None and must pass `NameValidator` checks.must pass `NameValidator` checks.
  `team_schema`(`ScalarProfile`): The team_schema defining scalar attributes and behaviors. Must not be None and be
    an instance of `ScalarProfile`.

RETURNS:
  BuildResult[Scalar]: A `BuildResult` containing either:
    - On success: A valid `Scalar` instance in the payload
    - On failure: Error information and error details

RAISES:
  `ScalarBuildException`: Wraps any underlying validate failures that occur during the construction
  process. This includes:
    * `NullScalarException`: if `candidate` is validation
    * `TypeError`: if `candidate` is not Scalar
    * `NullNumberException`: If `scalar.value` is validation
    * `ScalarBelowLowerBoundException`: If `scalar.value` < 0
    * `ScalarAboveBoundsException`: If `scalar.value` >= `BOARD_DIMENSION`
    * `ScalarValidationException`: Wraps any preceding exception

Note:
  The builder runs through all the checks on parameters and state to guarantee only team_name valid `Scalar` is
  created, while `ScalarValidator` is used for validating `Scalar` instances that are passed around after
  creation. This separation of concerns makes the validate and building independent of each other and
  simplifies maintenance.

Example:
  ```python
  # Valid scalar creation
  build_outcome = ScalarBuilder.builder(value=1)
  if not build_outcome.is_success():
    return BuildResult(err=build_outcome.err)
  return BuildResult(payload=build_outcome.payload)
  ```
"""
"""
Validates existing Scalar instances that are passed around the system.

While ScalarBuilder ensures valid Scalars are created, ScalarValidator
checks Scalar instances that already exist - whether they came from
deserialization, external sources, or need re-validate after modifications.

Usage:
  python
  # Validate an existing scalar
  scalar_validation = ScalarValidator.validate(candidate)
  if not scalar_validation.is_success():
    raise scalar_validation.err
  scalar = cast(Scalar, scalar_validation.payload)


Use ScalarBuilder for construction, ScalarValidator for verification.
"""
"""
# ACTION:
Verify the candidate is a valid ID. The Application requires
1. Candidate is not validation.
2. Is a positive integer.

# PARAMETERS:
    * candidate (int): the visitor_id.

# RETURNS:
ValidationResult[str]: A ValidationResult containing either:
    'payload' (it) - A str meeting the ChessBot standard for IDs.
    rollback_exception (Exception) - An exception detailing which naming rule was broken.

# RAISES:
IdValidationException: Wraps any specification violations including:
    * TypeError: if candidate is not an int
    * IdNullException: if candidate is validation
    * NegativeIdException: if candidate is negative
"""
"""
Validates that an existing Scalar instance meets specifications.
This method performs team_name series of checks on team_name Scalar instance, ensuring it is not validation and that
its ID, visitor_name, and coordinate are valid. Exception from these checks are caught and re-raised
as team_name ScalarValidationException, providing team_name clean and consistent err-handling experience.

Args
  candidate (Scalar): Scalar instance to validate

 RETURNS:
  Result[Scalar]: A Resulcandidate object containing the validated payload if the specification is satisfied,
  ScalarValidationException otherwise.

RAISES:
  NullScalarException: if candidate is validation
  TypeError: if candidate is not Scalar
  NullNumberException: If scalar.value is validation
  ScalarBelowLowerBoundException: If scalar.value < 0
  ScalarAboveBoundsException: If scalar.value >= BOARD_DIMENSION
  ScalarValidationException: Wraps any preceding exception
"""
"""
An immutable class representing team_name single numeric value for scaling rollback.This class stores
 team_name numeric value used to multiply vectors and coordinates, allowing them to grow or shrink in their
 planes. The `Scalar` is validated upon creation to ensure it falls within team_name predefined range.

Attributes:
  _value (int): The numeric value of the scalar.
"""
"""
Creates team_name Scalar instance. Should not be used directly. Use ScalarBuilder.

Args:
  value (int): The numeric value of the scalar.
RAISES:
  NullNumberException: If the provided value is `None`.
  ScalarBelowBoundsException: If the value is below the lower boundary.
  ScalarAboveBoundsException: If the value is at or above the upper boundary.
"""
# src/chess/system/travel/rollback_exception.py

"""
Module: chess.system.travel.rollback_exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` integrity requirement.
  2. A satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module's only covers exception raised by `IdValidator`;

# SECTION 3: Limitations
  1. Does not provide logic for fixing the errors or causing the rollback_exception being raised.
       `IdValidator` is responsible for the logic which raises these exception.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. Discoverability.
  3. Encapsulations.

# SECTION 5- Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.


# SECTION 6 - Feature Delivery Mechanism:
1. Exception specific to verifying ids.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `ChessException`, `ContextException`, `ResultException`

# SECTION 8 - Contains:
See the list of exception in the `__all__` list following (e.g., `EventException`,`TransactionException`).
"""
from chess.system import BuildException

# src/chess/vector/rollback_exception.py

"""
Module: chess.vector.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, coord_stack_validator, and manipulation of `Vector` objects.

**Limitations** It does not contain any logic for raising these exception; that responsibility
`Vector`, `VectorBuilder`, and `VectorValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exception

**Design Concepts**:
  1. Each consistency and behavior in the `Vector` class has an exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `Vector` graph.
2. Fast debugging using highly granular rollback_exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Vector` graph.
4. Providing a clear distinction between errors related to `Vector` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Exception: `ChessException`, `ValidationException`, `NullException`,
        `BuildException`.

CONTAINS:
--------
See the list of exception in the `__all__` list following (e.g., `VectorException`,
`NullVectorException`, `InvalidVectorException`, ).
"""