# Update Operation

**Command:**
```python
# Retrieve the book
retrieved_book = Book.objects.get(title="1984")

# Update the title
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

print(retrieved_book)
