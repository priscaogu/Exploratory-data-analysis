import os
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """  # load data file into a dataframe

    df = pd.read_csv(os.getcwd() + '\\Documents\\Understanding_the_data\\' + CITY_DATA.get(city))

    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        # month =  input('Enter the month'.format(months))
        month_index = months.index(month)

        # filter by month to create the new dataframe
        df = df[df.month == month_index]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[(df.day_of_week) == day.title()]

    return df


df = load_data('chicago', 'march', 'friday')

print(df)