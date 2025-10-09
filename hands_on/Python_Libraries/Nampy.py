import numpy as np
from datetime import date
import math

# Example function using numpy
def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    return np.pi * np.power(radius, 2)  
print(f"Area of circle with radius 5: {calculate_circle_area(5)}")

# Example function using datetime
def days_until_new_year():
    """Calculate the number of days until New Year's Day."""
    today = date.today()
    new_year = date(today.year + 1, 1, 1)
    return (new_year - today).days          
print(f"Days until New Year: {days_until_new_year()}")
# Array manipulation with numpy
def manipulate_array(arr):
    """Perform some basic array manipulations."""
    np_arr = np.array(arr)
    return {
        'original': np_arr,
        'mean': np.mean(np_arr),
        'std_dev': np.std(np_arr),
        'squared': np.square(np_arr)
    }   
print(manipulate_array([1, 2, 3, 4, 5]))
#create a  2d array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"2D Array:\n{array_2d}")
