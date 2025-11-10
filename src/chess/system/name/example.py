# chess/system/visitor_name/example.py

"""
Module: chess.system.visitor_name.example
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

# src/chess/system/visitor_name/exception.py

"""
Module: chess.system.visitor_name.exception
Author: Banji Lawal
Created: 2025-09-17
Updated: 2025-10-10
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` integrity requirement.
  2. A satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module's only covers exceptions raised by `NameValidator`;

# SECTION 3: Limitations
  1. Does not provide logic for fixing the errors or causing the rollback_exception being raised.
       `NameValidator` is responsible for the logic which raises these exceptions.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. Discoverability.
  3. Encapsulations.

# SECTION 5- Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.


# SECTION 6 - Feature Delivery Mechanism:
1. Exceptions specific to verifying names.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `ValidationException`, `BlankStringException`, `NullException`

# SECTION 8 - Contains:
See the list of exceptions in the `__all__` list following (e.g., `InvalidNameException`,`NullNameException`).
"""