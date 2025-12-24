def print_string(value):
    if not isinstance(value, str):
        print("Error: expected a string.")
        return
    print(value)


def analyze_string_case(value):
    if not isinstance(value, str):
        print("Error: expected a string.")
        return
    
    if value.isupper():
        print("All letters are uppercase.")
    elif value.islower():
        print("All letters are lowercase.")
    else:
        print("Mixed case.")


def uppercase_list(word):
    if not isinstance(word, str):
        print("Error: expected a string.")
        return []
    return [char.upper() for char in word]