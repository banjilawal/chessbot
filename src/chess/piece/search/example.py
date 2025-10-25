# src/chess/discovery/checker.py
"""
Module: chess.discovery.discovery
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
***Limitation 1***: No validator, error checking is performed in `Checker` class. Using the class directly instead of
  its CRUD interfaces goes against recommended usage.

***Limitation 2***: There is no guarantee properly created `Checker` objects released by the module will satisfy client
    requirements. Clients are responsible for ensuring a `DiscoveryBuilder` product will not fail when used. Products
    from `DiscoveryBuilder` --should-- satisfy `DiscoveryValidator` requirements.

**Related Features**:
    Authenticating existing discoverys -> See DiscoveryValidator, module[chess.discovery.validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data Holding, Coordination, Performance

**Design Concepts**:
    Separating object creation from object usage.
    Keeping constructors lightweight

# PURPOSE:
---------
1. Putting all the steps and logging into one place makes modules using `Checker` objects cleaner and easier to follow.

***Satisfies***: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
    `BuildResult`, `Builder`, `LoggingLevelRouter`, `ChessException`, `NullException`, `BuildFailedException`
    `IdValidator`, `NameValidator`

From `chess.discovery`:
    `Checker`, `NullDiscovery`, `DiscoveryBuildFailedException`, `DiscoverySchema`

From `chess.commander`:
  `Commander`, `CommanderValidator`,

From `chess.piece`:
  `Piece`

# CONTAINS:
----------
 * `Checker`
"""