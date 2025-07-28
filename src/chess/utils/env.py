class DevMode:
    _raise_errors = True  # Set this to False in production

    @classmethod
    def raise_or_print(cls, message: str):
        if cls._raise_errors:
            raise RuntimeError(message)
        else:
            print("[WARNING]", message)
