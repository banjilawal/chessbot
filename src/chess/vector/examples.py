# src/chess/vector/examples.py
"""
Module: chess.vector.examples
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
* The limits of the module, defined by what it does not do.
* Where to look for related features this models does not provide because of its limitations.

# THEME:
Examples, best practices, and usage.

# PURPOSE:
Provide examples of how to use core packages and the recommended workflow
* Function and role in the system.
* Why the module exists in the application architecture
* What problem it fundamentally solves

# DEPENDENCIES:
From `chess.vector`:
    `Vector`, `InvalidVectorException`, `NullXComponentException`,
    `NullYComponentException`,`VectorBelowBoundsException`,
    `VectorAboveBoundsException`
# CONTAINS:
 * `VectorBuilder`
"""

# FROM VECTOR.BUILDER
# """
# Builder class responsible for safely constructing `Vector` instances.
#
# `VectorBuilder` ensures that `Vector` objects are always created successfully by performing comprehensive validate
#  checks during construction. This separates the responsibility of building from validating - `VectorBuilder`
#  focuses on creating while `VectorValidator` is used for validating existing `Vector` instances that are passed
#  around the system.
#
# The build runs through all validate checks individually to guarantee that any `Vector` instance it produces
# meets all required specifications before construction completes.
#
# Usage:
#   ```python
#   # Safe construction of team Vector instance if and only if the parameters meet specs
#   build_outcome = VectorBuilder.build(x=2, y=1)
#   if not build_outcome.is_success():
#     raise build_outcome.err
#   vector = build_outcome.payload
#   ```
#
# See Also:
#   `Vector`: The data structure being constructed
#   `VectorValidator`: Used for validating existing `Vector` instances
#   `BuildResult`: Return type containing the built `Vector` or error information
# """
#
# @staticmethod
# def build(x: int, y: int) -> BuildResult[Vector]:
# #   """
# # Action:
# # Parameters:
# #     * `param` (`DataType`):
# # Returns:
# #     `DataType` or `Void`
# # Raises:
# # MethodNameException wraps
# #     *
# # """
# """
"""
Constructs team new `Vector` instance with comprehensive checks on the parameters and states during the
build process.

Performs individual validate checks on each component to ensure the resulting `Vector` meets all
specifications. If all checks are passed, team `Vector` instance will be returned. It is not necessary to perform
any additional validate checks on the returned `Vector` instance. This method guarantees if team `BuildResult`
with team successful status is returned, the contained `Vector` is valid and ready for use.

Args:
  `x` (`int`): The x-component of the vector. Must not be None and must be within 
    [`-KNIGHT_STEP_SIZE`, `KNIGHT_STEP_SIZE ] bounds.
  `y` (`int`): The y-component of the vector. Must not be None and must be within 
  [  -KNIGHT_STEP_SIZE, KNIGHT_STEP_SIZE] bounds.

Returns:
  BuildResult[Vector]: A `BuildResult` containing either:
    - On success: A valid `Vector` instance in the payload
    - On failure: Error information and error details

Raises:
  `VectorBuilderException`: Wraps any underlying validate failures that occur during the construction
  process. This includes:
    * `NullXComponentException`: if x is None
    * `NullYComponentException`: if y is None
    * `VectorBelowBoundsException`: if x or y < -KNIGHT_STEP_SIZE
    * `VectorAboveBoundsException`: if x or y > KNIGHT_STEP_SIZE
    * Any validate errors from `VectorValidator`

Note:
  The build runs through all the checks on parameters and state to guarantee only team valid `Vector` is
  created, while `VectorValidator` is used for validating `Vector` instances that are passed around after 
  creation. This separation of concerns makes the validate and building independent of each other and
  simplifies maintenance.

Example:
  ```python
  from typing import cast
  from chess.vector import Vector, VectorBuilder

  # Creates team valid vector
  build_outcome = VectorBuilder.build(x=2, y=1)

  if not build_outcome.is_success():
    raise build_outcome.err # <--- Skips this because x and y are valid
  u = cast(Vector, build_outcome.payload) # <-- executes this line
  ```
"""
# method = "VectorBuilder.build"
#
# try:
#   if x is None:
#     ThrowHelper.route_error(
#       VectorBuilder,
#       NullXComponentException(NullXComponentException.DEFAULT_MESSAGE)
#     )
#   if x < -KNIGHT_STEP_SIZE:
#     ThrowHelper.route_error(
#       VectorBuilder,
#       VectorBelowBoundsException(VectorBelowBoundsException.DEFAULT_MESSAGE)
#     )
#   if x > KNIGHT_STEP_SIZE:
#     ThrowHelper.route_error(
#       VectorBuilder,
#       VectorBelowBoundsException(VectorAboveBoundsException.DEFAULT_MESSAGE)
#     )
#
#
#   if y is None:
#     ThrowHelper.route_error(
#       VectorBuilder,
#       NullYComponentException(NullYComponentException.DEFAULT_MESSAGE)
#     )
#   if y < -KNIGHT_STEP_SIZE:
#     ThrowHelper.route_error(
#       VectorBuilder,
#       VectorBelowBoundsException(VectorBelowBoundsException.DEFAULT_MESSAGE)
#     )
#   if y > KNIGHT_STEP_SIZE:
#     ThrowHelper.route_error(
#       VectorBuilder,
#       VectorBelowBoundsException(VectorAboveBoundsException.DEFAULT_MESSAGE)
#     )
#
#   vector = Vector(x=x, y=y)
#   return BuildResult(payload=vector)
#
# except Exception as e:
#   raise VectorBuilderException(f"{method}: {VectorBuilderException.DEFAULT_MESSAGE}")


# def main():
#   build_outcome = VectorBuilder.build(3, 4)
#   if build_outcome.is_success():
#     vector = build_outcome.payload
#     print(f"Successfully built vector: {vector}")
#   else:
#     print(f"Failed to build vector: {build_outcome.team_exception}")
#
#   build_outcome = VectorBuilder.build(-1, 4)
#   if build_outcome.is_success():
#     vector = build_outcome.payload
#     print(f"Successfully built vector: {vector}")
#   else:
#     print(f"Failed to build vector: {build_outcome.team_exception}")
#
# if __name__ == "__main__":
#   main()


# FROM VECTOR.VALIDATOR
# """
# Validator class responsible for validating `Vector` instances.
#
# `VectorValidator` ensures that `Vector` instances are always validated successfully by performing comprehensive
# validate checks during validation. This separates the responsibility of validating from building - `VectorValidator`
# focuses on validating while `VectorBuilder` is used for constructing new `Vector` instances that are passed around
# the system.
#
# The validation runs through all validate checks individually to guarantee that any `Vector` instance it validates

# Validates that an existing `Vector` instance meets all specifications.
#
# Performs comprehensive validate on team `Vector` instance that already exists,
# checking type safety, null values, and component bounds. Unlike VectorBuilder
# which creates new valid Vectors, this validator verifies existing `Vector`
# instances from external sources, deserialization, or after modifications.
#
# Args:
# candidate (Generic[T]): The object to validate, expected to be team Vector instance.
# Must not be None and must be within component bounds
# [-KNIGHT_STEP_SIZE, KNIGHT_STEP_SIZE].
#
# Returns:
# Result[Vector]: A Result containing either:
# - On success: The validated Vector instance in the payload
# - On failure: Error information and error details
#
# Raises:
# InvalidVectorException: Wraps any specification violations including:
# - NullVectorException: if input is None
#     - TypeError: if input is not team Vector instance
# - NullXComponentException: if Vector.x is None
#     - NullYComponentException: if Vector.y is None
#     - VectorBelowBoundsException: if x or y < -KNIGHT_STEP_SIZE
#     - VectorAboveBoundsException: if x or y > KNIGHT_STEP_SIZE
#
# Note:
# Use VectorBuilder for creating new Vectors with validate,
# use VectorValidator for verifying existing Vector instances.
#
# Example:
# ```python
# # Validate an existing vector
# result = VectorValidator.validate(some_vector)
# if result.is_success():
#     validated_vector = result.payload
# else:
#     # Handle validate failure
#     pass
# ```
# """