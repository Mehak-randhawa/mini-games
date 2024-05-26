#This project reads a story from a file, 
#identifies placeholder words marked by "<>" tags, 
#prompts the user to input words for these placeholders, 
#replaces the placeholders with the user's input, and then prints the modified story. 
#It essentially creates a customizable story 
#by filling in user-provided words for placeholders in the original text.
# Open the story file in read mode
with open("story.txt", "r") as f:
    story = f.read()

words = set()  # Create a set of all our unique words
start_of_word = -1

target_start = "<"
target_end = ">"

# Locate the start and end of each placeholder word in our story
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word:i+1]  # Grab the word and put it in our set
        words.add(word)
        start_of_word = -1

# Ask user to generate answers for each placeholder word
answers = {}

for word in words:
    answers[word] = input(f"Enter a word for {word}: ")

# Replace all placeholder words with the user's answers
for word in words:
    story = story.replace(word, answers[word])

# Print the final story
print(story)
