def calculate_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

grades_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
all_scores = []

print("Enter student scores. Type 'done' when finished.")

while True:
    entry = input("Score (or 'done'): ")
    if entry.lower() == 'done':
        break
    score = float(entry)
    all_scores.append(score)
    grade = calculate_grade(score)
    grades_count[grade] += 1
    print(f"-> Grade: {grade}")

print("\n--- Final Report ---")
for g, count in grades_count.items():
    print(f"{g}: {count} students")

if all_scores:
    average = sum(all_scores) / len(all_scores)
    print(f"\nClass Average: {average:.2f}")