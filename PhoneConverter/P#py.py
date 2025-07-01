'''
Phone Number converter: eg (517) 989-1887 = 517-989-1887
'''
number = input("Enter your phone number")

def convert_number(number):
    digits_only = ''
    final_number = ''
    count = 0
    
    for ch in number:
        if ch.isdigit():
            digits_only += ch

    if len(digits_only) != 10:
        print("Please enter a valid phone number")
    else:
        for ch in digits_only:
            if count == 3 or count == 6:
                final_number += '-'
                final_number += ch
                count+=1
            else:
                final_number += ch
                count+=1
        return final_number

'''
test_numbers = [
    "(517) 944-6797",
    "517.989.1887",
    "517-989-1887",
    "(800)1234567",
    "12345678901",   # Too long
    "123456789"      # Too short
]


# Run tests
for num in test_numbers:
    result = convert_number(num)
    print(result)
'''
result = convert_number(number)
print(result)