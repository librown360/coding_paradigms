# implement a function to flatten and sort an array of integers 
# in ascending order adhereing to functional programming paradigm

# keep variables immutable
# write only pure functions
# functions may be higher order

num_list = [[12,35],[10,57],[15,39],[46,22]]

def flatten_sort(input):
    # first flatten the nested list of integers
    flat = [element for sublist in input for element in sublist]
    # take flattened list and return a sorted ascending one
    return sorted(flat)

print(flatten_sort(num_list))

# The funtion has two sole purposes none of which are to change the data received

# It is a pure function because there are no side effects when executing it
# none of the elements are being modified, only sorted into a single list

# This is not a higer order function because it neither takes in a function as a 
# parameter nor does it return a function

# I do not think it would have been easier to solve the problem using a different
# programming style

# I think functional programming is helpful in solving this problem because we
# know what the solution should be and functional programming focuses on the "what"
# rather than the "how" of solving a problem programmatically