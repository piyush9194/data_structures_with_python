"""
        The mirror image of tree can ve derived by traversing the tree in postorder traversal and
        swapping the left and right child of each node

        https://www.youtube.com/watch?v=apkprrLFZ6A&list=PLjhq5EHRYAeLdh0xtn2v7wbQsVc8WAB2e&index=15

"""


def mirror_image_of_tree(self, root):
    """Swap every node left and right child in postorder traversal"""
    current = root
    if current:
        self.mirror_image_of_tree(current.left)
        self.mirror_image_of_tree(current.right)
        current.left, current.right = current.right, current.left