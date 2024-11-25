# Pig Latin

SUFFIX = "ay"

def pig_word( word: str) -> str:
    """ translate a word to pig latin."""
    return word[1:] + word[0] + SUFFIX

def main()->None:
    word = input("Enter a word: ")
    print(f"{word} translated is {pig_word(word)}")

main()
