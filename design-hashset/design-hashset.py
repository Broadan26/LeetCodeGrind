class MyHashSet:

    def __init__(self):
        self.root = None

    def add(self, key: int) -> None:
        '''
        Inserts a value into the hashset tree
        '''
        if self.root is None: # No tree exists
            self.root = TreeNode(key)
        node = self.root
        prev = None
        while node is not None: # Locate key or locate where to place new key
            prev = node
            if node.val == key: # Key in tree, done
                return
            elif node.val > key: # Determine which way to traverse
                node = node.left
            else: 
                node = node.right
        if prev.val > key: # Place new key
            prev.left = TreeNode(key)
        else:
            prev.right = TreeNode(key)

    def remove(self, key: int) -> None:
        '''
        Removes the requested key from the tree
        '''
        if self.root is None: # Tree is empty
            return

        node = self.root
        prev = None
        while node is not None and node.val != key: # Search for the key
            prev = node
            if node.val > key:
                node = node.left
            else:
                node = node.right

        if node is None: # Key not found
            return

        if node.left is None or node.right is None: #Node to be deleted has 1 child
            curr = None
            if node.right is None: # Determine which node is empty
                curr = node.left
            else:
                curr = node.right
            if prev is None: # If head was removed, simply move subtree
                self.root = curr
            else:
                if node == prev.left: # Otherwise skip the over the old node
                    prev.left = curr
                else:
                    prev.right = curr

        else: # Node to be deleted has 2 children
            p = None
            temp = None
            temp = node.right
            while temp.left is not None: #Look for the smallest node
                p = temp
                temp = temp.left
            if p is not None:
                p.left = temp.right
            else:
                node.right = temp.right
            node.val = temp.val

    def contains(self, key: int) -> bool:
        '''
        Determines if the key value is in the tree or not
        Returns true if found, false otherwise
        '''
        iterator = self.root
        while iterator is not None:
            if iterator.val == key:
                return True
            elif iterator.val > key:
                iterator = iterator.left
            else:
                iterator = iterator.right
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)