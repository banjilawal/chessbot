# 2. Domain-Specific Operations
#
# Each transaction type (travel, promotion, castling, enemy, etc.) gets its own subpackage.
# Inside, you can have:
#
# chess/
# └── transaction/
#   ├── travel/
#   │  ├── __init__.py
#   │  ├── old_transaction.py
#   │  ├── old_occupation_validator.py
#   │  ├── travel_event.py
#   │  ├── err.py
#   │  └── err.py
#   │
#   ├── promotion/
#   │  ├── __init__.py
#   │  ├── old_transaction.py
#   │  ├── old_occupation_validator.py
#   │  ├── travel_event.py
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
#     ├── travel_event.py
#     └── err.py
