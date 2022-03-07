"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
question = input('Please enter your age: ')
age = int(question)
heart = 220 - age
highheart = heart*0.85
lowheart = heart*0.65
print(f'When you excercise to strengthen your heart, you should \nkeep your heart rate between {lowheart:.0f} and {highheart:.0f} beats per minute.')