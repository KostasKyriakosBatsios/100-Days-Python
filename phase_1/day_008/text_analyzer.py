# Day 8 26/8/26!

def main():
    print("=== Text Analyzer ===")

    # Ask the user to enter a text
    text = get_input("\nEnter a text: ")

    print("\n=== Analysis ===\n")

    # Count the characters (with and without spaces), words and sentences in the text
    char_spaces_count = len(text)

    words = text.split()
    words_count = 0
    char_no_spaces_count = 0
    for w in words:
        words_count += 1
        for c in w:
            char_no_spaces_count += 1

    sentences_count = 0
    for c in text:
        if c in ['.', '!', '?']:
            sentences_count += 1

    print(f"Characters (with spaces): {char_spaces_count}\nCharacters (without spaces): {char_no_spaces_count}\nWords: {words_count}\nSentences: {sentences_count}")

    # Lets find the most common word in the text, average word length, longest and shortest word in the text
    word_freq = {}
    for w  in words:
        if w in word_freq:
            word_freq[w] += 1
        else:
            word_freq[w] = 1

    # Also, lets find the most common character in the text
    char_freq = {}
    for c in text:
        if c not in [' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '!', '?']:
            if c in char_freq:
                char_freq[c] += 1
            else:
                char_freq[c] = 1

    most_common_word = max(word_freq, key=word_freq.get)
    most_common_character = max(char_freq, key=char_freq.get)
    avg_word_length = char_no_spaces_count / words_count
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)

    print(f"\nMost common word: {most_common_word}\nOccurences: {word_freq[most_common_word]}\n\nAverage word length: {avg_word_length:.2f}\n\nLongest word: {longest_word}\nShortest word: {shortest_word}\n\nMost common letter: {most_common_character}\nOccurences: {char_freq[most_common_character]}")

# Function to get user input
def get_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()

        # Make sure (obviously if the text isn't empty) that the spaces between the words are not more than 1 space
        if "  " in user_input:
            print("Please make sure there are no more than 1 space between words.")
            continue

        if user_input != "":
            break

    return user_input

main()