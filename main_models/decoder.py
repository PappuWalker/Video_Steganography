def binary_to_text(binary_string):
    # Ensure the binary string length is a multiple of 8
    if len(binary_string) % 8 != 0:
        print("Warning: Binary string length is not a multiple of 8. Padding with zeros.")
        binary_string = binary_string.ljust((len(binary_string) + 7) // 8 * 8, '0')

    text = ""
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        text += chr(int(byte, 2))
    return text

# Example usage
binary_message = input("Enter the binary message: ")
decoded_text = binary_to_text(binary_message)
print(f"Decoded text: {decoded_text}")