import time
import pandas as pd
import numpy as np
pd.set_option("display.max_columns", 200)

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter a city name: ").lower()
    while city.lower() not in CITY_DATA:
        city = input("Please re-enter the city name: ").lower()

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input("Please enter a month name or the word all if you do not want to filter: ").lower()
    while month.lower() not in months:
        month = input("Please re-enter the month name: ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input("Please enter a day of the week or the word all if you do not want to filter: ").lower()
    while day.lower() not in days:
        day = input("Please re-enter the day name: ").lower()

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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("The most popular month is: ", popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most popular day of the week is: ", popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular start hour is: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most popular start station is: ", popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most popular end station is: ", popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Station Combo'] = df['Start Station'] + df['End Station']
    popular_station_combo = df['Station Combo'].mode()[0]
    print("The most popular station combination is: ", popular_station_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_travel_time)

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("The average travel time is: ", average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    genders = df['Gender'].value_counts()
    print(genders)

    # Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    print("The earliest year of birth is: ", earliest_year)

    latest_year = df['Birth Year'].max()
    print("The most recent year of birth is: ", latest_year)

    most_common_year = df['Birth Year'].mode()[0]
    print("The most common year of birth is: ", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats_2(df):
    """Displays statistics on bikeshare users in Washington."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    answer = input('Would you like to see some raw data? (yes or no): ')
    i = 0
    if answer.lower() == 'no':
        message = "Thank you for your usage"
        return message
    else:
        while answer.lower() == 'yes':
            if i == 0:
                print(df[0 : 5])
                print('-'*40)
                i = 4
                answer = input('Would you like to see more raw data? (yes or no): ')
                continue
            else:
                print(df[(i+1) : (i+6)])
                print('-'*40)
                i += 5
                answer = input('Would you like to see more raw data? (yes or no): ')
                continue

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        
        if city.lower() == 'washington':
            user_stats_2(df)
        else:
            user_stats(df)
        
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
