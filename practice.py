store_results = []

def sum_number():
    a= int(input('first number: '))
    b = int(input('second number: '))
    return a + b
    
while True:
    result = sum_number()
    store_results.append(result)
    print('the sum is',result)
    print(store_results)

    continue_calculating = input('Do you want to perform another calculation (yes/no: )')
    if continue_calculating != 'yes':
        break
    


