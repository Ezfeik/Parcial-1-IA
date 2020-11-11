class Tree:
    """
        General Tree data structure.
        A node independent implementation with basics method.
    """
    

    def __init__(self, data, level=0):
        
        self.data = data
        self.root = None
        self.leafs = []
        self.level = level


    def add_leaf(self, data, target=None):
        """
            Insertion of an element. Change IN-PLACE
        """
        
        
        if target:
            if target == self.data:
                leaf = Tree(data, level=self.level + 1)
                leaf.root = self
                self.leafs.append(leaf)
            else:
                for leaf in self.leafs:
                    leaf.add_leaf(data, target=target)
        else:
            leaf = Tree(data, level=self.level + 1)
            leaf.root = self
            self.leafs.append(leaf)


    def chain_to_root(self):
        """
            Return a list of the elements from the current element to the root element of
            the tree.
        """
        
        
        chain = [self.data]
        aux_tree = self.root
        while aux_tree:
            chain.append(aux_tree.data)
            aux_tree = aux_tree.root
        return chain


    def print_tree(self):
        """
            Print by level. Directory tree like.
        """
        
        
        print('    '*self.level + str(self.data))
        if self.leafs:
            for leaf in self.leafs:
                leaf.print_tree()
