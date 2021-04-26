# Written by: Vy Hoang
# Program: Concert seat assignments - using nested if conditions
# This program provides concert seat assignments based on the potential input.

# Get user input for musical preference
music = input('Please enter your musical preference: ')

# Proceed to get user's information if the musicical preference = "classical"
if music.lower() == "classical":
    first_name = input('Enter your first name: ')
    last_name = input('\nEnter your last name: ')
    membership = input('\nEnter your membership level (composer, conductor or musician): ')
    seat = input('\nEnter your seat preference (Orchestra, Main, Balcony): ')
    meal = input('\nEnter your meal type (Chicken, Fish, Vegan): ')

    # Display messages based on criteria
    if membership.lower() == "composer":
        if seat.lower() == "orchestra":
            print('{} {}, You qualify for these exeptional seats!'
                  .format(first_name.capitalize(), last_name.capitalize()))
        if seat.lower() == "main":
            print('{} {}, The seats in the main section are good seats.'
                  .format(first_name.capitalize(), last_name.capitalize()))
        if seat.lower() == "balcony":
            print('{} {}, Interesting, let us know if you want closer seats.'
                  .format(first_name.capitalize(), last_name.capitalize()))

    if membership.lower() == "conductor":
        if seat.lower() == "orchestra":
            print('{} {}, Member level of Composer required if you want to sit '
                  'in the orchestra section!'
                  .format(first_name.capitalize(), last_name.capitalize()))
        if seat.lower() == "main":
            print('{} {}, The seats in the main section are good seats.'
                  .format(first_name.capitalize(), last_name.capitalize()))
        if seat.lower() == "balcony":
            print('{} {}, Interesting, let us know if you want closer seats.'
                  .format(first_name.capitalize(), last_name.capitalize()))

    if membership.lower() == "musician":
        if seat.lower() == "orchestra":
            print('{} {}, Member level of Composer required if you want to sit '
                  'in the orchestra section!'
                  .format(first_name.capitalize(), last_name.capitalize()))
        if seat.lower() == "main":
            print('{} {}, Member level of Composer or Conductor required if you want to sit '
                  'in the main section!'
                  .format(first_name.capitalize(), last_name.capitalize()))
        if seat.lower() == "balcony":
            print('{} {}, Your balcony seats are confirmed.'
                  .format(first_name.capitalize(), last_name.capitalize()))


    # Create a list to hold survey scores.
    list_survey = ["The concert was wonderful.",
                   "The food was fantastic.",
                   "The seats were superb."]
    list_scores = []
    total = 0
    # Get user to input a sentiment score for the survey
    for survey in list_survey:
        scores = int(input('\nEnter score 1 - 5 (1 = strongly disagree; 5 = strongly agree) '
                           '\nfor "{}": '.format(survey)))
        list_scores.append(scores)
        total += scores

    # Determine any score <4 or <3 or <2
    any_score_lt4 = False
    any_score_lt3 = False
    any_score_lt2 = False
    for score in list_scores:
        if score < 4:
            any_score_lt4 = True
        if score < 3:
            any_score_lt3 = True
        if score < 2:
            any_score_lt2 = True

    # Display messages based on the input scores
    if membership.lower() == "composer":
        if total < 12 or any_score_lt4:
            print('Dear Composer, Your survey score of ', min(list_scores),
                  'was lower than we would like. \nPlease give us another opportunity soon.')
        else:
            print('Thank you for being a Composer member and for having a good time!')

    if membership.lower() == "conductor":
        if total < 11 or any_score_lt3:
            print('Dear Conductor, Your survey score of ', min(list_scores),
                  'was lower than we would like. \nThe next time you attend we will be nicer.')
        else:
            print('Thank you for being a Conductor member and for having a good time!')

    if membership.lower() == "musician":
        if total < 10 or any_score_lt2:
            print('Dear Musician, Your survey score of ', min(list_scores),
                  ' was lower than we would like. \nYou will have more fun next time.')
        else:
            print('Thank you for being a Musician member and for having a good time!')

# Display message and end the program if the musicial preference != "classical")
else:
    print('\nWe do not recognize the {} musical genre. Sorry.'.format(music))






