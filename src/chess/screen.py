from curses.textpad import rectangle

import pygame

from chess.board.board import ChessBoard
from chess.common.config import COLUMN_SIZE, ROW_SIZE, PYGAME_CAPTION, PYGAME_FONT, PYGAME_FONT_SIZE, SCREEN_COLOR, \
    CELL_COLOR, CELL_PX, BORDER_PX, SCREEN_WIDTH, SCREEN_HEIGHT, KING_COLOR, PAWN_COLOR, KNIGHT_COLOR, CASTLE_COLOR, \
    BISHOP_COLOR, QUEEN_COLOR
from chess.common.game_color import GameColor


from dataclasses import dataclass, field

import pygame
from typing import TYPE_CHECKING, Optional, cast, OrderedDict

from colorama.ansi import clear_line

from chess.geometry.coordinate.coordinate import Coordinate
from chess.rank.bishop_rank import BishopRank
from chess.rank.castle_rank import CastleRank
from chess.rank.knight_rank import KnightRank
from chess.rank.promotable.king_rank import KingRank
from chess.rank.promotable.pawn_rank import PawnRank
from chess.rank.queen_rank import QueenRank
from chess.token.chess_piece import ChessPiece

if TYPE_CHECKING:
    from chess.board.board import ChessBoard

@dataclass(frozen=True)
class DragState:
    chess_piece: ChessPiece
    original_coordinate: Coordinate
    current_coordinate: Coordinate
    offset_x: int = 0
    offset_y: int = 0

    def updated_position(self, new_coordinate: Coordinate):
        return DragState(
            chess_piece=self.chess_piece,
            original_coordinate=self.chess_piece.coordinate_stack.current_coordinate(),
            current_coordinate=new_coordinate,
            offset_x =self.offset_x,
            offset_y=self.offset_y
        )


@dataclass
class GameDisplay:
    chess_board: 'ChessBoard'
    cell_px: int = CELL_PX
    border_px: int = BORDER_PX
    screen_width: int = SCREEN_WIDTH
    screen_height: int = SCREEN_HEIGHT

    def __post_init__(self):
        self.screen_width = 8 * self.cell_px + self.border_px * 2
        self.screen_height = 8 * self.cell_px + self.border_px * 2

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("ChessBot")
        self.font = pygame.font.SysFont("monospace", 50)

    def draw_grid(self):
        screen_color = GameColor.DARK_GRAY_1.value
        self.screen.fill(screen_color)

        cell_color = GameColor.LIGHT_SAND.value
        opposite_cell_color = screen_color

        current_cell_color = cell_color
        previous_cell_color = cell_color
        for row in range(8):
            for col in range(8):
                cell_rect = pygame.Rect(
                    col * self.cell_px + self.border_px,
                    row * self.cell_px + self.border_px,
                    self.cell_px,
                    self.cell_px
                )

                cell = self.chess_board.squares[row][col]
                current_cell_color = cell_color if (row + col) % 2 == 0 else opposite_cell_color

                pygame.draw.rect(self.screen, current_cell_color, cell_rect)
                # Draw an outlined rectangle
                pygame.draw.rect(self.screen, GameColor.BLACK.value, cell_rect, 1)

    def draw_teams(self):
        for square in self.chess_board.occupied_squares():
            self.draw_chess_piece(square.occupant)

    def draw_chess_piece(self, chess_piece: ChessPiece):
        king_color = KING_COLOR
        pawn_color = PAWN_COLOR
        knight_color = KNIGHT_COLOR
        castle_color = CASTLE_COLOR
        bishop_color = BISHOP_COLOR
        queen_color = QUEEN_COLOR

        coordinate = chess_piece.coordinate_stack.current_coordinate()
        chess_piece_shape = pygame.Rect(
            coordinate.column * self.cell_px + self.border_px,
            coordinate.row * self.cell_px + self.border_px,
            self.cell_px - self.border_px,
            self.cell_px - self.border_px
        )

        if isinstance(chess_piece.rank, KingRank):
            pygame.draw.rect(self.screen, KING_COLOR, chess_piece_shape)
        if isinstance(chess_piece.rank, PawnRank):
            pygame.draw.rect(self.screen, PAWN_COLOR, chess_piece_shape)
        if isinstance(chess_piece.rank, KnightRank):
            pygame.draw.rect(self.screen, KNIGHT_COLOR, chess_piece_shape)
        if isinstance(chess_piece.rank, CastleRank):
            pygame.draw.rect(self.screen, CASTLE_COLOR.value, chess_piece_shape)
        if isinstance(chess_piece.rank, BishopRank):
            pygame.draw.rect(self.screen, BISHOP_COLOR, chess_piece_shape)
        if isinstance(chess_piece.rank, QueenRank):
            pygame.draw.rect(self.screen, QUEEN_COLOR, chess_piece_shape)

        text_surface = self.font.render(str(chess_piece.name), True, GameColor.BLACK.value)
        text_rectangle = text_surface.get_rect(center=chess_piece_shape.center)
        self.screen.blit(text_surface, text_rectangle)

    def get_chess_piece_at_mouse_position(self, mouse_position: tuple) -> Optional[ChessPiece]:

        if mouse_position is None:
            print(
                f"[Warning] Mouse position cannot be None. "
                f"Cannot get an chess_piece at a null position."
            )
            return None
        coordinate = self.coordinate_at_mouse_positon(mouse_position)
        if coordinate is None:
            print(
                f"Mouse is outside the field chess_board. Cannot get a "
                f"chess_piece at a position outside the chess_board."
            )
            return None
        return  self.chess_board.squares[coordinate.row][coordinate.column].occupant

    def handle_mouse_down(self, event: pygame.event.Event):
        if event.button == 1:
            chess_piece = self.get_chess_piece_at_mouse_position(event.position)
            if chess_piece is not None:
                self.start_drag(chess_piece, event.pos)


    def handle_mouse_motion(self, event: pygame.event.Event):
        if self.is_dragging and self.active_drags:
            mover_id = list(self.active_drags.keys())[0]
            self.update_drag(mover_id, event.pos)

    def handle_mouse_up(self, event: pygame.event.Event) -> PlacementStatus | None:
        if event.button == 1 and self.is_dragging and self.active_drags:
            mover_id = list(self.active_drags.keys())[0]
            placement_status = self.end_drag(mover_id)
            self.is_dragging = False
            return placement_status
        return PlacementStatus.RELEASED

    def start_drag(self, chess_piece: ChessPiece, mouse_position: tuple[int, int]) -> None:
        chess_piece.coordinate_stack.current_coordinate()
        self.active_drags[chess_piece.id] = DragState(
            chess_piece=chess_piece,
            original_coordinate=chess_piece.coordinate_stack.current_coordinate(),
            current_coordinate=chess_piece.coordinate_stack.current_coordinate(),
            offset_x=mouse_position[0] - (chess_piece.coordinate_stack.current_coordinate().column * self.cell_px),
            offset_y=mouse_position[1] - (chess_piece.coordinate_stack.current_coordinate().row * self.cell_px)
        )
        self.is_dragging = True
        print("chess_piece", chess_piece.id, "dragging started at", self.active_drags[chess_piece.id].original_coordinate)

    def update_display(self):
        self.draw_grid()
        self.draw_teams()
        pygame.display.flip()

# chess_board: ChessBoard
#     cell_px: int = 60
#     border_px: int = 2
#     screen_width: int = 800
#     screen_height: int = 800
# from dataclasses import dataclass, field
#
# import pygame
# from typing import TYPE_CHECKING, Optional, cast, OrderedDict
#
#
# from chess.board.board import ChessBoard
# from chess.common.config import COLUMN_SIZE, ROW_SIZE
# from chess.common.game_color import GameColor
# from chess.geometry.coordinate.coordinate import Coordinate
# from chess.rank.bishop_rank import BishopRank
# from chess.rank.castle_rank import CastleRank
# from chess.rank.knight_rank import KnightRank
# from chess.rank.promotable.king_rank import KingRank
# from chess.rank.promotable.pawn_rank import PawnRank
# from chess.rank.queen_rank import QueenRank
# from chess.rank.rank import Rank
#
# if TYPE_CHECKING:
#
# @dataclass(frozen=True)
# class DragState:
#     rank: Rank
#     original_coordinate: Coordinate
#     current_coordinate: Coordinate
#     offset_x: int = 0
#     offset_y: int = 0
#
#     def with_updated_position(self, new_coordinate: Coordinate) -> 'DragState':
#         return DragState(
#             rank=self.rank,
#             original_coordinate=self.original_coordinate,
#             current_coordinate=new_coordinate,
#             offset_x=self.offset_x,
#             offset_y=self.offset_y
#         )
#
# @dataclass
# class ChessBoardDisplay:
#     chess_board: ChessBoard
#     cell_px: int = 60
#     border_px: int = 2
#     screen_width: int = 800
#     screen_height: int = 800
#
#     active_drags: OrderedDict[int, DragState] = field(default_factory=OrderedDict)
#     is_dragging: bool = False
#
#     def __post_init__(self):
#         self.screen_width = COLUMN_SIZE * self.cell_px + self.border_px * 2
#         self.screen_height = ROW_SIZE * self.cell_px + self.border_px * 2
#
#         pygame.init()
#         self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
#         pygame.display.set_caption("Podscape")
#         self.font = pygame.font.SysFont("monospace", 30)
#
#     def load_chess_piece_images(self):
#         import os
#
#         base_path = "assets"
#
#         chess_pieces = [
#             "white-castle", "white-knight", "white-bishop", "white-king", "white-queen", "white-captor"
#             "black-castle", "black-knight", "black-bishop", "black-king", "black-queen", "black-captor"
#         ]
#
#         # for name in chess_pieces:
#         #     try:
#         #         path = os.path.join(base_path, f"{name}.png")  # or .svg if you’re using pygame-svg
#         #         image = pygame.image.load(path)
#         #         scaled = pygame.transform.scale(image, (self.cell_px, self.cell_px))  # auto-scale to square
#         #         self.piece_images[name] = scaled
#         #     except Exception as e:
#         #         print(f"⚠️ Failed to load image {name}: {e}")
#
#
#     def draw_grid(self):
#         screen_color = GameColor.DARK_GRAY_1.value
#         self.screen.fill(screen_color)
#
#         cell_color = GameColor.LIGHT_SAND.value
#         opposite_cell_color = screen_color
#
#         current_cell_color = cell_color
#         previous_cell_color = cell_color
#         for row in range(ROW_SIZE):
#             for col in range(COLUMN_SIZE):
#                 cell_rect = pygame.Rect(
#                     col * self.cell_px + self.border_px,
#                     row * self.cell_px + self.border_px,
#                     self.cell_px,
#                     self.cell_px
#                 )
#
#                 square = self.chess_board.squares[row][col]
#                 current_cell_color = cell_color if (row + col) % 2 == 0 else opposite_cell_color
#
#                 pygame.draw.rect(self.screen, current_cell_color, cell_rect)
#                 # Draw an outlined rectangle
#                 pygame.draw.rect(self.screen, GameColor.BLACK.value, cell_rect, 1)

    # def draw_all_entities(self):
    #     # First draw chess_board entities
    #     for entity in self.board.entities:
    #         self.draw_entity(entity)
    #
    #     # Then draw any entities being dragged at their current position
    #     for drag_state in self.active_drags.values():
    #         rect = pygame.Rect(
    #             drag_state.current_coordinate.column * self.cell_px + self.border_px,
    #             drag_state.current_coordinate.row * self.cell_px + self.border_px,
    #             drag_state.chess_piece.dimension.length * self.cell_px - self.border_px,
    #             drag_state.rank.dimension.height * self.cell_px - self.border_px
    #         )
    #         pygame.draw.rect(self.screen, GameColor.OLIVE.value, rect)
    #         text_surface = self.font.render(str(drag_state.mover.mover_id), True, GameColor.BLACK.value)
    #         text_rect = text_surface.get_rect(center=rect.center)
    #         self.screen.blit(text_surface, text_rect)
    #
    # def draw_entity(self, entity: 'GridEntity'):
    #     """Draw p single mover on the chess_board"""
    #     if entity is None:
    #         print("[Warning] Entity cannot be None. Cannot draw p null mover to the screen.")
    #         return
    #     if entity.top_left_coordinate is None:
    #         print("[Warning] Entity has no top_left_coordinate. Cannot draw an mover without p top_left_coordinate to the screen.")
    #         return
    #
    #     king_color = GameColor.OLIVE.value
    #     pawn_color = GameColor.DEEP_ORANGE.value
    #     knight_color = GameColor.CERULEAN.value
    #     bishop_color = GameColor.INDIGO.value
    #     castle_color = GameColor.SALMON
    #     queen_color = GameColor.SILVER.value
    #     # print(f"Drawing mover {mover.mover_id_counter} at top_left_coordinate {mover.top_left_coordinate}")
    #     # Calculate position and dimensions
    #     rect = pygame.Rect(
    #         rank.coordinate.column * self.cell_px + self.border_px,
    #         rank.top_left_coordinate.row * self.cell_px + self.border_px,
    #         entity.dimension.length * self.cell_px - self.border_px,
    #         entity.dimension.height * self.cell_px - self.border_px
    #     )
    #     # Draw the mover (fixed the width parameter)
    #
    #     if isinstance(entity, KingRank):
    #         pygame.draw.rect(self.screen, king_color, rect)
    #
    #     if isinstance(entity, PawnRank):
    #         pygame.draw.rect(self.screen, pawn_color, rect)
    #
    #     if isinstance(entity, CastleRank):
    #         pygame.draw.rect(self.screen, castle_color, rect)
    #
    #     if isinstance(entity, KnightRank):
    #         pygame.draw.rect(self.screen, knight_color, rect)
    #
    #     if isinstance(entity, BishopRank):
    #         pygame.draw.rect(self.screen, bishop_color, rect)
    #
    #     if isinstance(entity, QueenRank):
    #         pygame.draw.rect(self.screen, queen_color, rect)

        # Draw mover ID
        # text_surface = self.font.render(str(entity.mover_id), True, GameColor.BLACK.value)
        # text_rect = text_surface.get_rect(center=rect.center)
        # self.screen.blit(text_surface, text_rect)
    #
    # def get_entity_at_mouse_position(self, mouse_position: tuple) -> Optional['GridEntity']:
    #     if mouse_position is None:
    #         print("[Warning] Mouse position cannot be None. Cannot get an mover at p null position.")
    #         return None
    #     coordinate = self.grid_coordinate_at_mouse_position(mouse_position)
    #     if coordinate is None:
    #         print("Mouse is outside the arena chess_board. Cannot get an mover at p position outside the chess_board.")
    #         return None
    #     return self.board.cells[coordinate.row][coordinate.column].occupant
    #
    # def handle_mouse_down(self, event: pygame.event.Event):
    #     if event.button == 1:  # Left mouse button
    #         entity = self.get_entity_at_mouse_position(event.pos)
    #         if entity is not None:
    #             self.start_drag(entity, event.pos)
    #
    # def handle_mouse_motion(self, event: pygame.event.Event):
    #     if self.is_dragging and self.active_drags:
    #         mover_id = list(self.active_drags.keys())[0]
    #         self.update_drag(mover_id, event.pos)
    #
    # def handle_mouse_up(self, event: pygame.event.Event) -> PlacementStatus | None:
    #     if event.button == 1 and self.is_dragging and self.active_drags:
    #         mover_id = list(self.active_drags.keys())[0]
    #         placement_status = self.end_drag(mover_id)
    #         self.is_dragging = False
    #         return placement_status
    #     return PlacementStatus.RELEASED
    #
    # def start_drag(self, mover: Mover, mouse_position: tuple[int, int]) -> None:
    #     self.active_drags[mover.mover_id] = DragState(
    #         mover=mover,
    #         original_coordinate=mover.top_left_coordinate,
    #         current_coordinate=mover.top_left_coordinate,
    #         offset_x=mouse_position[0] - (mover.top_left_coordinate.column * self.cell_px),
    #         offset_y=mouse_position[1] - (mover.top_left_coordinate.row * self.cell_px)
    #     )
    #     self.is_dragging = True
    #     print("mover", mover.mover_id, "dragging started at", self.active_drags[mover.mover_id].original_coordinate)
    #
    # def update_drag(self, mover_id: int, mouse_position: tuple[int, int]) -> None:
    #     if not self.is_dragging or mover_id not in self.active_drags:
    #         return
    #
    #     drag_state = self.active_drags[mover_id]
    #     mover = drag_state.mover
    #
    #     # Calculate proposed chessboard position
    #     proposed_column = (mouse_position[0] - drag_state.offset_x) // self.cell_px
    #     proposed_row = (mouse_position[1] - drag_state.offset_y) // self.cell_px
    #
    #     # Boundary checks
    #     new_column = max(0, min(proposed_column, self.board.dimension.length - mover.dimension.length))
    #     proposed_row = max(0, min(proposed_row, self.board.dimension.height - mover.dimension.height))
    #
    #     # Enforce HorizontalMover constraint
    #     if isinstance(mover, HorizontalMover):
    #         proposed_row = drag_state.original_coordinate.row
    #
    #     if isinstance(mover, VerticalMover):
    #         proposed_column = drag_state.original_coordinate.column
    #
    #     # Check against both visual and chess_board states
    #     test_coordinate = GridCoordinate(row=proposed_row, column=new_column)
    #     if not self.is_position_valid_for_drag(mover, test_coordinate):
    #         return
    #     try:
    #         new_coord = GridCoordinate(row=proposed_row, column=proposed_column)
    #         self.active_drags[mover_id] = drag_state.with_updated_position(new_coord)
    #     except ValueError as e:
    #         print(f"Invalid coordinate: {e}")
    #
    # def is_position_valid_for_drag(self, mover: Mover, test_coordinate: GridCoordinate) -> bool:
    #     """Combined check for visual dragging"""
    #     # 1. Check chess_board's official position (for static entities)
    #     if not self.board.can_entity_move_to_cells(mover, test_coordinate):
    #         return False
    #
    #     # 2. Check against other dragged entities
    #     for other_id, other_state in self.active_drags.items():
    #         if other_id == mover.mover_id:
    #             continue
    #         other_cells = self.get_occupied_cells(
    #             other_state.current_coordinate.row,
    #             other_state.current_coordinate.column,
    #             other_state.mover.dimension
    #         )
    #
    #         if self.get_occupied_cells(test_coordinate.row, test_coordinate.columnl, mover.dimension) & other_cells:
    #             return False
    #     return True
