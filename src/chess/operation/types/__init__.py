# 2. Domain-Specific Operations
#
# Each operation type (occupation, promotion, castling, subject, etc.) gets its own subpackage.
# Inside, you can have:
#
# chess/
#  └── operation/
#      ├── occupation/
#      │   ├── __init__.py
#      │   ├── executor.py
#      │   ├── validator.py
#      │   ├── directive.py
#      │   ├── exception.py
#      │   └── attack_exceptions.py
#      │
#      ├── promotion/
#      │   ├── __init__.py
#      │   ├── executor.py
#      │   ├── validator.py
#      │   ├── directive.py
#      │   └── exception.py
#      │
#      ├── castling/
#      │   ├── __init__.py
#      │   ├── executor.py
#      │   ├── validator.py
#      │   └── exception.py
#      │
#      └── subject/
#          ├── __init__.py
#          ├── executor.py
#          ├── validator.py
#          ├── directive.py
#          └── exception.py
