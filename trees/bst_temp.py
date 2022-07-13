class Node:
    def __init__(self,key) -> None:
        self.key = key
        self.left =None
        self.right = None

def get_min_value(node):
    curr = node
    while curr.left != None:
        curr = curr.left
    return curr


def insert(node,key):
    if node is None:
        return Node(key)
    elif node.key < key:
        node.right = insert(node.right,key)
    elif node.key > key:
        node.left = insert(node.left,key)
    return node

def binary_serach(node,key):
    if node is None:
        return node
    elif node.key > key:
        return binary_serach(node.left,key)
    elif node.key < key:
        return binary_serach(node.right,key)
    elif node.key == key:
        return node

def delete(node,key):
    if node is None:
        return node
    elif node.key < key:
        # instead of return people do write i.e root.right = delete(node.right,key) why ??
        return delete(node.right,key)
    elif node.key > key:
        return delete(node.left,key)
    else:
        if node.left is None:
            temp_node = node.right
            node = None
            return temp_node
        elif node.right is None:
            temp_node = node.left
            node = None
            return temp_node
        else:
            temp_node = get_min_value(node.right)
            node.key = temp_node.key
            return delete(node.right,temp_node.key)


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.key)
        inOrder(root.right)

def preOrder(root):
    if root:
        print(root.key)
        preOrder(root.left)
        preOrder(root.right)
    
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.key)
        
root = None
root = insert(root,12)
root = insert(root,23)
root = insert(root,10)
root = insert(root,100)
# print(binary_serach(root,84))
print(binary_serach(root,100))
root = delete(root,100)
print(binary_serach(root,100))