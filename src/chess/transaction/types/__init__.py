# 2. Domain-Specific Operations
#
# Each transaction type (occupation, promotion, castling, enemy, etc.) gets its own subpackage.
# Inside, you can have:
#
# chess/
#  └── transaction/
#      ├── occupation/
#      │   ├── __init__.py
#      │   ├── transaction.py
#      │   ├── validator.py
#      │   ├── base.py
#      │   ├── err.py
#      │   └── err.py
#      │
#      ├── promotion/
#      │   ├── __init__.py
#      │   ├── transaction.py
#      │   ├── validator.py
#      │   ├── base.py
#      │   └── err.py
#      │
#      ├── castling/
#      │   ├── __init__.py
#      │   ├── transaction.py
#      │   ├── validator.py
#      │   └── err.py
#      │
#      └── enemy/
#          ├── __init__.py
#          ├── transaction.py
#          ├── validator.py
#          ├── base.py
#          └── err.py
