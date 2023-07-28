from datetime import datetime
import pandas as pd


def string_list_to_filtered_date_list(input_data):
    # Validation check for input
    if isinstance(input_data, list):
        # If input is a list, convert into pandas dataframe
        df = pd.DataFrame({input_data[0]: input_data})
    else:
        raise ValueError("Input data must be a list of datetime strings.")

    # Convert to datetime type and turn invalid elements to NaT
    df[df.columns[0]] = pd.to_datetime(df[df.columns[0]], errors='coerce')

    # Convert datetime to date / remove time from datetime
    df[df.columns[0]] = df[df.columns[0]].dt.date

    # Remove invalid elements
    df = df.dropna()

    # Return a list of datetime objects
    return df[df.columns[0]].tolist()


def find_logins_start_end_length(date_list):
    # Sort dates from list by ascending order
    date_list.sort(reverse=False)

    # Initialize lists and vars
    start_date = []
    end_date = []
    length_no = []
    consecutive_count = 1

    start_date.append(date_list[0]) # append first start date into list

    for i in range(len(date_list)): # for each entry in date list...

        #...check if index has reached last element in list
        if (i == len(date_list)-1): 
            end_date.append(date_list[i])
            length_no.append(consecutive_count)
            continue

        #...check if next date is a consecutive one
        elif date_list[i+1].toordinal() - date_list[i].toordinal() == 1:
            consecutive_count +=1
        
        #...check if next date is a duplicate one (multiple logins per day)
        elif date_list[i+1].toordinal() - date_list[i].toordinal() == 0:
            continue

        #...check if next date is a non-consecutive one
        else:
            end_date.append(date_list[i])
            length_no.append(consecutive_count)

            consecutive_count = 1   # reset length counter
            start_date.append(date_list[i+1]) # next date is a start date

    # Return three lists of start dates, end dates, and length number 
    return start_date, end_date, length_no

    

def tabulate_login_data(start_date_list, end_date_list, length_no_list):
    # Combine dates into table
    df = pd.DataFrame({'START': start_date_list, 'END': end_date_list, 'LENGTH': length_no_list})
    df = df.sort_values(by=['LENGTH'], ascending=False) # sort table by descending length
    
    # Reset the index column
    df = df.reset_index(drop=True)

    return df
