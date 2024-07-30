class BinarySearchTree:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    
    def add_child(self, data):
        if self.data==data:
            return

        if self.data>data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right= BinarySearchTree(data)

    def inorder_traversal(self):
        element=[]
        #visit the left node
        if self.left:
            element+= self.left.inorder_traversal()

        #visit the parent node
        element.append(self.data)

        #visite the right node
        if self.right:
            element+=self.right.inorder_traversal()

        return element

    def preorder_traversal(self):
        element=[]
        
        #visit the parent node
        element.append(self.data)

        #visit the left node
        if self.left:
            element+= self.left.preorder_traversal()

        #visite the right node
        if self.right:
            element+=self.right.preorder_traversal()

        return element
    
    def postorder_traversal(self):
        element=[]

        if self.left:
            element+=self.left.postorder_traversal()

        if self.right:
            element+= self.right.postorder_traversal()

        element.append(self.data)

        return element
    def search(self, element):
        if self.data== element:
            return True
        if self.data<element:
            if self.right:
                return self.right.search(element)
            else:
                return False
        else:
            if self.left:
                return self.left.search(element)
            else:
                return False
    

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def sum(self):
        leftsum= self.left.sum() if self.left else 0
        rightsum= self.right.sum() if self.right else 0
        return leftsum+ rightsum+self.data

    def delete(self, val):
        if self.data>val:
            if self.left:
                self.left=self.left.delete(val)
        elif self.data<val:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            # Node with one child
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            # Node with two children
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self




def build_tree(elements):
    root= BinarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root


if __name__=='__main__':
    numbers=[5, 3, 8, 1, 4, 7, 10]
    root=build_tree(numbers)
    print(root.inorder_traversal())
    print(root.preorder_traversal())
    print(root.postorder_traversal())

    print("Found" if root.search(10) else "Not found")
    print(f"Maximum element in this tree is ", root.find_max())
    print(f"Minimum element in this tree is ", root.find_min())
    root.delete(10)
    print("Inorder Traversal after deleting 10:", root.inorder_traversal())  # [1, 3, 4, 5, 7, 8]
    root.delete(5)
    print("Inorder Traversal after deleting 5:", root.inorder_traversal())  # [1, 3, 4, 7, 8]