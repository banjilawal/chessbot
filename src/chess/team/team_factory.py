# from chess.common.config import ChessPieceConfig
# from chess.common.emitter import id_emitter
# from chess.player.player import Player
# from podscape.constants import PodscapeColor
#
#
# def TeamBuilder():
#
#     def __init__(self):
#         pass
#
#     def build_team(self, team_id: int, team_color: PodscapeColor) -> P;ayer:
#         player = Player(team_id=team_id, color=team_color)
#         team.piece_registry[ChessPieceConfig.PAWN.name] = get_pawn_dictionary(team)
#         team.piece_registry[ChessPieceConfig.KNIGHT.name] = get_knight_dictionary(team)
#         team.piece_registry[ChessPieceConfig.BISHOP.name] = get_bishop_dictionary(team)
#         team.piece_registry[ChessPieceConfig.ROOK.name] = get_castle_dictionary(team)
#         team.piece_registry[ChessPieceConfig.QUEEN.name] = get_queen_dictionary(team)
#         team.piece_registry[ChessPieceConfig.KING.name] = get_king_dictionary(team)
#
#         return team
#
#
#     def get_pawn_dictionary(team: Team):
#         base_name = team.color + "_" + ChessPieceConfig.PAWN.name
#         rank = ChessPieceConfig.PAWN.rank()
#         pawn_dict = {}
#
#         for i in ChessPieceConfig.PAWN.number_per_team():
#             key = i + 1
#             name = base_name + "_" + key
#             rank = i + 1
#             chess_piece_id = id_emitter.piece_id()
#             pawn_dict[key] = Pawn(chess_piece_id=chess_piece_id, name=name, team=team, rank=rank)
#         return pawn_dict
#
#
#     def get_knight_dictionary(team: Team):
#         base_name = team.color + "_" + ChessPieceConfig.KNIGHT.name
#         rank = ChessPieceConfig.KNIGHT.rank()
#         knight_dict = {}
#
#         for i in ChessPieceConfig.KNIGHT.number_per_team():
#             key = i + 1
#             name = base_name + "_" + key
#             chess_piece_id = id_emitter.piece_id()
#             knight_dict[key] = Knight(chess_piece_id=chess_piece_id, name=name, team=team, rank=rank)
#         return knight_dict
#
#     def get_bishop_dictionary(team: Team):
#         base_name = team.color + "_" + ChessPieceConfig.BISHOP.name
#         rank = ChessPieceConfig.BISHOP.rank()
#         bishop_dict = {}
#
#         for i in ChessPieceConfig.BISHOP.number_per_team():
#             key = i + 1
#             name = base_name + "_" + key
#             chess_piece_id = id_emitter.piece_id()
#             bishop_dict[key] = Bishop(chess_piece_id=chess_piece_id, name=name, team=team, rank=rank)
#         return bishop_dict
#
#
#     def get_castle_dictionary(team: Team):
#         base_name = team.color + "_" + ChessPieceConfig.ROOK.name
#         rank = ChessPieceConfig.ROOK.rank()
#         castle_dict = {}
#
#         for i in ChessPieceConfig.ROOK.number_per_team():
#             key = i + 1
#             name = base_name + "_" + key
#             chess_piece_id = id_emitter.piece_id()
#             castle_dict[key] = Rook(chess_piece_id=chess_piece_id, name=name, team=team, rank=rank)
#         return castle_dict
#
#
#     def get_queen_dictionary(team: Team):
#         base_name = team.color + "_" + ChessPieceConfig.QUEEN.name
#         rank = ChessPieceConfig.QUEEN.rank()
#         queen_dict = {}
#
#         for i in ChessPieceConfig.QUEEN.number_per_team():
#             key = i + 1
#             name = base_name + "_" + key
#             chess_piece_id = id_emitter.piece_id()
#             queen_dict[key] = Bishop(chess_piece_id=chess_piece_id, name=name, team=team, rank=rank)
#         return queen_dict
#
#
#     def get_king_dictionary(team: Team):
#         base_name = team.color + "_" + ChessPieceConfig.KING.name
#         rank = ChessPieceConfig.ROOK.rank()
#         king_dict = {}
#
#         for i in ChessPieceConfig.KING.number_per_team():
#             key = i + 1
#             name = base_name + "_" + key
#             chess_piece_id = id_emitter.piece_id()
#             king_dict[key] = King(chess_piece_id=chess_piece_id, name=name, team=team, rank=rank)
#         return king_dict