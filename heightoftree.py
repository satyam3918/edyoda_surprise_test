class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data
class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur

            else:
                cur = self.insert(root.right, data)
                root.right = cur
            return root


    def get_height(self, root):

        m = A()
        temp = m.get_height_util(root)
        return temp

class A:
    def method_1(self, root):
        print(root.data)


    def get_height_util(self, root):
        if root == None:
            return 0
        lh = self.get_height_util(root.left)
        rh = self.get_height_util(root.right)

        if lh > rh:
            return lh + 1
        else:
            return rh + 1
def main():
    T = int(input("Enter the number of elements: "))
    my_tree = Solution()
    root = None
    for i in range(T):
        data = int(input("Enter the element: "))
        root = my_tree.insert(root, data)
    height = my_tree.get_height(root)
    print("Height of the tree is: ", str(height))
if __name__ == "__main__":
    main()
