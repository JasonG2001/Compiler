class Position:
    def __init__(self, idx: int, ln: int, col: int, file_name: str, file_text: str) -> None:
        self.idx: int = idx
        self.ln: int = ln
        self.col: int = col
        self.file_name: str = file_name
        self.file_text: str = file_text

    def advance(self, cur_char: str):
        self.idx += 1
        self.col += 1
        
        if cur_char == "\n":
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.file_name, self.file_text)

    def get_idx(self) -> int:
        return this.idx
