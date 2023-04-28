import re


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = str()
        while cur:
            out += (f"{str(cur.value)} -> ")
            cur = cur.next
        return out[:-3]

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Empty Stack")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.size >= 1:
            remove = self.head.next
            self.head.next = self.head.next.next
            self.size -= 1
            return remove.value


class Regex:
    def __init__(self):
        self.regex = r"\d+|[+\-*/]"
        self.input_list = list()
        self.tokens = list()

    def add(self, element):
        self.input_list.append(element)

    def scanning(self):
        for element in self.input_list:
            check = re.match(self.regex, element)
            if check:
                if element.isdigit():
                    self.tokens.append(Token("NUM", int(element)))
                else:
                    self.tokens.append(Token(OP[element], element))
            else:
                print(f"Error: Unexpected character: {element}")
                exit()
        return self.tokens

class Token:
    def __init__(self, type, value):
        self.type = type
        self.lexeme = value
    def to_string(self):
        return f"Token [type={self.type}, lexeme={self.lexeme}]"


if __name__ == "__main__":
    empty = False
    stacker = Stack()
    regEx = Regex()
    OP = {"+":"PLUS", "-": "MINUS", "*": "STAR", "/": "SLASH"}

    while empty == False:
        element = str(input())
        type = None

        match element:
            case x if x in OP:
                v0 = stacker.pop()
                v1 = stacker.pop()
                stacker.push(eval(f"{v1} {x} {v0}"))
            
            case x if x.isdigit() == True:
                stacker.push(int(element))

            case "":                        # To end
                list_tokens = regEx.scanning()
                for token in list_tokens: print(f"Token [type={token.type}, lexeme={token.lexeme}]")

                print(stacker.head.next.value)
                stacker.pop()
                empty = True

                exit()

            case default:                   # For error printing
                pass

        regEx.add(element)