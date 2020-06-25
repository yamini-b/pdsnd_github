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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("which city would you like to filter by ? \n").lower()
        if city not in ('new york city','chicago','washington'):
            print("Please choose a valid input\n")
            continue
        else:
            break



    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("which month would you like to filter by  ?\n").title()
        if month not in ('January','February','March','April','May','June','All','all'):
            print("Please choose a valid input\n")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("which day would you like to filter by(Please select All in case you dont want to use a filter) ?\n")
        if day not in ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All','all'):
            print("Please choose a valid input\n")
            continue
        else:
            break

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])#converting start to datetime
    df['month']=df['Start Time'].dt.month#extract month from start time
    df['day_of_week']=df['Start Time'].dt.weekday_name#extract day of week from start time

    if month != 'All':
        months=['January','February','March','April','May','June']
        month=months.index(month)+1
        df=df[df['month']==month]
    if day.lower() !='all':
        df=df[df['day_of_week']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print('Most Common month:',popular_month)

    # TO DO: display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print('Most Common day:',popular_day)

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour#extracting hour
    popular_hour=df['hour'].mode()[0]#popular hour calc
    print('Most Common month:',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_st=df['Start Station'].value_counts().idxmax()#xommon str of station name
    print('Most Common start station:',popular_start_st)

    # TO DO: display most commonly used end station
    popular_end_st=df['End Station'].value_counts().idxmax()#xommon str of station name
    print('Most Common start station:',popular_end_st)

    # TO DO: display most frequent combination of start station and end station trip
    df['popular_combo']=df['Start Station'].str.cat(df['End Station'],sep=' to ')#common str of station name
    popular_combination=df['popular_combo'].mode()[0]#popular station calc
    print('Most Common station combination :',popular_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time_travel=sum(df['Trip Duration'])
    print('Total travel time :',total_time_travel/86400," days")

    # TO DO: display mean travel time
    Mean_time_travel=df['Trip Duration'].mean()
    print('Mean travel time :',Mean_time_travel/60," minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('User Type:', user_types)

    # TO DO: Display counts of gender
    try:
        Gender_types=df['Gender'].value_counts()
        print('Gender Type:', Gender_types)
    except:
        print("gender data not available for this location\n")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_Year=df['Birth Year'].min()
        print("Earliest year :",Earliest_Year)
    except:
        print("Data not available")

    try:
        Most_Recent_Year=df['Birth Year'].max()
        print("Most Recent year :",Most_Recent_Year)
    except:
        print("Data not available")

    try:
        Common_Year=df['Birth Year'].value_counts().idxmax()
        print("Most Common year :",Common_Year)
    except:
        print("Data not available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
   raw=input("do you want to see raw data ? \n").lower()
   if raw not in ('yes','no'):
        raw_data(df)
        return

   else:
            while raw=='yes':
                for i in range(5):
                    print(df.iloc[i])#to extract the first 5 rows
                    raw=input("more raw input? \n").lower()
                    if raw=='yes':
                        continue
                    else:
                        print("Thanks!")#change 1 for the refactoring project
                        break
   return


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
