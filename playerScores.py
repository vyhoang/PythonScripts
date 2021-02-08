# program03: Compare three numbers

print('This program records goals for Soccer players '
      'and points for basketball players.')

print('Please enter three names of Soccer players.\n')
soccer1 = input('Name of Soccer player 1: ')
soccer2 = input('Name of Soccer player 2: ')
soccer3 = input('Name of Soccer player 3: ')

print('\nPlease enter career goals for each Soccer player.\n')
goal1 = int(input('Career goals for soccer player {}: '.format(soccer1)))
goal2 = int(input('Career goals for soccer player {}: '.format(soccer2)))
goal3 = int(input('Career goals for soccer player {}: '.format(soccer3)))

print('Soccer Players in sorted order:')
if (goal1 >= goal2) and (goal1 >= goal3):
    if goal2 >= goal3:
        print(soccer1, '-', goal1)
        print(soccer2, '-', goal2)
        print(soccer3, '-', goal3)
    else:
        print(soccer1, '-', goal1)
        print(soccer3, '-', goal3)
        print(soccer2, '-', goal2)

elif (goal2 >= goal1) and (goal2 >= goal3):
    if goal1 >= goal3:
        print(soccer2, '-', goal2)
        print(soccer1, '-', goal1)
        print(soccer3, '-', goal3)
    else:
        print(soccer2, '-', goal2)
        print(soccer3, '-', goal3)
        print(soccer1, '-', goal1)

else:  # g3>=g1 and g3 >=g2
    if goal1 >= goal2:
        print(soccer3, '-', goal3)
        print(soccer1, '-', goal1)
        print(soccer2, '-', goal2)
    else:
        print(soccer3, '-', goal3)
        print(soccer2, '-', goal2)
        print(soccer1, '-', goal1)


print('Please enter three names of Basketball players.\n')
basketball1 = input('Name of Basketball player 1: ')
basketball2 = input('Name of Basketball player 2: ')
basketball3 = input('Name of Basketball player 3: ')

print('Please enter career points for each basketball player.\n')
point1 = int(input('Career points for basketball player {}: '.format(basketball1)))
point2 = int(input('Career points for basketball player {}: '.format(basketball2)))
point3 = int(input('Career points for basketball player {}: '.format(basketball3)))

print('Basketball Players in sorted order:')
if (point1 >= point2) and (point1 >= point3):
    max_points = point1
    if point2 >= point3:
        print(basketball1, '-', point1)
        print(basketball2, '-', point2)
        print(basketball3, '-', point3)
    else:
        print(basketball1, '-', point1)
        print(basketball3, '-', point3)
        print(basketball2, '-', point2)

elif (point2 >= point1) and (point2 >= point3):
    max_points = point2
    if point1 >= point3:
        print(basketball2, '-', point2)
        print(basketball1, '-', point1)
        print(basketball3, '-', point3)
    else:
        print(basketball2, '-', point2)
        print(basketball3, '-', point3)
        print(basketball1, '-', point1)

else:  # p3>=p1 and p3 >=p2
    max_points = point3
    if point1 >= point2:
        print(basketball3, '-', point3)
        print(basketball1, '-', point1)
        print(basketball2, '-', point2)
    else:
        print(basketball3, '-', point3)
        print(basketball2, '-', point2)
        print(basketball1, '-', point1)


