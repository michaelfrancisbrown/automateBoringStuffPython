spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(a_list):
    count=0
    a_string=''
    while count < len(a_list)-1:
        a_string += a_list[count] + ', '
        count+=1
    return a_string + 'and ' + a_list[count] 

print(comma(spam))
