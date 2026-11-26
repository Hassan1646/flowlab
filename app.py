
def greet(name, greeting="Hi"):
    return f"{greeting}, {name}!"


def farewell(name):
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    print(greet("world"))