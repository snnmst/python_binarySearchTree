class PERSON:
    def __init__(self, name, no):
        self.name = name
        self.no = no

class NODE:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.amount = 1
        self.parent = None 


class HBINARYTREE():
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, data):
        if self.root is None:
            self.root = NODE(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, cur_node):
        if data.no < cur_node.data.no:
            if cur_node.left is None:
                cur_node.left = NODE(data)
                cur_node.left.parent = cur_node
            else:
                self._insert(data, cur_node.left)
        elif data.no > cur_node.data.no:
            if cur_node.right is None:
                cur_node.right = NODE(data)
                cur_node.right.parent = cur_node
            else:
                self._insert(data, cur_node.right)
        else:
            cur_node.amount += 1
    
    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
        print("**************************************")
        
    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(f"{cur_node.data.name} - {cur_node.data.no}")
            self._print_tree(cur_node.right)
        

    def find(self, val):
        if self.root != None:
            return self._find(val, self.root)
        else:
            return None
    def _find(self, val, cur_node):
        if val == cur_node.data.no:
            return cur_node
        elif val < cur_node.data.no and cur_node.left != None:
            return self._find(val, cur_node.left)
        elif val > cur_node.data.no and cur_node.right != None:
            return self._find(val, cur_node.right)
        
    def delete_value(self, val):
        return self.delete_node(self.find(val))
    
    def delete_node(self, node):
        if node == None or self.find(node.data.no) == None:
            print('Node to be deleted not found in th tree!')
            return None
        
        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current
        
        def num_children(n):
            num_children = 0
            if n.left != None :
                num_children += 1
            if n.right != None:
                num_children += 1
            return num_children
        
        node_parent = node.parent
        node_children = num_children(node)

        # CASE 1 (node has no children)

        if node_children == 0:
            if node_parent != None:
                if node_parent.left == node:
                    node_parent.left = None 
                else:
                    node_parent.right = None 
                
            else:
                self.root = None 
        
        # CASE 2 (node has a single child)

        if node_children == 1:
            if node.left != None:
                child = node.left
            else:
                child = node.right 
            
            if node_parent!= None:
                if node_parent.left == node:
                    node_parent.left = child 
                else:
                    node_parent.right = child 
                
            else:
                self.root = child 
            
            child.parent = node_parent
        
        # CASE 3 (node has two children)

        if node_children == 2:
            successor = min_value_node(node.right)
            node.data = successor.data
            self.delete_node(successor)


if __name__ == '__main__':

    hBinaryTree = HBINARYTREE()
    p1 = PERSON('Sinan', 17)
    p2 = PERSON('Elly', 11)
    p3 = PERSON('Alex', 23)
    p4 = PERSON('BilliBob', 31)
    p5 = PERSON('David', 12)
    p6 = PERSON('Simon', 7)
    p7 = PERSON('Lily', 19)

    persons = [p1,p2,p3,p4,p5,p6,p7]
    for p in persons:
        hBinaryTree.insert(p)
    

    hBinaryTree.print_tree()
    hBinaryTree.delete_value(12)
    hBinaryTree.print_tree()
    hBinaryTree.delete_value(7)
    hBinaryTree.print_tree()
    hBinaryTree.delete_value(23)
    hBinaryTree.print_tree()
    hBinaryTree.delete_value(11)
    hBinaryTree.print_tree()
    hBinaryTree.delete_value(31)
    hBinaryTree.print_tree()
    hBinaryTree.delete_value(17)
    hBinaryTree.print_tree()
    hBinaryTree.delete_value(19)
    hBinaryTree.print_tree()
    hBinaryTree.delete_value(0)