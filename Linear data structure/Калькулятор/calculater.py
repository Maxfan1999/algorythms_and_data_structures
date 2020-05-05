class StackOnList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('Method "pop" is allowed only for not empty stack')
        res = self.items[-1]
        del self.items[-1]
        return res

    def top(self):
        if self.is_empty():
            raise Exception('Method "top" is allowed only for not empty stack')
        else:
            return self.items[-1]

class StringCalculator:
    def __init__(self):
        self.operators = {
            "+": 2,
            "-": 2,
            "*": 1,
            "/": 1
        }

    def convert_to_polish(self, s):
        s = s.replace(" ", "")
        result_ar = []
        _stack = StackOnList()
        index = 0
        while index < len(s):
            token = s[index]
            is_digit = False
            if token.isdigit():
                is_digit = True
            index += 1
            while is_digit:
                if index < len(s):
                    if s[index].isdigit():
                        token += s[index]
                        index += 1
                    else:
                        break
                else:
                    break
            # print(result_ar, _stack.items, token)
            if is_digit:
                if len(token) > 90:
                    raise Exception("Token length bigger than 90")
                result_ar.append(token)
            elif token == "(":
                _stack.push(token)
            elif token == ")":
                while _stack.top() != "(":
                    result_ar.append(_stack.pop())
                _stack.pop()
            elif token in self.operators:
                if not _stack.is_empty():
                    if _stack.top in self.operators:
                        if self.operators[token] >= self.operators[_stack.top()]:
                            result_ar.append(_stack.pop())
                _stack.push(token)
        while not _stack.is_empty():
            result_ar.append(_stack.pop())
        return result_ar

    @staticmethod
    def simple_operations(left, right, operator):
        left, right = int(left), int(right)
        if operator == "+":
            return left + right
        elif operator == "-":
            return left - right
        elif operator == "*":
            return left * right
        elif operator == "/":
            return left // right

    def calculate_polish(self, polish):
        _stack = StackOnList()
        for token in polish:
            if token in self.operators:
                right_operant = _stack.pop()
                left_operant = _stack.pop()
                res = self.simple_operations(left_operant, right_operant, token)
                if 0 > res or res >= 10**90:
                    raise Exception("Result of exeption is smoller than zero")
                _stack.push(res)
            else:
                _stack.push(token)
        return _stack.pop()


with open("input.txt", "r") as _input_file:
    with open('output.txt', 'w') as _output_file:
        for string_exeptions in _input_file.readlines():
            try:
                calc = StringCalculator()
                polish = calc.convert_to_polish(string_exeptions)
                # print(polish)
                print(calc.calculate_polish(polish), file=_output_file)
            except:
                print("Error", file=_output_file)



