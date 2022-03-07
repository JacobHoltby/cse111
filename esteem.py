print('This program is an implementation of the Rosenberg')
print('Self-Esteem Scale. This program will show you ten')
print('statements that you could possibly apply to yourself.')
print('Please rate how much you agree with each of the')
print('statements by responding with one of these four letters:')
print('')

print('D means you strongly disagree with the statement.')
print('d means you disagree with the statement.')
print('a means you agree with the statement.')
print('A means you strongly agree with the statement.')

print('1. I feel that I am a person of worth, at least on \
    an equal plane with others.')
q1 = input('Enter D, d, a, or A: ')
print('2. I feel that I have a number of good qualities.')
q2 = input('Enter D, d, a, or A: ')
print('3. All in all, I am inclined to feel that I am a failure.')
q3 = input('Enter D, d, a, or A: ')
print('4. I am able to do things as well as most other people.')
q4 = input('Enter D, d, a, or A: ')
print('5. I feel I do not have much to be proud of.')
q5 = input('Enter D, d, a, or A: ')
print('6. I take a positive attitude toward myself.')
q6 = input('Enter D, d, a, or A: ')
print('7. On the whole, I am satisfied with myself.')
q7 = input('Enter D, d, a, or A: ')
print('8. I wish I could have more respect for myself.')
q8 = input('Enter D, d, a, or A: ')
print('9. I certainly feel useless at times.')
q9 = input('Enter D, d, a, or A: ')
print('10. At times I think I am no good at all.')
q10 = input('Enter D, d, a, or A: ')
print('')

if q1 == 'D':
    point1 = 0
if q1 == 'd':
    point1 = 1
if q1 == 'a':
    point1 = 2
if q1 == 'A':
    point1 = 3
else:
    pass

if q2 == 'D':
    point2 = 0
if q2 == 'd':
    point2 = 1
if q2 == 'a':
    point2 = 2
if q2 == 'A':
    point2 = 3
else:
    pass

if q4 == 'D':
    point4 = 0
if q4 == 'd':
    point4 = 1
if q4 == 'a':
    point4 = 2
if q4 == 'A':
    point4 = 3
else:
    pass

if q6 == 'D':
    point6 = 0
if q6 == 'd':
    point6 = 1
if q6 == 'a':
    point6 = 2
if q6 == 'A':
    point6 = 3
else:
    pass

if q7 == 'D':
    point7 = 0
if q7 == 'd':
    point7 = 1
if q7 == 'a':
    point7 = 2
if q7 == 'A':
    point7 = 3
else:
    pass

    
if q3 == 'D':
    point3 = 3
if q3 == 'd':
    point3 = 2
if q3 == 'a':
    point3 = 1
if q3 == 'A':
    point5 = 0
else:
    pass
    
if q5 == 'D':
    point5 = 3
if q5 == 'd':
    point5 = 2
if q5 == 'a':
    point5 = 1
if q5 == 'A':
    point5 = 0
else:
    pass
    
if q8 == 'D':
    point8 = 3
if q8 == 'd':
    point8 = 2
if q8 == 'a':
    point8 = 1
if q8 == 'A':
    point8 = 0
else:
    pass
    
if q9 == 'D':
    point9 = 3
if q9 == 'd':
    point9 = 2
if q9 == 'a':
    point9 = 1
if q9 == 'A':
    point9 = 0
else:
    pass
    
if q10 == 'D':
    point10 = 3
if q10 == 'd':
    point10 = 2
if q10 == 'a':
    point10 = 1
if q10 == 'A':
    point10 = 0
else:
    pass

score = point1 + point2 + point3 + point4 + point5 + point6 + \
    point7 + point8 + point9 + point10 
print(f'Your score is {score}.')
print('A score below 15 may indicate problematic low self-esteem.')
