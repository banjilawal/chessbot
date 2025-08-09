`Engine Package (engine)

This document outlines the planned architecture for the engine package, which provides 
the core decision-making logic for the CyberneticOwner. The goal is to create a modular
and extensible system for finding and selecting optimal moves.
Table of Contents
    Core Components
        The Engine
        ExplorationMaster
        Scout
        ScoutReport
        ScoutReportSorter
        TargetSelector
    Further Considerations

Core Components
<a name="the-engine"></a>The Engine
e Engine class will serve as the primary interface between the CyberneticOwner and the 
chess logic. Its main responsibility is to orchestrate the entire decision-making 
process. The CyberneticOwner will simply call a method on the Engine to get a 
recommended move, and the Engine will handle all the underlying steps.
Key Responsibilities:
    Initiate the scouting process by delegating to the ExplorationMaster.
    Receive the sorted reports.
    Delegate the final move selection to the TargetSelector.
    Return the chosen ChessPiece and Coordinate to the CyberneticOwner.
<a name="explorationmaster"></a>ExplorationMaster


The ExplorationMaster is responsible for sending every free ChessPiece on the team on a
scouting mission. It will have a single public method that initiates this process for 
all pieces.
Key Responsibilities:
    Iterate through all a team's pieces.
    For each piece, create a Scout instance.
    Call the survey() method on each Scout.
    Collect all the resulting ScoutReport objects into a single list.
<a name="scout"></a>Scout

The Scout class represents a single ChessPiece on a scouting mission. Its purpose is to perform a survey of its possible moves and package the results into a report. This abstraction allows the main engine to work with a higher-level concept than individual pieces.
Key Responsibilities:
    Receive a ChessPiece during initialization.
    Contain a single public method, survey(), which delegates to the static Explorer class.
    Return a ScoutReport object.

<a name="scoutreport"></a>ScoutReport

This is a data-only class (dataclass is a good candidate) that encapsulates the findings of a single Scout's mission.
Key Attributes:
    id: A unique identifier for the report.
    scout: The ChessPiece that performed the survey.
    locations: A list of Coordinate objects representing the piece's legal moves.

Note on Hashing: The __hash__ method should be updated to return hash((self._id, self._scout.id)).
<a name="scoutreportsorter"></a>ScoutReportSorter

This component will be responsible for taking all the ScoutReport objects and sorting them based on a predefined set of criteria. This sorting is crucial for the TargetSelector to efficiently find the best move.
Key Responsibilities:
    Receive a list of ScoutReport objects.
    Apply sorting logic (e.g., by the number of locations, by potential capture value, by potential threat).
    Return a new, sorted list of ScoutReport objects.

<a name="targetselector"></a>TargetSelector

The TargetSelector is the final step in the decision-making process. It takes the sorted ScoutReports and picks the most desirable destination to move to. If the first choice is invalid (for any reason), it proceeds down the list until a valid move is found.
Key Responsibilities:
    Receive a sorted list of ScoutReport objects.
    Iterate through the reports.
    For each report, iterate through its locations.
    Select the first valid move and return the associated ChessPiece and Coordinate.

Further Considerations
<a name="further-considerations"></a>Explorer

As we discussed, the Explorer class will be a static utility. It will simply 
take a ChessPiece and MapService and return a list of Coordinate objects, 
simplifying the Scout's job. This keeps the Explorer focused on the low-level 
logic of finding valid paths, without any knowledge of the scouting or reporting
process.`