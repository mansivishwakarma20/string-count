def count_vowels_and_consonants(input_string):
    """Count the number of vowels and consonants in a string."""
    vowels = "aeiouAEIOU"  # Define vowels (both lowercase and uppercase)
    vowel_count = 0
    consonant_count = 0

    for char in input_string:
        if char.isalpha():  # Check if the character is alphabetic
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Main execution
if __name__ == "__main__":
    user_input = input("Enter a string: ")
    vowels, consonants = count_vowels_and_consonants(user_input)
    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")