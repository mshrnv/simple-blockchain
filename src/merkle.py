"""Custom Merklee tree"""
from hashlib import sha256


class Node:
    """Node of Merkle tree"""

    def __init__(self, left, right, content):
        self.left = left
        self.right = right
        self.content = content
        self.value = self.__hash()

    def __hash(self) -> str:
        return sha256(self.content.encode("utf-8")).hexdigest()

    def __str__(self):
        return self.value


class MerkleTree:
    """Merkle tree class"""

    def __init__(self, values):
        self.__build_tree(values)

    def __build_tree(self, values):
        leaves = [Node(None, None, value) for value in values]
        if len(leaves) % 2 == 1:
            leaves.append(leaves[-1])
        self.__root = self.__build_tree_rec(leaves)

    def __build_tree_rec(self, nodes):
        mid = len(nodes) // 2

        if len(nodes) == 2:
            return Node(
                nodes[0],
                nodes[1],
                str(nodes[0]) + str(nodes[1]),
            )

        left = self.__build_tree_rec(nodes[:mid])
        right = self.__build_tree_rec(nodes[mid:])
        content = str(left) + str(right)

        return Node(left, right, content)

    def print_tree(self):
        """Recursievly prints all tree nodes"""
        self.__print_tree_rec(self.__root)

    def __print_tree_rec(self, node):
        if node is not None:
            if node.left is not None:
                print("Left: " + str(node.left))
                print("Right: " + str(node.right))
            else:
                print("Input")

            print("Value: " + str(node.value))
            print("Content: " + str(node.content))
            print("")
            self.__print_tree_rec(node.left)
            self.__print_tree_rec(node.right)

    def get_root_hash(self):
        """Hash of root element"""
        return self.__root.value
