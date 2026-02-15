"""
Author: Mukhtar Ali
Assignment: #1
"""

# string
gym_member = "Alex Alliton"  # str

# float
preferred_weight_kg = 20.5  # float

# Integer
highest_reps = 25  # int

# Boolean
membership_active = True  # bool


# Dictionary
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 35, 30),
    "Taylor": (25, 50, 40),
    "Jordan": (20, 30, 15)
}

# d) Calculate totals and add new key-value pairs like "Alex_Total"
for friend, minutes_tuple in list(workout_stats.items()):
    total_minutes = sum(minutes_tuple)
    workout_stats[f"{friend}_Total"] = total_minutes

print("Workout stats (with totals):")
for k, v in workout_stats.items():
    print(f"{k}: {v}")

print()


# e) 2D (nested) list (list of lists)
workout_list = []
friends = []

for friend, minutes_tuple in workout_stats.items():
    if not friend.endswith("_Total"):
        friends.append(friend)
        workout_list.append(list(minutes_tuple))

print("workout_list (2D list):")
for i, row in enumerate(workout_list):
    print(f"{friends[i]} -> {row}")

print()


# f) Slicing the workout_list
print("Yoga and running minutes for all friends:")
for i, row in enumerate(workout_list):
    print(f"{friends[i]}: {row[0:2]}")  # yoga + running

print()

# Extract and print the minutes for weightlifting for the last two friends.
print("Weightlifting minutes for the last two friends:")
for i in range(len(workout_list) - 2, len(workout_list)):
    print(f"{friends[i]}: {workout_list[i][2]}")  # weightlifting only

print()


# g) If-statement within a loop: total >= 120
print("Checking who has total workout minutes >= 120:")
for friend in friends:
    total_key = f"{friend}_Total"
    if workout_stats[total_key] >= 120:
        print(f"Great job staying active, {friend}!")

print()


# h) User input feature
name_input = input("Enter a friend's name to look up (e.g., Alex): ").strip()

if name_input in workout_stats and not name_input.endswith("_Total"):
    mins = workout_stats[name_input]
    total = workout_stats[f"{name_input}_Total"]
    print(f"\n{name_input}'s workout minutes:")
    print(f"Yoga: {mins[0]}")
    print(f"Running: {mins[1]}")
    print(f"Weightlifting: {mins[2]}")
    print(f"Total: {total}")
else:
    print(f"Friend {name_input} not found in the records.")

print()


# i) Highest and lowest total workout minutes
highest_friend = None
lowest_friend = None
highest_total = None
lowest_total = None

for friend in friends:
    total = workout_stats[f"{friend}_Total"]
    if highest_total is None or total > highest_total:
        highest_total = total
        highest_friend = friend
    if lowest_total is None or total < lowest_total:
        lowest_total = total
        lowest_friend = friend

print(f"Friend with the highest total workout minutes: {highest_friend} ({highest_total})")
print(f"Friend with the lowest total workout minutes: {lowest_friend} ({lowest_total})")
