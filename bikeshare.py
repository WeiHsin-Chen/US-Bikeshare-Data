#!/usr/bin/env python
# coding: utf-8

# In[178]:


import time
import pandas as pd
import numpy as np


# In[209]:


CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}


# In[219]:


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
    city = input('Would you like to see data for Chicago, New York, or Washington? ').lower()
    
    while city != 'chicago' and city != 'new york' and city != 'washington':
        print('There is no data for {}.'.format(city.title()))
        city = input('Would you like to see data for Chicago, New York, or Washington? ').lower()
    
    
    option_month_day = input('Would you like to filter the data by month, day, or not at all?').lower()
    if option_month_day == 'month':
        # get user input for month (all, january, february, ... , june)
        month = input('Which month or all - January, February, March, April, May, or June? ').lower()
        while month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month != 'june' and month != 'all':
            print('There is no data for {}.'.format(month.title()))
            month = input('Which month or all - January, February, March, April, May, or June? ').lower()
        
        
        day = input('Which weekday of this month or all? - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday').lower()
        while day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday' and day != 'all':
            print('There is no data for {}.'.format(day.title()))
            day = input('Which weekday of this month or all? - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday').lower()
            
    elif option_month_day == 'day':
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').lower()
        while day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday' and day != 'all':
            print('There is no data for {}.'.format(day.title()))
            day = input('Which weekday of this month or all? - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday').lower()
        
        print('These data would be selected with all months to explore.')
        month = 'all'
        
    else:
        print('The data would be all months and days to explore.')
        month = 'all'
        day = 'all'
    
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
    city = pd.read_csv(CITY_DATA[city], index_col=0)
    df = pd.DataFrame(city)
    
    # transfer 'Start Time' data type to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # get month and day columns
    df['month'] = df['Start Time'].dt.month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    df['day_of_week'] = df['Start Time'].dt.weekday
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        df = df[df['day_of_week'] == day]      
    
    return df

In[182]:


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
    city = pd.read_csv(CITY_DATA[city], index_col=0)
    df = pd.DataFrame(city)
    
    # transfer 'Start Time' data type to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # get month and day columns
    df['month'] = df['Start Time'].dt.month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    df['day_of_week'] = df['Start Time'].dt.weekday
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        df = df[df['day_of_week'] == day]      
    
    return df


# In[183]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[df['month'].mode()[0] - 1].title()
    print('The most common month is:', popular_month)

    # display the most common day of week
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    popular_day = days[df['day_of_week'].mode()[0]].title()
    print('The most common day of week is:', popular_day)

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['start_hour'].mode()[0]
    print('The most common start hour is:', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[184]:





# In[185]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:', popular_end_station)    

    # display most frequent combination of start station and end station trip
    df['Start and End Station'] = df['Start Station'] + ' to ' + df['End Station']
    popular_start_end_station = df['Start and End Station'].mode()[0]
    print('The most frequent combination of start station and end station trip is:\n', popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[186]:





# In[187]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time in seconds is:', total_travel_time)

    # display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean(), 2)
    print('The mean travel time in seconds is:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[188]:





# In[203]:


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('The details of user types are:\n', count_user_types)

    if city != 'washington':
    # Display counts of gender
        count_user_gender = df['Gender'].value_counts()
        print('The details of user gender are:', count_user_gender)

    # Display earliest, most recent, and most common year of birth
   
        earliset_birth_year = df['Birth Year'].min()
        print('The earliest year of birth is:', earliset_birth_year)
    
        most_recent_birth_year = df['Birth Year'].max()
        print('The most recent year of birth is:', most_recent_birth_year)
    
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('The most common year of birth is:', most_common_birth_year)
    
    else:
        print('Sorry, there is no data of Gender and Year of Birth for Washington city.')
        
    n = 5
    raw_data = input('Do you want to see 5 lines of raw data? yes or no').lower()
    while raw_data == 'yes' and n <= len(df['User Type']):
        print(df.head(n))
        raw_data = input('Do you want to see more 5 lines of raw data? yes or no').lower()
        n += 5

        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[205]:





# In[221]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()


# In[ ]:




