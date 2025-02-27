## 1. HEAPS
class MinHeap:
    def __init__(self):
        self.a = [] # Initialize an empty list to represent the heap

    """Insert a new element into the Min Heap."""
    def insert(self, val):
        self.a.append(val) # Add the new value at the end
        i = len(self.a) - 1 # Index of the newly added element

        # "Bubble Up" process to maintain heap property
        while i > 0 and self.a[(i - 1) // 2] > self.a[i]:
            # Swap the new element with its parent if it's smaller
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i] # swap positions
            i = (i - 1) // 2 # Move up to the parent's index

    """Delete a specific element from the Min Heap."""
    def delete(self, value):
        i = -1 # To find the index of the value
        for j in range(len(self.a)):
            if self.a[j] == value:
                i = j # found
                break
        if i == -1:
            return # Value not found
        
        # Replace the element with the last one and remove the last, because it's duplate it now
        self.a[i] = self.a[-1]
        self.a.pop()

        # But the last method brokes the rule, because unsort the array. So, here's where heapify / bubble down take action.

        # "Bubble Down" to restore heap property
        while True:
            left = 2 * i + 1 # left chield
            right = 2 * i + 2 # right child
            smallest = i

            
            if left < len(self.a) and self.a[left] < self.a[smallest]:
                smallest = left
            if right < len(self.a) and self.a[right] < self.a[smallest]:
                smallest = right
            if smallest != i:
                self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
                i = smallest
            else:
                break

    """Heapify function to maintain the heap property.""" 
    def minHeapify(self, i, n):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.a[left] < self.a[smallest]:
            smallest = left
        if right < n and self.a[right] < self.a[smallest]:
            smallest = right
        if smallest != i:
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            self.minHeapify(smallest, n)

    """Search for an element in the Min Heap."""
    def search(self, element):
        for j in self.a:
            if j == element:
                return True
        return False

    def getMin(self):
        return self.a[0] if self.a else None

    def printHeap(self):
        print("Min Heap:", self.a)

# Example Usage
if __name__ == "__main__":
    h = MinHeap()
    values = [10, 7, 11, 5, 4, 13]
    for value in values:
        h.insert(value)
    h.printHeap()
    
    h.delete(7)
    print("Heap after deleting 7:", h.a)
    
    print("Searching for 10 in heap:", "Found" if h.search(10) else "Not Found")
    print("Minimum element in heap:", h.getMin())
