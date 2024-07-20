# function named print_numbers to print numbers from 1 to max value
def print_numbers(max_value):
    total = 0
    for i in range(1, max_value + 1):
        print(i, end=' ')
        total = total + i
    print('\n')
    return total

#main program
print('my main program')
# calling function
result_total_10 = print_numbers(10) # print 1 to 10, total = 55
print(result_total_10)
result_total_20 = print_numbers(20) # print 1 to 20, total = 210
print(result_total_20)
result_total_100 = print_numbers(100) # print 1 to 100, total = 5050
print(result_total_100)
print('continue main program')

