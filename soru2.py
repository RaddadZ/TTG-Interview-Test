# check length of array and rotate
def rotate(array, shiftby):
    if shiftby > len(array):
        raise ValueError('shiftby should not exceed array length. The value of shiftby was: {}'.format(shiftby))
    # slice before nth element and add it later
    return array[shiftby:]+array[:shiftby]

# print results
try:
    result = rotate([1,2,3,4,5,6], 8)
    print(result)
except ValueError as error:
    print(error)
