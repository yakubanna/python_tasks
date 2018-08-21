
def prime_numbers_finder(N):
    prime_numbers = [2]
    for index in range(2, N):
        for step in prime_numbers:
            if(index % step == 0):
                break;
        else:
            prime_numbers.append(index)

    return prime_numbers

def prime_array_finder(N):
    prime_array = []
    prime_numbers = prime_numbers_finder(N)
    for index in prime_numbers:
        while(N % index == 0):
            prime_array.append(index)
            N/=index

    return prime_array



n = int(input(""))
prime_array = prime_array_finder(n)
if prime_array != []:
    for index in prime_array:
        print(index, end=" ")
else:
    print(n)
