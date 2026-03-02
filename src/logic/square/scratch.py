"""
 ROLE: Service, Lifecycle Management, Encapsulation, API layer.

 RESPONSIBILITIES:
 1.  Public facing Square microservice API.
 2.  Encapsulate integrity logic for Square instances in one extendable module.
 3.  Authoritative, single source of truth for Square state by providing single entry and exit points to Square
     lifecycle.

  PARENT:
     *   IntegrityService

  PROVIDES:
 None

  LOCAL ATTRIBUTES:
     *   SERVICE_NAME (str)
     *   token_visit_handler (TokenVisitHandler)
     *   collision_detector (SquareCollisionDetector)

  INHERITED ATTRIBUTES:
     *   See IntegrityService for inherited attributes.

  CONSTRUCTOR PARAMETERS:
     Local:
         *   token_visit_handler (TokenVisitHandler)
         *   collision_detector (SquareCollisionDetector)
     Inherited:
         *   See IntegrityService for inherited constructor parameters.

  LOCAL METHODS:
     *   begin_square_visit(square: Square, visitor: Token) -> UpdateResult[Square]
     *   end_square_visit(square: Square) -> DeletionResult[Token]

  INHERITED METHODS:
 None
 """