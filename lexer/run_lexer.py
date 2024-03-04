from lexer import Lexer

if __name__ == "__main__":
    while True:
        text: str = input("Enter text...\n")
        lexer: Lexer = Lexer(text)
        print(lexer.make_token())
