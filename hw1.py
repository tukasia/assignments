from typing import List

import pandas as pd

CONFIRMED_CASES_URL = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data" \
                      f"/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv "

"""
When downloading data it's better to do it in a global scope instead of a function.
This speeds up the tests significantly
"""
confirmed_cases = pd.read_csv(CONFIRMED_CASES_URL, error_bad_lines=False)


def poland_cases_by_date(day: int, month: int, year: int = 2020) -> int:
    """
    Returns confirmed infection cases for country 'Poland' given a date.

    Ex.
    >>> poland_cases_by_date(7, 3, 2020)
    5
    >>> poland_cases_by_date(11, 3)
    31

    :param year: 4 digit integer representation of the year to get the cases for, defaults to 2020
    :param day: Day of month to get the cases for as an integer indexed from 1
    :param month: Month to get the cases for as an integer indexed from 1
    :return: Number of cases on a given date as an integer
    """

    # Your code goes here (remove pass)
    d=datetime.date(year, month, day)
    data=strftime('%m/%d/%y').lstrip("0").replace(" 0"," ")
    inpoland= confirmed_cases.loc[confirmed_cases["Country/Region"]=="Poland"]
    result = inpoland[data].values[0]
    return result 


def top5_countries_by_date(day: int, month: int, year: int = 2020) -> List[str]:
    """
    Returns the top 5 infected countries given a date (confirmed cases).

    Ex.
    >>> top5_countries_by_date(27, 2, 2020)
    ['China', 'Korea, South', 'Cruise Ship', 'Italy', 'Iran']
    >>> top5_countries_by_date(12, 3)
    ['China', 'Italy', 'Iran', 'Korea, South', 'France']

    :param day: 4 digit integer representation of the year to get the countries for, defaults to 2020
    :param month: Day of month to get the countries for as an integer indexed from 1
    :param year: Month to get the countries for as an integer indexed from 1
    :return: A list of strings with the names of the coutires
    """

    # Your code goes here (remove pass)
    d=datetime.date(year, month, day)
    d1=d.strftime('%m/%d/%y').lstrip("0").replace(" 0"," ")replace(" /0","/")
    countries confirmed_cases[[confirmed_cases["Country/Region",d1].groupby(["Country/Region"]).sum().sort_values(by+d1, ascending=False, head(5)
    return list (countries index)


# Function name is wrong, read the pydoc
def no_new_cases_count(day: int, month: int, year: int = 2020) -> int:
    """
    Returns the number of countries/regions where the infection count in a given day
    was NOT the same as the previous day.

    Ex.
    >>> no_new_cases_count(11, 2, 2020)
    35
    >>> no_new_cases_count(3, 3)
    57

    :param day: 4 digit integer representation of the year to get the cases for, defaults to 2020
    :param month: Day of month to get the countries for as an integer indexed from 1
    :param year: Month to get the countries for as an integer indexed from 1
    :return: Number of countries/regions where the count has not changed in a day
    """
    
    # Your code goes here (remove pass)
    d=datetime.date(year, month, day)
    d1=d.strftime('%m/%d/%y').lstrip("0").replace(" 0"," ")replace(" /0","/")
    yesterday = d - daytime.timedelta(days-1)
    yesterdaystr =  d.strftime('%m/%d/%y').lstrip("0").replace(" 0"," ")replace(" /0","/")
    return len(nonfirmed_cases.loc(confirmed_cases(d1)-confirmed_cases[yesterdaystr!=0].index)
                                                                                                                  
                                                                                                                  
