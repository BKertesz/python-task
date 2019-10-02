#Task 1
# Post Code generator: accepts 2 strings: "79-900" and "80-155" and returns a list of codes between them
def post_code_generator(start, end):
    to_int = lambda number: int(number.replace("-",""))
    return [str(x)[:2] + "-" + str(x)[2:] for x in range(to_int(start),to_int(end))]

#Task 2
# A LIST CONTAINING ELEMENTS OF 1-nTH VALUE IS GIVEN. WRITE A FUNCTION THAT WILL CHECK WHAT ITEMS ARE MISSING
def missing_element(list_to_check, end_number):
    return [x for x in range(1, end_number+1) if x not in list_to_check]

#Task 3
# YOU SHOULD GENERATE A LIST OF NUMBERS FROM 2 TO 5.5 WITH A STROKE OF 0.5, THE RESULT DATA MUST BE OF THE DECIMAL TYPE
def list_generator(start, end, step):
    new_list = []
    while (end + step != start):
        new_list.append(start + 0.0)
        start += step
    return new_list

print(post_code_generator("79-900","80-155"))
print(missing_element([2,3,7,4,9], 10))
print(list_generator(2,5.5,0.5))