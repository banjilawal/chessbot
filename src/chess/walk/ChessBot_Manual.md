# ChessBot Game Manual

## 📖 Introduction
ChessBot is an advanced chess game and engine built in Python, featuring a modular architecture and an interactive Pygame interface. 
It supports both human players and AI-controlled opponents, with a strong focus on clean separation of game rules, board management, and UI.

---

## 🎮 How to Play
1. **Objective**: Checkmate your opponent's king while protecting your own.
2. **Setup**: Standard chess rules and piece placement apply.
3. **Turns**: Players alternate moves. Each player can move one piece per turn.
4. **Capturing**: Move your piece onto a square occupied by an opponent's piece to capture it.
5. **Special Rules**:
   - **Pawn Promotion**: Pawns reaching the opponent’s back rank can be promoted.
   - **Castling**: Move the king two squares toward a rook, which then moves to the square next to the king.
   - **En Passant**: Capture a pawn that has just moved two squares forward as if it had only moved one.

---

## 🖥 Game Interface
- **Drag-and-Drop**: Move pieces using your mouse.
- **Color-Coded Pieces**: Each piece type has a distinct visual indicator.
- **Configurable Board Size**: Adjust via configuration settings in `config.py`.
- **Highlighting**: (Planned) Show legal moves when a piece is selected.

---

## 🤖 AI Features
- **Destination Selection**: AI evaluates possible moves and prioritizes capturing high-value pieces.
- **Fallback Logic**: Chooses a random legal move if no captures are available.
- **Future Enhancements**: Risk assessment and defensive strategies.

---

## ⚙ Technical Features
- **Modular Movement Strategies**: Each piece's movement is implemented separately (`BishopMovement`, `RookMovement`, etc.).
- **Validation System**: Ensures moves are legal, prevent friendly fire, and respect movement definitions.
- **Transaction Management**: Allows undo/redo functionality for safe move rollbacks.
- **Capture Tracking**: Keeps records of captured pieces, captors, and capture locations.

---

## 🛠 Installation & Running
Refer to the README installation section for detailed setup instructions.

Quick start:
```bash
git clone https://github.com/yourusername/chessbot.git
cd chessbot
python bootstrap.py
```

Run the game:
```bash
python main.py
```

---

## 🎯 Tips for New Players
- Control the center squares early.
- Protect your king by castling when possible.
- Avoid moving the same piece multiple times in the opening unless necessary.
- Think ahead — anticipate your opponent’s response.

---

## 📜 License
ChessBot is licensed under the MIT License. See the LICENSE file for details.
