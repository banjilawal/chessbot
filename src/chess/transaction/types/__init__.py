# 2. Domain-Specific Operations
#
# Each transaction type (event, promote, castling, enemy, etc.) gets its own subpackage.
# Inside, you can have:
#
# chess/
# └── transaction/
#   ├── event/
#   │  ├── __init__.py
#   │  ├── transaction.py
#   │  ├── validator.py
#   │  ├── event.py
#   │  ├── err.py
#   │  └── err.py
#   │
#   ├── promote/
#   │  ├── __init__.py
#   │  ├── transaction.py
#   │  ├── validator.py
#   │  ├── event.py
#   │  └── err.py
#   │
#   ├── castling/
#   │  ├── __init__.py
#   │  ├── transaction.py
#   │  ├── validator.py
#   │  └── err.py
#   │
#   └── enemy/
#     ├── __init__.py
#     ├── transaction.py
#     ├── validator.py
#     ├── event.py
#     └── err.py
