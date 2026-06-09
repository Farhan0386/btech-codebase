def greet(name , greeting='Hello'):
    """Return a greeting string."""
    return f"{greeting},{name}"

msg=greet("Farhan")
print(msg)
print(greet("Bob", "Hi"))