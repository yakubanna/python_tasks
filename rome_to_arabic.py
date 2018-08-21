def rome_to_arabic(a):
    numbers = { "I" : 1,
             "V" : 5,
             "X" : 10,
             "L" : 50,
             "C" : 100,
             "D" : 500,
             "M" : 1000
           }
    combination = { "IV" : 4,
                    "IX" : 9,              
                    "XL" : 40,
                    "XC" : 90,
                    "CD" : 400,
                    "CM" : 900
                }
    prev = str(a)[0]
    number = int(numbers[str(a)[0]])
    for index in a[1:]:
        if numbers[prev] < numbers[index]:
            number -= numbers[prev]
            number += combination[prev+index]
        else:
            number += numbers[index]
        prev = index
            
            
    return number
a = input("")

print(rome_to_arabic(a))
