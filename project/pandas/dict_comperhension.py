import random
names = ['Dhu', 'Cal', 'Pat', 'Man', 'Ash']
students_score = {name:random.randint(1, 100) for name in names}

passed_students = { key:value for (key,value) in students_score.items() if value > 40}

# Example 2
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
result = {word:len(word) for word in sentence.split()}

print(result)

# Example 3
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
weather_f = {new_key:((new_value * 9/5) + 32) for (new_key, new_value) in weather_c.items()}

# Write your code 👇 below:
print(weather_f)
