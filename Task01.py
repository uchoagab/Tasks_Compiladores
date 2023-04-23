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


if __name__ == "__main__":
    empty = False
    stacker = Stack()

    while empty == False:
        element = str(input())
        match element:
            case "":
                print(stacker.head.next.value)
                stacker.pop()
                empty = True
                exit()
            case "+":
                v0 = stacker.pop()
                v1 = stacker.pop()
                stacker.push(v1+v0)
            case "-":
                v0 = stacker.pop()
                v1 = stacker.pop()
                stacker.push(v1-v0)
            case "*":
                v0 = stacker.pop()
                v1 = stacker.pop()
                stacker.push(v1*v0)      
            case "/":
                v0 = stacker.pop()
                v1 = stacker.pop()
                stacker.push(v1/v0)          
            case default:
                stacker.push(int(element))