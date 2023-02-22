import random
from vocabularyList import vocabulary


def generate_word():
    # Choose a random number from total number of dictionaries
    dictionary_length = len(vocabulary)
    random_dictionary = random.randrange(dictionary_length)

    # Choose a random word from the chosen dictionary
    random_translation = random.randrange(0, 1)
    random_word = vocabulary[random_dictionary[random_translation]]
    print(random_word)


generate_word()

# def score_tracker():
#     score = 0
#     user_answer = input(f"Translate the word")
