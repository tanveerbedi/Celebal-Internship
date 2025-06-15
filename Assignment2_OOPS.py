from datetime import datetime

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"✅ Node '{data}' added at {datetime.now().strftime('%H:%M:%S')}")

    def print_list(self):
        if self.head is None:
            print("📭 The list is currently empty.")
            return
        current = self.head
        print("🧾 Linked List content:")
        while current:
            print(f"[ {current.data} ] -> ", end="")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        try:
            if self.head is None:
                raise Exception("Cannot delete from an empty list.")
            if n <= 0:
                raise IndexError("Index must be 1 or greater.")
            if n == 1:
                deleted = self.head.data
                self.head = self.head.next
                print(f"🗑️ Deleted node with data '{deleted}' at {datetime.now().strftime('%H:%M:%S')}")
                return
            current = self.head
            count = 1
            while count < n - 1 and current.next:
                current = current.next
                count += 1
            if current.next is None:
                raise IndexError("Index out of range.")
            deleted = current.next.data
            current.next = current.next.next
            print(f"🗑️ Deleted node with data '{deleted}' at {datetime.now().strftime('%H:%M:%S')}")
        except Exception as e:
            print("❌ Error:", e)

    def delete_by_value(self, value):
        try:
            if self.head is None:
                raise Exception("Cannot delete from an empty list.")
            if self.head.data == value:
                self.head = self.head.next
                print(f"🗑️ Deleted node with value '{value}' at {datetime.now().strftime('%H:%M:%S')}")
                return
            current = self.head
            while current.next and current.next.data != value:
                current = current.next
            if current.next is None:
                raise ValueError("Value not found in the list.")
            current.next = current.next.next
            print(f"🗑️ Deleted node with value '{value}' at {datetime.now().strftime('%H:%M:%S')}")
        except Exception as e:
            print("❌ Error:", e)

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"📊 The list currently has {count} node(s).")

    def search_value(self, value):
        current = self.head
        position = 1
        while current:
            if current.data == value:
                print(f"🔍 Value '{value}' found at position {position}.")
                return
            current = current.next
            position += 1
        print(f"❌ Value '{value}' not found in the list.")

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("🔁 Linked List reversed.")

    def save_to_file(self, filename="linked_list_output.txt"):
        try:
            with open(filename, "w") as file:
                current = self.head
                while current:
                    file.write(str(current.data) + " -> ")
                    current = current.next
                file.write("None\n")
            print(f"💾 List saved to '{filename}'")
        except Exception as e:
            print("❌ Error saving file:", e)


def main():
    print("👋 Welcome to Linked List Playground Game (by Tanveer Singh)")
    ll = LinkedList()

    while True:
        print("\n📘 Menu:")
        print("1. ➕ Add a node")
        print("2. 📄 Print the list")
        print("3. ❌ Delete node by position")
        print("4. ❌ Delete node by value")
        print("5. 📏 Show list size")
        print("6. 🔍 Search for a value")
        print("7. 🔁 Reverse the list")
        print("8. 💾 Save list to a file")
        print("9. 🚪 Exit")

        choice = input("Enter your choice (1–9): ")

        if choice == '1':
            value = input("Enter value to add: ")
            ll.add_node(value)
        elif choice == '2':
            ll.print_list()
        elif choice == '3':
            try:
                n = int(input("Enter 1-based index of node to delete: "))
                ll.delete_nth_node(n)
            except ValueError:
                print("❌ Please enter a valid integer.")
        elif choice == '4':
            value = input("Enter value of node to delete: ")
            ll.delete_by_value(value)
        elif choice == '5':
            ll.get_length()
        elif choice == '6':
            value = input("Enter value to search: ")
            ll.search_value(value)
        elif choice == '7':
            ll.reverse_list()
        elif choice == '8':
            ll.save_to_file()
        elif choice == '9':
            print("👋 Exiting... Have a great day!")
            break
        else:
            print("⚠️ Invalid option. Choose from 1 to 9.")


if __name__ == "__main__":
    main()
