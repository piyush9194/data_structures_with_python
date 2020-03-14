""""Diameter of Binary Tree"""




def diamter_of_binary_tree(self):
    self.diameter = 0
    def height(root):
        if not root:
            return 0
        left = height(root.left)
        right = height(root.right)

        c_diameter = left + right
        self.diameter = max(self.diameter,c_diameter)

        return max(left,right) +1

    height(self.root)
    return self.diameter