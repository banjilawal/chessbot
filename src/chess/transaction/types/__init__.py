# 2. Domain-Specific Operations
#
# Each transaction type (event, promotion, castling, enemy, etc.) gets its own subpackage.
# Inside, you can have:
#
# chess/
# └── transaction/
#   ├── event/
#   │  ├── __init__.py
#   │  ├── old_transaction.py
#   │  ├── old_occupation_validator.py
#   │  ├── event.py
#   │  ├── err.py
#   │  └── err.py
#   │
#   ├── promotion/
#   │  ├── __init__.py
#   │  ├── old_transaction.py
#   │  ├── old_occupation_validator.py
#   │  ├── event.py
#   │  └── err.py
#   │
#   ├── castling/
#   │  ├── __init__.py
#   │  ├── old_transaction.py
#   │  ├── old_occupation_validator.py
#   │  └── err.py
#   │
#   └── enemy/
#     ├── __init__.py
#     ├── old_transaction.py
#     ├── old_occupation_validator.py
#     ├── event.py
#     └── err.py
