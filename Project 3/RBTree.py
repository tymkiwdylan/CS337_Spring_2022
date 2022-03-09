
import process



class RBNode:
    def  __init__(self, Key, data):

       self.Key = Key
       self.parent = 0
       self.left = 0
       self.right = 0
       self.isRed = 0
       self.data = data
    

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
        self.nil = RBNode(0, 0)
        self.root = self.nil
        self.root.parent = self.nil
        self.root.left = self.nil
        self.root.right = self.nil
        self.min_vruntime = self.root
        self.size = 0

    def insert(self, value, data):
        z = RBNode(value, data)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x 
            if z.Key < x.Key:
                x = x.left
            else:
                x = x.right
        
        z.parent = y
        
        if y == self.nil:
            self.root = z
        else:
            if z.Key < y.Key:
                y.left = z
            else:
                y.right = z
        
        z.left = self.nil
        z.right = self.nil
        z.isRed = True
        self.size += 1
        self.fix_insert(z)
        
        if (z.Key < self.min_vruntime.Key) or z.parent == self.nil:
            self.min_vruntime = z


    def fix_insert(self, node):
        while (node.parent.isRed): 
            uncle = self.uncle(node) 
            if uncle.isRed:
                node.parent.isRed = False
                uncle.isRed = False
                node.parent.parent.isRed = True
                node = node.parent.parent
            else:
                if self.isTriangle(node): 
                    node = node.parent
                    if node.parent.right == node:
                        self.rotate_left(node)
                    else:
                        self.rotate_right(node)
                    
                node.parent.isRed = False
                node.parent.parent.isRed = True
                if node.parent.right == node:
                    self.rotate_left(node.parent.parent)
                else:
                    self.rotate_right(node.parent.parent)


        self.root.isRed = False

    def uncle(self, node):
        if node.parent.parent.left != node.parent:
            return node.parent.parent.left
        else:
            return node.parent.parent.right
            
    def isTriangle(self, node):
        if node.parent.parent.right.left == node:
            return True
        if node.parent.parent.left.right == node:
            return True
        return False


    def rotate_left(self, node):
        y = node.right
        node.right = y.left
        y.left.parent = node
        y.parent = node

        if node.parent == self.nil:
            self.root = y
        else:
            if node == node.left.parent:
                node.parent.left = y
            else:
                node.parent.right = y
        y.left = node
        node.parent = y

    def rotate_right(self, node):
        y = node.left
        node.left = y.right
        y.right.parent = node
        y.parent = node.parent

        if node.parent == self.nil:
            self.root = y
        else:
            if node == node.parent.left:
                node.parent.left = y
            else:
                node.parent.right = y
        y.right = node
        node.parent = y

    def print_tree(self, root):
        if root != self.nil:

            self.print_tree(root.left)
            print(root.Key)
            self.print_tree(root.right)

    def remove_min_vruntime(self):
        node = self.min_vruntime

        if node.right == self.nil:
            self.min_vruntime = node.parent
            self.min_vruntime.left = self.nil
        else:
            self.min_vruntime = node.right
            self.min_vruntime.parent = node.parent
            self.min_vruntime.parent.left = self.min_vruntime


        self.size -= 1
        return node.data

    def get_size(self):
        return self.size


def main():
    tree = RBTree()

    tree.insert(0,1)
    print(tree.remove_min_vruntime())
    tree.insert(0,2)
    tree.insert(5,1)
    print(tree.root.data)
    print(tree.root.parent.data)
    print(tree.remove_min_vruntime())
    print(tree.root.data)
    tree.insert(5,1)

    # tree.print_tree(tree.root)

    #print("size:" ,tree.size)

    # print(tree.remove_min_vruntime())
    # print(tree.remove_min_vruntime())
    # print(tree.remove_min_vruntime())
    # print(tree.remove_min_vruntime())
    # print(tree.remove_min_vruntime().Key)

    # while tree.size != 0:
    #     print(tree.remove_min_vruntime())
    
    # print("size:" ,tree.size)

    # print(tree.root.Key)
    # print(tree.root.left.Key)
    # print(tree.root.right.Key)
    # print(tree.root.right.right.Key)
    # print(tree.min_vruntime.Key)


    


if __name__ == '__main__':
    main()
        

