def analyze_string(user_input):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    special_char_count = 0
    frequency = {}

    for char in user_input:
        if char.isalpha():  # Checks if it's a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():
            digit_count += 1
        elif not char.isspace():  # skip spaces
            special_char_count += 1

        # Frequency count using dictionary
        char_lower = char.lower()
        if char_lower != " ":
            frequency[char_lower] = frequency.get(char_lower, 0) + 1

    # Output
    print("\n--- String Analysis ---")
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"Digits: {digit_count}")
    print(f"Special Characters: {special_char_count}")
    
    print("\nCharacter Frequency:")
    for char, count in frequency.items():
        print(f"'{char}': {count}")

# Main Program
if __name__ == "__main__":
    user_input = input("Enter a string to analyze: ")
    analyze_string(user_input)
