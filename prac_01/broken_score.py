"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# TODO: Fix this!
EXCELLENT_THRESHOLD = 90
PASSED_THRESHOLD = 50

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= EXCELLENT_THRESHOLD:
    print("Excellent")
elif score >= PASSED_THRESHOLD:
    print("Pass")
else:
    print("Bad")
