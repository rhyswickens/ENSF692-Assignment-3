# school_data.py
# Author: Rhys Wickens
#
# A terminal-based application for computing and printing school statistics based on the given input.


# importing required packages and data
import numpy as np
from math import floor
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Combining all school enrollment arrays into a single array
arrays = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]

# reshaping each array to 20 x 3
reshaped_arrays = [array.reshape(20, 3) for array in arrays]

# Combining the reshaped array into a single NumPy three-dimensional array of shape 10 x 20 x 3
final_array = np.array(reshaped_arrays)

# Create lists ofthe school names and school codes
school_names = ["Centennial High School", "Robert Thirsk School", "Louise Dean School", "Queen Elizabeth High School", "Forest Lawn High School", 
               "Crescent Heights High School", "Western Canada High School", "Central Memorial High School", "James Fowler High School", 
               "Ernest Manning High School", "William Aberhart High School", "National Sport School", "Henry Wise Wood High School", "Bowness High School", 
               "Lord Beaverbrook High School", "Jack James High School", "Sir Winston Churchill High School", "Dr. E. P. Scarlett High School", 
               "John G Diefenbaker High School", "Lester B. Pearson High School"]
school_codes = ["1224", "1679", "9626", "9806", "9813", "9815", "9816", "9823", "9825", "9826", "9829", "9830", "9836", "9847", "9850", "9856", "9857", "9858", "9860", "9865"]

class SchoolDirectory:
    """A class to represent a School Directory where school names correspond to a school code.

    Attributes:
        school_names (List): List of strings that represent the school names
        school_codes (List): List of strings that represent the school codes that correspond to the school names
    """
    def __init__(self, school_names, school_codes):
        # I am creating dictionaries here as per the requirements in the README.
        self.name_to_code = {name: code for name, code in zip(school_names, school_codes)}
        self.code_to_name = {code: name for name, code in zip(school_names, school_codes)}
        self.school_names = school_names
        self.school_codes = school_codes
        
    def get_code_from_name(self, name):
        """ Given a school name, returns the school code or "School code not found" if the name doesn't exist.
        
        Args: 
            School name (String): String value that represents the name of the school

        Return: 
            School code or "School code not found" (String)
        """
        return self.name_to_code.get(name, "School code not found.")
    
    def get_name_from_code(self, code):
        """Given a school code, returns the school name or "School name not found" if the code doesn't exist.

        Args: 
            School code (String): String value that represents the code of the school

        Return: 
            School name or "School name not found" (String)
        """
        return self.code_to_name.get(code, "School name not found.")
    
    def get_index_from_name(self, name):
        """Given a school name, returns the index of the school in the list or -1 if the school name doesn't exist.

        Args: 
            School name (String): String value that represents the name of the school

        Return: 
            Index in school_names list or -1 (int)
        """
        if name in self.school_names:
            return self.school_names.index(name)
        return -1
    
    def get_index_from_code(self, code):
        """
        Given a school code, returns the index of the school in the list or -1 if the school code doesn't exist.

        Args: 
            School code (String): String value that represents the code of the school

        Return: 
            Index in school_codes list or -1 (int)
        """
        if code in self.school_codes:
            return self.school_codes.index(code)
        return -1

def get_user_input():
    """Asks the user to enter a school name or code in the terminal.

    Return: 
        user input (String): returns the string that the user inputted
    """
    school = input("Please enter the high school name or school code: ")
    return school

def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here

    print("\nShape of full data array: " + str(final_array.shape))
    print("Dimensions of full data array: " + str(final_array.ndim))

    # Create a SchoolDirectory object with the school names and codes
    directory = SchoolDirectory(school_names, school_codes)

    # Prompt for user input and figure out the input type. If an invalid input is entered, ask the user again until a correct input is entered.
    while True:
        try:
            input = get_user_input()
            if(directory.get_index_from_name(input) >= 0):
                input_type = "name"
                break
            elif(directory.get_index_from_code(input) >= 0):
                input_type = "code"
                break
            else:
                raise ValueError
        except ValueError:
            print("\nYou must enter a valid school name or code.\n")
    
    # Get school code from input and the index of the school
    if(input_type == "name"):
        code_input = directory.get_code_from_name(input)
    else:
        code_input = input
    school_index = directory.get_index_from_code(code_input)

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    # print the inputed school name and code
    print("School Name: " + str(directory.get_name_from_code(code_input)) + ", School Code: " + str(code_input))

    # Print the mean enrollment for grade 10, 11, and 12, as well as the highest and lowest enrollment for a single grade
    print("Mean enrollment for Grade 10: " + str(floor(np.nanmean(final_array[:, school_index, 0]))))
    print("Mean enrollemnt for Grade 11: " + str(floor(np.nanmean(final_array[:, school_index, 1]))))
    print("Mean enrollemnt for Grade 12: " + str(floor(np.nanmean(final_array[:, school_index, 2]))))
    print("Highest enrollment for a single grade: " + str(floor(np.nanmax(final_array[:, school_index, :]))))
    print("Lowest enrollment for a single grade: " + str(floor(np.nanmin(final_array[:, school_index, :]))))

    # Printing the total enrollment for each year from 2013 to 2022. Also printing the total ten year enrollment over that time.
    for i in range(10):
        print("Total enrollment for "+str(2013 + i)+": " + str(floor(np.nansum(final_array[i, school_index, :]))))
    print("Total ten year enrollment: " + str(floor(np.nansum(final_array[:, school_index, :]))))
    print("Mean total enrollment over 10 years: " + str(floor(np.nansum(final_array[:, school_index, :]) / 10)))

    # If any enrollment number is greater than 500 for the school, print the median enrollment for those values over 500.
    # Otherwise, print "No enrollments over 500."
    if(np.any(final_array[:, school_index, :] > 500)):
        sub_array = final_array[:, school_index, :]
        sub_array_over_500 = sub_array[sub_array > 500]
        print("For all enrollments over 500, the median value was: " + str(floor(np.nanmedian(sub_array_over_500))))
    else:
        print("No enrollments over 500.")

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

    # Printing general statisics: mean enrollment in 2013 and 2022, total graduating class of 2022, and the highest/lowest enrollment for a single grade
    print("Mean enrollment in 2013: " + str(floor(np.nanmean(final_array[0, :, :]))))
    print("Mean enrollment in 2022: " + str(floor(np.nanmean(final_array[9, :, :]))))
    print("Total graduating class of 2022: " + str(floor(np.nansum(final_array[9, :, 2]))))
    print("Highest enrollment for a single grade: " + str(floor(np.nanmax(final_array[:, :, :]))))
    print("Lowest enrollment for a single grade: " + str(floor(np.nanmin(final_array[:, :, :]))))


if __name__ == '__main__':
    main() 

