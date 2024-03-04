from invalid_character_exception import InvalidCharacterException
from token import Token
from typing import List

class Lexer:
    def __init__(self, text: str) -> None:
        self.text: str = text
        self.pos: int = 0
        self.cur_char: str = text[self.pos]
        self.numbers: str = "0123456789"
    
    def advance(self):
        self.pos += 1
        self.cur_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_token(self) -> List[Token]:
        tokens: List[Token] = []

        while self.cur_char:
            if self.cur_char == "+":
                tokens.append(Token("PLUS"))
                self.advance()
            elif self.cur_char == "-":
                tokens.append(Token("MINUS"))
                self.advance()
            elif self.cur_char == "/":
                tokens.append(Token("DIVIDE"))
                self.advance()
            elif self.cur_char == "*":
                tokens.append(Token("MULTIPLY"))
                self.advance()
            elif self.cur_char == "(":
                tokens.append(Token("LPAR"))
                self.advance()
            elif self.cur_char == ")":
                tokens.append(Token("RPAR"))
                self.advance()
            elif self.cur_char in self.numbers:
                tokens.append(self.make_numbers())
            else:
                return InvalidCharacterException(f"Character '{self.cur_char}' not recognised")

        return tokens

    def make_numbers(self) -> Token:
        num_str: str = ""
        dot_count: int = 0;

        while self.cur_char and self.cur_char in (self.numbers + "."):
            if self.cur_char == ".":
                if dot_count == 1:
                    break
                dot_count += 1
            num_str += self.cur_char
            self.advance()

        return Token("FLOAT", float(num_str)) if dot_count else Token("INT", int(num_str))
