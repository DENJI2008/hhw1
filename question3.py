# a. Read file and display words with #
def display_words_hash(filename):
    f=open(filename, "r") # Open the file in read mode
    for line in f:
        print('#'.join(line.split()))
    f.close()

# b. Count vowels, consonants, upper, lower
def count_characters(filename):
    f=open(filename, "r")
    text = f.read()
    vowels = 0
    consonants = 0
    upper = 0
    lower = 0
    for i in range(len(text)):
        if text[i] in 'aeiouAEIOU':
            vowels= vowels+1
        if text[i] not in 'aeiouAEIOU' and text[i].isalpha():
            consonants = consonants+1
        if text[i].isupper():
            upper = upper+1
        if text[i].islower():     
            lower = lower+1
    return vowels, consonants, upper, lower
    f.close()

# c. Remove lines with 'a' and write to another file
def remove_lines_with_a(src, dest):
    f1=open(src, "r+")
    f2=open(dest, "w")
    for line in f1:
        if 'a' not in line.lower():
            f2.write(line)
    f1.close()
    f2.close()

# d. Binary file: create & search
import pickle
def create_binary(data, filename):
    f=open(filename, "wb")
    pickle.dump(data, f)

def search_roll(filename, roll):
    f=open(filename, "rb")
    data = pickle.load(f)
    for record in data:
        if record['roll'] == roll:
            return record['name']
    return "Roll not found."

# e. Binary file: update marks
def update_marks(filename, roll, new_marks):
    f=open(filename, "rb")
    data = pickle.load(f)
    for record in data:
        if record['roll'] == roll:
            record['marks'] = new_marks
            break
    f=open(filename, "wb")
    pickle.dump(data, f)

# f. Random number generator (dice simulation)
import random
def roll_dice():
    return random.randint(1, 6)

# Example usage

display_words_hash("example.txt")  # Display words with #  # Count characters
print("Vowels, Consonants, Uppercase, Lowercase in example.txt:", count_characters("example.txt"))  # Count vowels, consonants, upper, lower
remove_lines_with_a("example.txt", "no_a_lines.txt")  # Remove lines with 'a' and write to another file
# Create binary file and search roll number
data = [{'roll': 1, 'name': 'Alice', 'marks': 85},
        {'roll': 2, 'name': 'Bob', 'marks': 90},
        {'roll': 3, 'name': 'Charlie', 'marks': 78}]
create_binary(data, "students.dat")  # Create binary file
print(search_roll("students.dat", 2))  # Search for roll number 2
update_marks("students.dat", 2, 95)  # Update marks for roll number 2
print(search_roll("students.dat", 2))  # Verify updated marks
# Simulate rolling a dice
print("Dice rolled:", roll_dice())  # Roll the dice and print the result