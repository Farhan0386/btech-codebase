def detect_type(value_str):
    try:
        int(value_str)
        return int, int(value_str)
    except ValueError:
        pass
    try:    
        float(value_str)
        return float, float(value_str)
    except ValueError:
        pass
    return str, value_str

user_input = input("Enter a value: ")
detected_type, converted = detect_type(user_input)
print(f"Detected type: {detected_type.__name__}")
print(f"Converted value: {converted}")
print(f"isinstance int? {isinstance(converted, int)}")