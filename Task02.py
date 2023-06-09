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


class Token:
    def __init__(self, type, value):
        self.type = type
        self.lexeme = value
    def to_string(self):
        return f"Token [type={self.type}, lexeme={self.lexeme}]"


if __name__ == "__main__":
    empty, error, error_element = False, False, None
    stacker = Stack()
    token_list = list()
    OP = {"+":"PLUS", "-": "MINUS", "*": "STAR", "/": "SLASH"}

    while empty == False:
        element = str(input())
        type = None

        match element:
            case x if x in OP:
                v0 = stacker.pop()
                v1 = stacker.pop()
                stacker.push(eval(f"{v1} {x} {v0}"))
                type = OP[x]   
            
            case x if x.isdigit() == True:
                stacker.push(int(element))
                type = "NUM"


            case "":                        # To end
                if error == True:
                    print(f"Error: unexpected character: {element}")
                else:
                    for token in token_list:
                        print(token.to_string())
                    print(stacker.head.next.value)

                stacker = Stack()
                empty, type = True, None
                exit()

            case default:                   # For error printing
                if error is False:
                    error = True
                    error_element = element
        
        element = Token(type, element)
        token_list.append(element)
