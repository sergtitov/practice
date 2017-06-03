from collections import deque

class Trie(object):
    def __init__(self, words):
        self.trie = {}        
        for word in words:
            subtrie = self.trie
            for letter in word:
                subtrie = subtrie.setdefault(letter, {})
    
    def print_trie(self):
        queue = deque([(key, self.trie[key]) for key in self.trie])
        while len(queue):
            # Get all the elements
            elements = list(queue)
            # For every element, print and add its children to the queue
            for item, subtrie in elements:
                print item,
                queue.popleft()
                queue.extend([(key, subtrie[key]) for key in subtrie])
            print
            
        
    def is_word_in_trie(self, word):
        subtrie = self.trie
        for letter in word:
            node = subtrie.get(letter)
            if node is None:
                return False
            subtrie = node

        return True    
    
    
words = ['Mama', 'Papa', 'Mad', 'Man', 'Papirus', 'Baby', 'Bay']
trie = Trie(words)

trie.print_trie()

print 'Mama', trie.is_word_in_trie('Mama')
print 'Mamo', trie.is_word_in_trie('Mamo')
