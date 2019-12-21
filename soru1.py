# simply check if elemnt in array1 exists in array2, if not, add to reuslt array
def findMissing(array1, array2):
    result = []
    for i in array1:
        if i not in array2:
            result.append(i)
    return result

# print results
result = findMissing([4,12,9,5,6,1],[4,9,12,6])
print(result)
