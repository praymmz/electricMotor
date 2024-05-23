class Mylist:
        def __init__(self, items = None):
                if items is None:
                    self.items = []
                else:
                    self.items = items

        def add(self, item):
                self.items.append(item)

        def delete(self, item):
                if item in self.items:
                        self.items.remove(item)
                        print(f"{item} has been deleted from the list.")
                else:
                        print(f"{item} not found in the list")

        def length(self):
                return len(self.items)

        def __str__(self):
            return str(self.items)

my_instance = Mylist([1, 2, 3, 4 ,5 ,6 ,7, 8, 9, 10])
my_instance.add(9)
my_instance.delete(2)
