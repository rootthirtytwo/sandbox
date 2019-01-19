class Queue:

    def __init__(self):
        self.queue = list()

    def add_item(self, item):
        if item not in self.queue:
            self.queue.insert(0, item)
            # self.queue.insert(len(self.queue), item)

    def delete_item(self):
        if len(self.queue) > 0:
            self.queue.pop()
            # self.queue.remove(self.queue[0])

    def queue_len(self):
        return len(self.queue)

    def print_queue(self):
        if len(self.queue) > 0:
            return self.queue

q = Queue()

print("Push A ")
q.add_item('A')
print("Push B ")
q.add_item('B')
print("Push C ")
q.add_item('C')
print("Length of the queue ",q.queue_len())
print("Items in the queue ", q.print_queue())

print("\nPop an item from the queue", sep='\n')
q.delete_item()
print("Items in the queue after pop", q.print_queue())


