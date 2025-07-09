import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class BSTNode:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def build_tree(self, dataset):
        sorted_dataset = sorted(dataset, key=lambda x: x[0])
        self.root = self._build_tree_from_sorted_data(sorted_dataset)

    def _build_tree_from_sorted_data(self, dataset):
        if not dataset:
            return None

        # median sebagai root
        mid = len(dataset) // 2
        key, data = dataset[mid]
        root = BSTNode(key, data)

        root.left = self._build_tree_from_sorted_data(dataset[:mid])  # Data kiri dari median
        root.right = self._build_tree_from_sorted_data(dataset[mid+1:])  # Data kanan dari median
        return root

    def insert(self, key, data=None):
        self.root = self._insert_recursive(self.root, key, data)

    def _insert_recursive(self, node, key, data):
        if node is None:
            return BSTNode(key, data)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key, data)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, data)
        return node

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def count_occurrences(self, key):
        return self._count_occurrences_recursive(self.root, key)

    def _count_occurrences_recursive(self, node, key):
        if node is None:
            return 0
        count = 0
        if node.key == key:
            count += 1
        count += self._count_occurrences_recursive(node.left, key)
        count += self._count_occurrences_recursive(node.right, key)
        return count

    def print_inorder(self, node):
        if node:
            self.print_inorder(node.left)
            print(f"{node.key}: {node.data}")
            self.print_inorder(node.right)

class BSTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BST Search Application")

        self.bst = BinarySearchTree()

        self.upload_button = tk.Button(root, text="Upload Dataset", command=self.upload_dataset)
        self.upload_button.pack(pady=10)

        self.search_label = tk.Label(root, text="Enter keyword to search:")
        self.search_label.pack()

        self.search_entry = tk.Entry(root)
        self.search_entry.pack(pady=5)

        self.search_button = tk.Button(root, text="Search", command=self.search_word)
        self.search_button.pack(pady=10)

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack(pady=10)

    def upload_dataset(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                df = pd.read_csv(file_path)
                sorted_data = sorted(zip(df['word'].astype(str), df['definition']), key=lambda x: x[0])
                self.bst.build_tree(sorted_data)
                messagebox.showinfo("Success", "Dataset uploaded and BST built successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to upload dataset: {e}")

    def search_word(self):
        keyword = self.search_entry.get().strip()
        if not keyword:
            messagebox.showwarning("Input Required", "Please enter a keyword to search.")
            return

        result_node = self.bst.search(keyword)
        self.result_text.delete(1.0, tk.END)

        if result_node:
            self.result_text.insert(tk.END, f"Keyword: {keyword}\n")
            self.result_text.insert(tk.END, f"Definition: {result_node.data}\n")
        else:
            self.result_text.insert(tk.END, f"Keyword '{keyword}' not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BSTApp(root)
    root.mainloop()
