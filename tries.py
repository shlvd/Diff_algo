class TrieNode:
    """
    A class representing a node of a TRIE data structure.
    We denote the multiple children of a node using a list.
    If this node represents an end of a key, then end_of_key would be True.
    """
    def __init__(self):
        self.children = [None] * 26    # No. of Alphabets.
        self.end_of_key = False       # Denotes if the node is end of a key


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def _char_to_index(char):
        return ord(char) - ord('a')

    def insert(self, key):
        """
        Insert a key into Trie data structure.
        :param key: Key to be inserted into Trie.
        :return: None.
        """
        key = key.lower()

        current_node = self.root
        for level in range(len(key)):
            index = self._char_to_index((key[level]))

            if current_node.children[index] is None:
                current_node.children[index] = TrieNode()

            current_node = current_node.children[index]

        current_node.end_of_key = True

    def search(self, key):
        """
        Search for a key in Trie.
        :param key: Key to be search for
        :return: True if key is present. False otherwise
        """
        key = key.lower()

        current_node = self.root
        for level in range(len(key)):
            index = self._char_to_index(key[level])

            if current_node.children[index] is None:
                return False

            current_node = current_node.children[index]
        return current_node is not None and current_node.end_of_key
