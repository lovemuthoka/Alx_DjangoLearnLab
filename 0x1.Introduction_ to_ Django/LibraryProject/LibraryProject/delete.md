# Delete Operation

**Command:**
```python
# Retrieve the book
retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
retrieved_book.delete()

# Verify deletion
try:
    Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("The book has been deleted.")
