class Token:
    def __init__(self, type: str, val: str = None) -> None:
        self.type = type
        self.val = val

    def __repr__(self):
        return f"{self.type}: {self.val}" if self.val else f"{self.type}"
