# a. Create holiday.txt and write 5 lines
def write_holiday_file():
    f=open("holiday.txt", "w") 
    f.writelines(["I love Computer Science.\n",
            "Python is fun to learn.\n",
            "Coding improves logic skills.\n",
            "Debugging helps understand errors.\n",
            "Technology makes life easier.\n"
        ])
    f.close()

# b. Count lines, words, and characters
def count_lwc(filename):
    f=open(filename, "r")
    lines = f.readlines()
    lines_count = len(lines)
    chars=f.read()
    L=chars.split()
    words_count = len(L)
    chars_count = (len(chars))
    return lines_count, words_count, chars_count
    f.close()

# c. Print lines without 'a'
def print_lines_without_a(filename):
    f=open(filename, "r")
    data=f.readlines()
    for line in data:
            if 'a' not in line.lower():
                print(line)
    f.close()           

# Example usage
write_holiday_file()  # Create the file with holiday lines
print("Lines, Words, Characters in holiday.txt:", count_lwc("holiday.txt"))  # Count lines, words, and characters

print("Lines without 'a' in holiday.txt:" )
print_lines_without_a("holiday.txt")  # Print lines without 'a'