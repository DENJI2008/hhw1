# a. Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# b. Average and grade for 5 subjects
def average_and_grade(m1, m2, m3, m4, m5):
    avg = (m1 + m2 + m3 + m4 + m5) / 5
    if avg >= 90:
        grade = 'A'
    elif avg >= 75:
        grade = 'B'
    elif avg >= 60:
        grade = 'C'
    else:
        grade = 'D'
    return avg, grade

# c. Check palindrome
def is_palindrome(s):
    return s == s[::-1]

print("Factorial of 5:", factorial(5))  # Example usage
print("Average and grade for marks 85, 90, 78, 88, 92:", average_and_grade(85, 90, 78, 88, 92))  # Example usage
print("Is 'radar' a palindrome?", is_palindrome('radar'))  # Example usage