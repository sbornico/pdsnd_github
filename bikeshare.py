import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    #declare/define filter values as lists and filter variables
    city = ''
    date_filter = ''
    month = 'all'
    day = 'all'
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). 
    counter = 0
    while city not in CITY_LIST: 
        if counter == 0:
            city = str(input('Would you like to see data for {}?'.format(CITY_LIST))).strip('\'\". ').title()
        else:
            city = str(input('Oh, there was a typo. Please repeat your choice: {}!'.format(CITY_LIST))).strip('\'\". ').title()
        counter +=1
        
    # get user input for date filter. 
    counter = 0
    while date_filter not in DATE_FILTER_LIST: 
        if counter == 0:
            date_filter = str(input('Would you like to filter the data by {}'.format(DATE_FILTER_LIST))).strip('\'\". ').lower()
        else:
            date_filter = str(input('Oh, there was a typo. Please repeat your choice: {}!'.format(DATE_FILTER_LIST))).strip('\'\". ').lower()
        counter +=1 

    if date_filter in ['month','both']:
        # get user input for month (january, february, ... , june)
        counter = 0
        while month not in MONTH_LIST: 
            if counter == 0:
                month = str(input('which month {}?'.format(MONTH_LIST))).strip('\'\". ').title()
            else:
                month = str(input('Oh, there was a typo. Please repeat your choice: {}!'.format(MONTH_LIST))).strip('\'\". ').title()
            counter +=1
    
    if date_filter in ['day','both']:
        # get user input for day (monday, tuesday, ..., friday)
        counter = 0
        while day not in DAY_LIST: 
            if counter == 0:
                day = str(input('Which day {}?'.format(DAY_LIST))).strip('\'\". ').title()
            else:
                day = str(input('Oh, there was a typo. Please repeat your choice: {}!'.format(DAY_LIST))).strip('\'\". ').title()
            counter +=1

    print('-'*40)
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
    # load csv file of city filter
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH_LIST.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # print filter values
    print('The date filters were set as follows: month = \'{}\' and day = \'{}\'.'.format(month, day))
    
    # display the most common month
    popular_month = df['month'].mode()[0]
    popular_month_count = df[df['month'] == popular_month]['month'].count()
    print('- The most common month is \'{}\' with a count of {}.'.format(MONTH_LIST[popular_month-1], popular_month_count))

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    popular_day_count = df[df['day_of_week'] == popular_day]['day_of_week'].count()
    print('- The most common day is \'{}\' with a count of {}.'.format(popular_day, popular_day_count))

    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    popular_hour_count = df[df['hour'] == int(popular_hour)]['hour'].count()
    print('- The most common start hour is \'{}\' with a count of {}.'.format(popular_hour, popular_hour_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
