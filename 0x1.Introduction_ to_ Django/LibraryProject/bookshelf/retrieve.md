# Retrieve Operation

**Command:**
```python
# Retrieve the book
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book)
