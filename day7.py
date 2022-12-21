class Node:
    def __init__(self, key=0, name=""):
        self.children = []
        self.data = key
        self.name = name
        self.total = 0


def findParent(root, node):
    if root == node:
        return root
    if node in root.children:
        return root
    for item in root.children:
        check = findParent(item, node)
        if check:
            return check
    return None


def findNode(node, key):
    if node.name == key:
        return node
    for item in node.children:
        check = findNode(item,key)
        if check:
            return check
    return None

def get_total(node):
    if len(node.children) == 0:
        return node.data
    elif len(node.children) > 0 and node.total > 0:
        return node.total
    for child in node.children:
        node.total+= get_total(child)
    return node.total


root = Node(name='/')
current = None

with open("day7input.txt") as f:
    for line in f:
        line = line.strip()
        if line == "$ cd pdtjlb":
            print("Found")
        line = line.split(" ")
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    current = findParent(root,current)
                else:
                    if current != None:
                        current = findNode(findParent(root,current), line[2])
                    else:
                        current = findNode(root, line[2])
        elif line[0] == "dir":
            test = Node(name=line[1])
            current.children.append(test)
        else:
            test = Node(name=line[1], key=int(line[0]))
            current.children.append(test)



overall = 0

def searchTree(root):
    global overall
    if root:
        for item in root.children:
            value = get_total(item)
            if value <= 100000 and len(item.children) > 0:
                overall+=value
            searchTree(item)

searchTree(root)
print(overall)
