from seed import res
from IPython.display import display
from functions import (
    string_list_to_filtered_date_list,
    find_logins_start_end_length,
    tabulate_login_data,
)

def main():
    
    # Filter input data, comvert strings into datetime object, and remove time component
    date_list = string_list_to_filtered_date_list(res)

    # Sort date list, organize into start and end dates, and calculate consecutive logins for each entry
    start_date, end_date, length_no = find_logins_start_end_length(date_list)

    # Form a table from the three lists (start date, end date, length)
    login_table = tabulate_login_data(start_date, end_date, length_no)

    # Display table
    display(login_table)

if __name__ == "__main__":
    main()