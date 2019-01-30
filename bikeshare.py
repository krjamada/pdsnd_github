import time
import pandas as pd
import numpy as np
import calendar as cd

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

# Getting city selection from user
    city = input('Choose a city between Chicago,New York City and Washington: ').lower()
    while city not in ['chicago','new york city','washington']:
            print('Please enter a valid city')
            city = input('Choose a city between Chicago,New York City and Washington: ').lower()

# Getting month selection from user
    month = input('Which month would you like to explore between January and June.If you want to look at all months please enter all: ').lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('Please enter a valid month')
            month = input('Please choose between January and June.If you want to look at all months please enter all: ').lower()

# Getting getting day selection from user
    day = input('Which day would you like to explore .If you want to look at all days please enter all: ').lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print('Please enter a valid day')
            day = input('Please enter a valid day.To look at all days please enter all: ').lower()


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

    # convert the Start Time and End Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # extract month,day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour

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
#Displaying statistics regarding time of bike usage
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = cd.month_name[df['month'].mode()[0]]
    print('Most common month:',most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day:',most_common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Displaying statistics regarding place of bike usage
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most common start station:',most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most common end station:',most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_trip = 'From ' + df['Start Station'] + ' to ' +df['End Station']
    print('Most common trip:',most_common_trip.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#Displaying statistics regarding duration of bike usage
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Duration'] =  df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    total_travel_time = df['Duration'].sum()
    print('Total Travel Time:',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Duration'].mean()
    print('Mean Travel Time:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Displaying statistics regarding demographics of bike usage
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Types of Users:',user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print('Gender Distribution:',genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_yob = int(df['Birth Year'].min())
        print("Earliest Birth Year: ",earliest_yob)
        latest_yob = int(df['Birth Year'].max())
        print("Most Recent Birth Year: ",latest_yob)
        common_yob = int(df['Birth Year'].mode())
        print("Most Common Birth Year: ",common_yob)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

## raw_data function is used to show raw data to the user when required
def raw_data(df):
    '''Asks user if raw data are required and displays raw data if necessary.'''
    rows = 0
    while True:
            raw_data = input("Would you like to see the five entries of the raw data:").lower()
            if (raw_data == 'yes'):
                print(df[rows: rows + 5])
                rows = rows + 5
                print('-'*80)
                continue
            elif (raw_data == 'no'):
                break
            else: print('Invalid input!')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
