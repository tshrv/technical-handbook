"""
Memory Management in Python

1. Stack Memory
2. Heap Memory

# Stack Memory
methods, method calls, references local to a function is present in the stack (when the function is called it is pushed onto the stack along with these things)

# Heap Memory
Not the heap data structure but just a pile of memory.
Any values, objects, that are present in the global namespace or to be shared between the functions, is stored in the heap


# Garbage Collection
Cleared via reference counter(python keeps track of names/labels refering to a memory location, when it becomes zero, the object is deleted)

Flaw -> cyclical references x = []; x.append(x)
When allocations - deallocation > threshold, generalization garbage collection is run which identifies such cases and deletes them.
Can be manually done by the gc module with gc.collect method
"""