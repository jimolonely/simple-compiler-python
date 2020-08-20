from pip._vendor.distlib.compat import raw_input

INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type},{value})'.format(type=self.type, value=self.value)

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        text = self.text

        if self.pos > len(text) - 1:
            return Token(EOF, None)

        current_char = text[self.pos]

        if current_char.isdigit():
            int_str = ''
            while self.pos < len(text) and current_char.isdigit():
                int_str += current_char
                self.pos += 1
                if self.pos < len(text):
                    current_char = text[self.pos]
                else:
                    break
            token = Token(INTEGER, int(int_str))
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        if self.current_token.type in token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat([INTEGER])

        op = self.current_token
        self.eat([PLUS, MINUS])

        right = self.current_token
        self.eat([INTEGER])

        if op.type == PLUS:
            return left.value + right.value
        elif op.type == MINUS:
            return left.value - right.value


def main():
    while True:
        try:
            text = raw_input('calc>')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
