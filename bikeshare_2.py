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
    
    print('Hello! Let\'s explore some US bikeshare data! \n')
    
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input("Which city you want to analyze? \n").lower().strip())
        if city in CITY_DATA.keys():
            break
        else:
            print("invalid input! please type a valid name \n")
            
            
    # get user input for month (all, january, february, ... , june)
    while True:    
        month = str(input("Do you want more filters in months?? if yes, type month name from within first six months else type 'all' \n").lower().strip())
        months1 = ["january","february","march","april","may","june","all"]
        if month in months1:
            break
        else:
            print("invalid input! please type a valid name \n")
            
            
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("Do you want more filters in days?? if yes, type day name else type 'all' \n"))
        days1 = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        if day in days1:
            break
        else:
            print("invalid input! please type a valid name \n")
            
            
    print('-'*40)
    return city, month, day


print("\n")     # separator


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

    # convert "Start Time" column to datetime using to_datetime function
    df["Start Time"] = pd.to_datetime(df['Start Time'])
    
    # extract month and day from "Start Time" column and create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
    df["hour"] = df["Start Time"].dt.hour
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


print("\n")     # separator


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    pop_month = df["month"].mode()[0]
    print(f"The most common month is: {pop_month} \n")

    # display the most common day of week
    pop_day = df["day_of_week"].mode()[0]
    print(f"The most common day of week is: {pop_day} \n")

    # display the most common start hour
    pop_hour = df["hour"].mode()[0]
    print(f"The most common day of week is: {pop_hour} \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


print("\n")     # separator


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    pop_station_st = df["Start Station"].mode()[0]
    print(f"The most common start station is: {pop_station_st} \n")

    # display most commonly used end station
    pop_station_en = df["End Station"].mode()[0]
    print(f"The most common end station is: {pop_station_en} \n")

    # display most frequent combination of start station and end station trip
    df["Combination"] = df["Start Station"] + df["End Station"]
    pop_combin = df["Combination"].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


print("\n")     # separator


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df["Trip Duration"].sum()
    print(f"The total number of travels is: {total:,} \n")
    # display mean travel time
    mean = df["Trip Duration"].mean()
    print(f"The average number of travels is: {mean:.3f} \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    
    if city != "washington":
        """Displays statistics on bikeshare users."""

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        user_count = df["User Type"].value_counts()
        print(f"{user_count}\n")

        # Display counts of gender
        city != "washington"
        gen_count = df["Gender"].value_counts()
        print(f"{gen_count}\n")
        

        # Display earliest, most recent, and most common year of birth
        early = df["Birth Year"].min()
        common = df["Birth Year"].mode()[0]
        recent = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        print(f"The earliest date of birth is {early:.0f}\n")
        print(f"The most recent date of birth is {recent:.0f}\n")
        print(f"The most common date of birth is {common:.0f}\n")

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        """Displays statistics on bikeshare users."""

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        user_count = df["User Type"].value_counts()
        print(user_count)
        
        print("washington has no columns called \"Gender\" or \"Birth Year\"\n")

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
def display_data(df):
    
    print("\n Do you want to show the first 5 rows of data? \n")
    x = 0
    while True:
        check = str(input("type \"yes\" or \"no\"\n").lower().strip())
        if check == "yes":
            print(df.iloc[x:x+5],"\n")
            x += 5
            print("Do you want to continue? \n")
            continue
        elif check == "no":
            break
        else:
            print("\n invalid input! please type a valid name \n")

        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
