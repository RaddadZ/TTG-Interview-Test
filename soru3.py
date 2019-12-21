# importing regex lib for some controls
import re

# account number needed speical formatting, comparing and representation, 
# a class or a struct would make it readable and managable 
class AccountNumber:
    # a string in this format will be broken down to integers, to be easily compared and manipulated
    def __init__(self, accountStr = '00 00000000 0000 0000 0000 0000'):
        self.control = int(accountStr[slice(0,2)])
        self.bankCode = int(accountStr[slice(3,11)])
        self.ownerId = int(accountStr[slice(12,31)].replace(" ", ""))
        self.repetition = 1

    # less than function overridden to be able to sort in a list
    def __lt__(self, other):
        if not isinstance(other, AccountNumber):
            # no comparation against unrelated types
            return NotImplemented
        if self.control < other.control:
            return True
        elif self.control > other.control:
            return False
        elif self.bankCode < other.bankCode:
            return True
        elif self.bankCode > other.bankCode:
            return False
        elif self.ownerId < other.ownerId:
            return True
        else:
            return False
    
    # equale function overridden to be used in check for rep
    def __eq__(self, other): 
        if not isinstance(other, AccountNumber):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.control == other.control and self.bankCode == other.bankCode and self.ownerId == other.ownerId

    # to string function overridden to print the wanted format of account number
    def __str__(self):
        ownerIdStr = '{:016d}'.format(self.ownerId)
        ownerIdList = [ownerIdStr[i:i+4] for i in range(0, len(ownerIdStr), 4)]
        return '{} {} {} {}'.format('{:02d}'.format(self.control), '{:08d}'.format(self.bankCode),\
         ' '.join(ownerIdList), '{:01d}'.format(self.repetition))

# read file
f = open("input.txt", "r")

# reading number Of Tests
try:
    numberOfTests = int(f.readline())
except ValueError:
    print ("first line is not a number, check format") # handle not-an-integer case

# init results output array
results = []
# iterate over test cases
for i in range(numberOfTests):
    # reading number Of Accounts
    try:
        numberOfAccounts = int(f.readline())
    except ValueError:
        print ("second line is not a number, check format") # handle not-an-integer case
    
    # iterate over accounts in one test case
    listOfAccounts = []
    for j in range(numberOfAccounts):
        account = f.readline().rstrip('\n')
        # check format of account number input using regex
        if not re.match("^\d{2}\s\d{8}(?:\s\d{4}){4}$",account):
            raise Exception('account number do not match, check input file format.',i,j)
        
        # check if before exists in the list
        # if so, add to repeteatition, raise a flag 
        tempAcc = AccountNumber(account)
        for acc in listOfAccounts:
            if acc == tempAcc:
                acc.repetition += 1
                tempAcc = None
        # check flag
        if tempAcc:
            listOfAccounts.append(tempAcc)
    
    # sort the list using custom class comparision
    results.append(sorted(listOfAccounts))

    # check last line between test cases
    isEmptyLine = f.readline() in ['\n', '\r\n']
    if not isEmptyLine and i != numberOfTests-1:
        raise Exception('not empty line, check input file format.')

# print results
for test in results:
    for acc in test:
        print(acc)
    print()
