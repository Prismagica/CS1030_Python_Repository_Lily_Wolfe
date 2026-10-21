# This program asks for your name and calculates your average and highest test scores
# It contains several errors (syntax, runtime, and logic) for you to find and fix
# Changed into a string
print(f'"Welcome to the Debugging Lab!')
# Changed into a f-string for consistency
name = input("Enter your name: ")
print(f"Hello {name}! Let's calculate your test scores.")
# Removed the extra quotation marks on 88.
scores = [85, 90, 78, 88, 92]

total = 0
for score in scores:
    total = total + score

average = total / len(scores)
# Added f-string to print the average score and added the missing brackets on "average"
print(f"Your average score is: {average}")

highest = 0
for s in scores:
    if s > highest:
        highest = s

print(f"Your highest score was: {highest}")