# Motion Package Overview

The `motion` package provides the foundational logic and structures needed to define how chess pieces move across the board. It is the lowest layer in the movement system and is designed to separate *orientation*, *walks*, *rules*, and *strategy* to maintain clarity and flexibility.

---

## 📚 Table of Contents

1. [🌐 Conceptual Layers](#-conceptual-layers)  
   - [1. Orientation](#1-orientation)  
   - [2. Walks](#2-walks)  
   - [3. Rules](#3-rules)  
   - [4. Strategy](#4-strategy)  
   - [5. Quadrant / Geometry](#5-quadrant--geometry)  
2. [🧱 Dependencies and Flow](#-dependencies-and-flow)  
3. [✅ Design Principles](#-design-principles)  
4. [🔧 Example Use Case](#-example-use-case)  
5. [🧭 Naming Clarification](#-naming-clarification)  
6. [📁 Recommended Directory Layout](#-recommended-directory-layout)  
7. [📌 Next Steps](#-next-steps)  

---

## 🌐 Conceptual Layers

### 1. Orientation
- Represents geometric alignment (vertical, horizontal, diagonal, L-shaped offset).
- These are not literal "directions" like north or south, but rather describe **how pieces may traverse the board**.
- Used as building blocks in walk sequences.

**Examples:**
- `vertical.py`
- `horizontal.py`
- `diagonal.py`
- `knight_offset.py`

---

### 2. Walks


**Examples:**
- `single_step.py`
- `compound_walk.py`
- `unbounded_walk.py`
- `path_constraints.py`

---

### 3. Rules
- Encapsulate how walks are applied under piece-specific rules.
- May include context-based logic (e.g., first move, promotion row, capture-only diagonals).
- Used by `MovementStrategy` but focused on rule validation.

**Examples:**
- `pawn_rule.py`
- `king_rule.py`
- `rook_rule.py`

---

### 4. Strategy
- Combines walk patterns and rule checks to determine legal destinations.
- Used by the `Rank` class to generate valid moves based on:
  - Current position
  - Board state
  - Team orientation (e.g., forward = north for white, south for black)

**Examples:**
- `movement_strategy.py`

---

### 5. Quadrant / Geometry
- Utilities for defining and calculating spatial quadrants or directional domains.
- Helps determine where a piece is allowed to move or capture.

**Examples:**
- `quadrant.py`

---

## 🧱 Dependencies and Flow

```plaintext
Piece
  └── delegates movement logic to → Rank
      └── uses → MovementStrategy
          ├── applies → Rules
          └── queries → Walks and Orientations
