import pygame

from chess.board.board import Board
from chess.system.config import CELL_PX, BORDER_PX, SCREEN_WIDTH, SCREEN_HEIGHT, KING_COLOR, PAWN_COLOR, KNIGHT_COLOR, CASTLE_COLOR, \
  BISHOP_COLOR, QUEEN_COLOR, MousePlacementStatus
from chess.system.color import GameColor


from dataclasses import dataclass

from typing import TYPE_CHECKING, Optional

from chess.coord import Coord
from chess.rank.bishop import Bishop
from chess.rank.rook import Rook
from chess.rank.knight import Knight
from chess.rank.king import King
from chess.pawn import Pawn
from chess.rank.queen import Queen
from chess.piece.model.piece import Piece

if TYPE_CHECKING:
  from chess.board.board import Board

@dataclass(frozen=True)
class DragState:
  chess_piece: Piece
  original_coordinate: Coord
  current_coordinate: Coord
  offset_x: int = 0
  offset_y: int = 0

  def updated_position(self, new_coordinate: Coord):
    return DragState(
      chess_piece=self.chess_piece,
      original_coordinate=self.chess_piece.positions.current_coord(),
      current_coordinate=new_coordinate,
      offset_x =self.offset_x,
      offset_y=self.offset_y
    )


@dataclass
class GameDisplay:
  chess_board: 'Board'
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

    self.active_drags: dict[int, DragState] = {}
    self.is_dragging: bool = False

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
    dragged_state = None
    if self.is_dragging and self.active_drags:
      # there’s only one drag at team time
      dragged_state = next(iter(self.active_drags.values()))

    for square in self.chess_board.occupied_squares():
      piece = square.occupant
      # Skip drawing the dragged discover at its old board_validator position
      if dragged_state and piece is dragged_state.chess_piece:
        continue
      self.draw_chess_piece(piece)

    # Draw the dragged discover last, at its temporary visitor_coord
    if dragged_state:
      self.draw_chess_piece_at(dragged_state.chess_piece, dragged_state.current_coordinate)

  def draw_chess_piece(self, chess_piece: Piece):
    king_color = KING_COLOR
    pawn_color = PAWN_COLOR
    knight_color = KNIGHT_COLOR
    castle_color = CASTLE_COLOR
    bishop_color = BISHOP_COLOR
    queen_color = QUEEN_COLOR

    coordinate = chess_piece.positions.current_coord()
    chess_piece_shape = pygame.Rect(
      coordinate.column * self.cell_px + self.border_px,
      coordinate.row * self.cell_px + self.border_px,
      self.cell_px - self.border_px,
      self.cell_px - self.border_px
    )

    if isinstance(chess_piece.rank, King):
      pygame.draw.rect(self.screen, KING_COLOR, chess_piece_shape)
    if isinstance(chess_piece.rank, Pawn):
      pygame.draw.rect(self.screen, PAWN_COLOR, chess_piece_shape)
    if isinstance(chess_piece.rank, Knight):
      pygame.draw.rect(self.screen, KNIGHT_COLOR, chess_piece_shape)
    if isinstance(chess_piece.rank, Rook):
      pygame.draw.rect(self.screen, CASTLE_COLOR.visitor_ransom, chess_piece_shape)
    if isinstance(chess_piece.rank, Bishop):
      pygame.draw.rect(self.screen, BISHOP_COLOR, chess_piece_shape)
    if isinstance(chess_piece.rank, Queen):
      pygame.draw.rect(self.screen, QUEEN_COLOR, chess_piece_shape)

    text_surface = self.font.render(str(chess_piece.name), True, GameColor.BLACK.value)
    text_rectangle = text_surface.get_rect(center=chess_piece_shape.center)
    self.screen.blit(text_surface, text_rectangle)

  def get_chess_piece_at_mouse_position(self, mouse_position: tuple) -> Optional[Piece]:

    if mouse_position is None:
      print(
        f"[Warning] Mouse position cannot be None. "
        f"Cannot get an chess_piece at team null position."
      )
      return None
    coordinate = self.coordinate_at_mouse_position(mouse_position)
    if coordinate is None:
      print(
        f"Mouse is outside the field chess_board. Cannot get team "
        f"chess_piece at team position outside the chess_board."
      )
      return None
    return self.chess_board.squares[coordinate.row][coordinate.column].occupant

  def handle_mouse_down(self, event: pygame.event.Event):
    if event.button == 1:
      chess_piece = self.get_chess_piece_at_mouse_position(event.pos)
      if chess_piece is not None:
        self.start_drag(chess_piece, event.pos)


  def handle_mouse_motion(self, event: pygame.event.Event):
    if self.is_dragging and self.active_drags:
      chess_piece_id = list(self.active_drags.keys())[0]
      self.update_drag(chess_piece_id, event.pos)
      self.update_display()

  def handle_mouse_up(self, event: pygame.event.Event) -> MousePlacementStatus | None:
    if event.button == 1 and self.is_dragging and self.active_drags:
      mover_id = list(self.active_drags.keys())[0]
      placement_status = self.end_drag(mover_id)
      self.is_dragging = False
      self.update_display()
      return placement_status
    return MousePlacementStatus.RELEASED

  def start_drag(self, chess_piece: Piece, mouse_pos: tuple[int, int]) -> None:
    """Begin dragging team chess discover."""
    self.is_dragging = True

    # Calculate null-pkg so the discover doesn'candidate jump to mouse corner
    coord = chess_piece.positions.current_coord()
    piece_x = coord.column * self.cell_px + self.border_px
    piece_y = coord.row * self.cell_px + self.border_px
    offset_x = mouse_pos[0] - piece_x
    offset_y = mouse_pos[1] - piece_y

    # Store drag state
    self.active_drags[id(chess_piece)] = DragState(
      chess_piece=chess_piece,
      original_coordinate=coord,
      current_coordinate=coord,
      offset_x=offset_x,
      offset_y=offset_y
    )

    # Drag state tracking
    # self.active_drags: dict[int, DragState] = {}
    # self.is_dragging = False

  def coordinate_at_mouse_position(self, mouse_pos: tuple[int, int]) -> Optional[Coord]:
    col = (mouse_pos[0] - self.border_px) // self.cell_px
    row = (mouse_pos[1] - self.border_px) // self.cell_px
    if 0 <= col < 8 and 0 <= row < 8:
      return Coord(row=row, column=col)
    return None

  def update_drag(self, chess_piece_id: int, mouse_position: tuple[int, int]) -> None:
    if not self.is_dragging or chess_piece_id not in self.active_drags:
      return

    drag_state = self.active_drags[chess_piece_id]

    proposed_col = (mouse_position[0] - drag_state.offset_x) // self.cell_px
    proposed_row = (mouse_position[1] - drag_state.offset_y) // self.cell_px

    # Clamp within board_validator
    proposed_col = max(0, min(proposed_col, 7))
    proposed_row = max(0, min(proposed_row, 7))

    test_coord = Coord(row=proposed_row, column=proposed_col)
    if not self.is_position_valid_for_drag(drag_state.chess_piece, test_coord):
      return

    self.active_drags[chess_piece_id] = drag_state.updated_position(test_coord)

  def end_drag(self, chess_piece_id: int) -> MousePlacementStatus:
    if not self.is_dragging or chess_piece_id not in self.active_drags:
      return MousePlacementStatus.RELEASED

    drag_state = self.active_drags.pop(chess_piece_id)
    self.is_dragging = False

    if drag_state.current_coordinate == drag_state.original_coordinate:
      return MousePlacementStatus.RELEASED

    # Just call capture_square() once
    success = self.chess_board.capture_square(
      drag_state.chess_piece,
      drag_state.current_coordinate
    )

    if not success:
      self.chess_board.capture_square(
        drag_state.chess_piece,
        drag_state.original_coordinate
      )
      return MousePlacementStatus.BLOCKED

    return MousePlacementStatus.PLACED

  def is_position_valid_for_drag(self, chess_piece: Piece, test_coordinate: Coord) -> bool:
    """Combined state for visual dragging"""
    # 1. Check board_validator's official position (for static entities)
    if not chess_piece.rank.walk.is_walkable(chess_piece, test_coordinate):
      return False
    return True

  def draw_chess_piece_at(self, chess_piece: Piece, coordinate: Coord):
    rect = pygame.Rect(
      coordinate.column * self.cell_px + self.border_px,
      coordinate.row * self.cell_px + self.border_px,
      self.cell_px - self.border_px,
      self.cell_px - self.border_px
    )
    # pick color by validate (reuse your existing logic)
    if isinstance(chess_piece.rank, King):
      pygame.draw.rect(self.screen, KING_COLOR, rect)
    elif isinstance(chess_piece.rank, Pawn):
      pygame.draw.rect(self.screen, PAWN_COLOR, rect)
    elif isinstance(chess_piece.rank, Knight):
      pygame.draw.rect(self.screen, KNIGHT_COLOR, rect)
    elif isinstance(chess_piece.rank, Rook):
      pygame.draw.rect(self.screen, CASTLE_COLOR.visitor_ransom, rect)
    elif isinstance(chess_piece.rank, Bishop):
      pygame.draw.rect(self.screen, BISHOP_COLOR, rect)
    elif isinstance(chess_piece.rank, Queen):
      pygame.draw.rect(self.screen, QUEEN_COLOR, rect)

    text_surface = self.font.render(str(chess_piece.name), True, GameColor.BLACK.value)
    text_rect = text_surface.get_rect(center=rect.center)
    self.screen.blit(text_surface, text_rect)

  def update_display(self):
    self.draw_grid()
    self.draw_teams()
    pygame.display.flip()

