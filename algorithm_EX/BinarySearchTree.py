class Node:
    __slots__ = '_item' , '_left' , '_right'
    
    def __init__(self, item, left=None, right=None):
        self._item = item
        self._left = left
        self._right = right
        
class BinarySearchTree:
    
    def __init__ (self, root=None):
        self._root = root
        
    # Get methods
    def get(self, key):
        return self.__get(self._root, key)
    
    def __get(self, node, key): #helper
        if (node is None):
            return None
        if node._item == key:
            return node
        elif node._item < key:
            return self.__get(node._left, key)
        else:
            return self.__get(node._right. key)
        
    # add methods
    def add(self, value):
        self._root = self.__add(self._root, value)
    
    def __add(self, node, value):
        if node is None:
            node = Node(value)
        if node._item == value:
            pass
        elif value < node._item:
            node._left = self.__add(node._left, value)
        else:
            node._right = self.__add(node._right, value)
        
        return node
    
    # remove methods
    def remove(self, key):
        self._root = self.__remove(self, self._root, key)
        
    def __remove(self, node, key):
        if node is None:# 第一种情况，
            return None
        if node._item == key:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                node._item = self.__get_max(node._left)
                node._left = self.__remove(node._left, node._item)       
        elif node._item < key:
            node = self.__remove(node._left, key)
        else:
            node = self.__remove(node._right, key)
            
        return node
        
    # get max/min methods
    def get_max(self):
        return self.__get_max(self._root)
    
    def _get_max(self, node):
        if node is None:
            return None
        while node._right:
            node = node._right
        return node._item
    
    def get_min(self):
        return self.__get_min(self._root)
    
    def _get_min(self, node):
        if node is None:
            return None
        while node._left:
            node = node._left
        return node._item
    
    # Traversal Methods
    def preorder_traversal(self):
        self.__preorder(self._root)
        print()
        
    def __preorder(self, node):
        if node is None:
            return 
        print('{' , node._item , '}', end=" ") 
        self.__preorder(node._left)
        self.__preorder(node._right)
        
    def inorder_traversal(self):
        self.__inorder(self._root)
        print()
        
    def __inorder(self, node):
        if node is None:
            return 
        self.__inorder(node._left)
        print('{' , node._item, '}', end=" ")
        self.__inorder(node._right)
        
    def postorder_traversal(self):
        self.__postorder(self._root)
        print()
        
    def __postorder(self, node):
        if node is None:
            return 
        self.__postorder(node._left)
        self.__postorder(node._right)
        print('{' , node._item , '}', end=" ")
