# 2. Domain-Specific Operations
#
# Each transaction type (occupation, promotion, castling, subject, etc.) gets its own subpackage.
# Inside, you can have:
#
# chess/
#  └── transaction/
#      ├── occupation/
#      │   ├── __init__.py
#      │   ├── transaction.py
#      │   ├── validator.py
#      │   ├── event.py
#      │   ├── exception.py
#      │   └── exception.py
#      │
#      ├── promotion/
#      │   ├── __init__.py
#      │   ├── transaction.py
#      │   ├── validator.py
#      │   ├── event.py
#      │   └── exception.py
#      │
#      ├── castling/
#      │   ├── __init__.py
#      │   ├── transaction.py
#      │   ├── validator.py
#      │   └── exception.py
#      │
#      └── subject/
#          ├── __init__.py
#          ├── transaction.py
#          ├── validator.py
#          ├── event.py
#          └── exception.py
