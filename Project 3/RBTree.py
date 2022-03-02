
class RBNode:
    def  __init__(self, Key, parent, left, right, isRed):

       Key = Key
       parent = parent
       left = left  
       right = right
       isRed = isRed
    

    def get_Key(self):
        return self.Key

    def get_parent(self):
        return self.get_parent
    
    def get_left(self):
        return self.left 
    

    def get_right(self):
        return self.right


    def get_isRed(self):
        return self.isRed

    
    def set_Key(self, Key):
        self.Key = Key 
    

    def set_parent(self, parent):
        self.parent = parent
    

    def set_left(self, left):
        self.left = left 

    def set_right(self, right):
        self.right = right
    

    def set_isRed(self, isRed):
        self.isRed = isRed

class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.root = self.nil
        self.min_vruntime = self.root

    def insert(self, value):
        pass

    def fix_insert(self, node):
        pass

    def rotate_left(self, node):
        y = node.right
        node.right = y.left
        y.left.set_parent(node)
        y.set_parent(node)

        if node.get_parent() == self.nil:
            self.root = y
        else:
            if node == node.get_parent().left:
                node.set_parent(y)
            else:
                node.get_parent().right.set_parent(y)
        y.left = node
        node.parent = y

    def rotate_right(self, node):
        y = node.left
        node.left = y.right
        y.right.set_parent(node)
        y.set_parent(node)

        if node.get_parent() == self.nil:
            self.root = y
        else:
            if node == node.get_parent().left:
                node.set_parent(y)
            else:
                node.get_parent().right.set_parent(y)
        y.right = node
        node.parent = y

    def print_tree(self):
        pass

    def remove_min_vruntime(self):
        pass
    
