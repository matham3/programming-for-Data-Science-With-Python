 

import pandas as pd
import numpy as np
import datetime as dt
import time
 

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york', 'washington']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the city you want see data for Chicago , New York City or Washington:" )
    city = city.casefold()
    while True:
       city = input('Which city do you want to explore Chicago New York or Washington?\n> ').lower()
       if city in CITIES:
           break



    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Enter the month from January to June OR Enter "all" for no month filter :')
    month = month.casefold()
    while month not in months:
        month = input("Invalid month name.Please Try Again!")
        month = month.casefold()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
    day = input('Enter the day from Monday to Sunday OR Enter "all" for no day filter : ')
    day = day.casefold()
    while day not in days:
        day = input('Invalid day name.Please Try Again!')
        day = day.casefold()
    print('-----'*50)
    return city, month, day


 


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    # Converting the Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    







def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    # Finding the most common month of the year from 1 to 12
    popular_monthw = df['month'].mode()[0]
    month = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most Popular Month:', month[popular_monthw-1])





    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    # Finding the most common day of the week from 0 to 6
    popular_days = df['day_of_weeks'].mode()[0]
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('Most Popular Days:', day[popular_days])



    # TO DO: display the most common start hour
    df['hours'] = df['Start_Time'].dt.hour
    popular_hours = df['hours'].mode()[0]
    print('Start Hour:', popular_hours)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)









def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Start Station: ', df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('End Station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('display most frequent combination of start station and end station trip:\n\n\n\n\n\n\n',df.groupby(['Start Station', 'End Station']).size().nlargest(1))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)








def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print('Total Trip Duration:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean Trip Duration:', df['Trip Duration'].mean())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)








def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()    
    user_types = df['User Type'].value_counts().to_string()
    print(user_type,'\n\n\n\n\n\n')
    print("for user types:")
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:    
        gender = df['Gender'].value_counts()
        print(gender,'\n\n\n\n\n')
    else : 
        print('none','\n\n\n\n\n')





    # TO DO: Display earliest, most recent, and most common year of birth


    if 'Birth Year' in df.columns:
        print('Earliest year of Birth:', df['Birth Year'].min())
        print('Most Recent year of Birth:', df['Birth Year'].max())
        print('Most Common year of Birth:', df['Birth Year'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    try:
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print("\nFor the selected filter, the oldest person to ride one "
              "bike was born in: " + earliest_birth_year)
        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print("For the selected filter, the youngest person to ride one "
              "bike was born in: " + most_recent_birth_year)
        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print("For the selected filter, the most common birth year amongst "
              "riders is: " + most_common_birth_year)
    except:
        print("We're sorry! There is no data of birth year for {}."
              .format(city.title()))

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        enter = ['Y','N']
        user_input = input('Would you like to see more data? (Enter:Yes/No).\n')
        
        while user_input.lower() not in enter:
            user_input = input('Please Enter Yes or No:\n')
            user_input = user_input.lower()
        n = 0        
        while True :
            if user_input.lower() == 'yes':
        
                print(df.iloc[n : n + 5])
                n += 5
                user_input = input('\n Would you like to see more data? (Y/N).\n')
                while user_input.lower() not in enter:
                    user_input = input('Please Enter Yes or No:\n')
                    user_input = user_input.lower()
            else:
                break           

        restart = input('\nWould you like to restart?(Y/N).\n')
        while restart.lower() not in enter:
            restart = input('Please Enter Yes or No:\n')
            restart = restart.lower()
        if restart.lower() != 'yes':
            print('BYE!')
            break


if __name__ == "__main__":
	main()