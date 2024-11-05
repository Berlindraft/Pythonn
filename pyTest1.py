class Parent:
    def __init__(self, data=None):
        if data is None:
            data = {}  # Avoid mutable default arguments
        self.data = data

    def add_entry(self, key, value):
        self.data[key] = value
        
    def show_values(self):
        for key, values in self.data.items():
            print(key, values)

class Child(Parent):
    def __init__(self, data=None):
        super().__init__(data)  # Passing the dictionary to the parent class

    def update_entries(self, updates):
        self.data.update(updates)  # Update multiple dictionary entries

# Create an instance of Child and modify the dictionary
child = Child({"name": "Alice", "age": 30})
child.add_entry("city", "New York")
child.update_entries({"age": 31, "job": "Engineer"})
child.show_values()

print(child.data)  
# Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'job': 'Engineer'}
