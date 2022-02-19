def FromDecimal(number=1,base=2, main_base = 10):
    result = ''
    alphabet_base = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F'
        }    
    alphabet = {}
    i = main_base-1
    while i != -1 :
        alphabet[str(i)] = alphabet_base[str(i)]
        i -= 1

    while number > 0:
            #для шестнадцатеричной СЧ используем словарь
            result = alphabet[str(int(number) % base)] + result
            number //= base
    return result

def ToDecimal(number='101',base=2):
    alphabet_letters = {
        15: 'F',
        14: 'E',
        13: 'D',
        12: 'C',
        11: 'B',
        10: 'A',
        9: '9',
        8: '8',
        7: '7',
        6: '6',
        5: '5',
        4: '4',
        3: '3',
        2: '2',
        1: '1',
        0: '0'
        }        
    dict_base = {}
    i = base-1
    while i != -1 :
        dict_base[str(i)] = alphabet_letters[i]
        i -= 1
    alphabet=dict([val,key] for key,val in dict_base.items())    

    result = 0
    len_number = len(number)-1
    number = str(number)
    while number.isalnum():
        #формула для перевода в десятиричную СЧ (для шестнадцатеричной СЧ используем словарь)
        result = int(alphabet[number[0:1]]) * pow(base,len_number) + result
        len_number -=1
        number = number[1:]
    return result    
    
#разделяет число на дробную и целую часть
def fraction_split(number='45.13', method='int'):
    number = str(number)
    comma_id = number.find('.')
    if method == 'int':
        integral_part = number[:comma_id]
        return integral_part
    elif method == 'frac':    
        fractional_part = number[(comma_id+1):]
        return fractional_part

#проверяет дробное число на корректность    
def iscorrect_number(number):
    alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.']
    correct = 0
    number = str(number)
    for symbol in number:
        if symbol in alphabet:
            correct += 1
    if correct == len(number):
        return True
    else:
        return False            

def main():


    print('Number system you can choose: \n 2 - 16')

    base = int(input("Enter the number system to convert: "))
    #проверка на соответсвие в списке допустимых значений
    while not 2 <= base <= 16:
        print('Write a correct system!')
        base = int(input("Enter the number system to convert: "))

    main_base = int(input("Enter the main number system: "))
    #проверка на соответсвие в списке допустимых значений
    while not 2 <= main_base <= 16:
        print('Write a correct system!')
        main_base = int(input("Enter the main number system:: "))

    
    number = '111'
    correct = 0
    while correct != len(number):
        number = input("Enter a number: ")
        correct = 0
        #масив допустимых значений 
        alphabet = [',', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        #проходимся по символам, и проверяем ялвяються они допустимыми значениями
        for symbol in number:
            if symbol in alphabet[:main_base+2]:
                correct +=1
        if correct != len(number):
            print("Enter a correct number!")
    #если числое дробное, то переводит его в тип float, и при надобности заменяет запятую на точку         
    if str(number).find('.') != -1:
        number = number
    elif str(number).find(',') != -1:
        number = number.replace(',', '.')
    elif main_base <=16:
        number = number    
    else:             
        number = int(number)            

    #выбор кол-во знаков в дробной части
    if str(number).find('.') != -1 and 10 < base <= 16:
        round_frac = input('Enter what number to round up to: ') 
        while not round_frac.isdigit():
            print('Enter a correct number!')
            round_frac = input('Enter what number to round up to: ') 
        round_frac = int(round_frac)           

    #вызов функций конвертации, если число целое
    if str(number).find('.') == -1:
        print('Your number:', FromDecimal(
            number = ToDecimal(number=str(number),base=main_base),
            base = base,
            main_base= main_base
            ))
    #вызов функций конвертации, если число дробное
    elif str(number).find('.') != -1:
        number_int = fraction_split(number,method='int')
        number_frac = fraction_split(number,method='frac')
        print('Your number:', 
        FromDecimal(
            number = ToDecimal(number=number_int,base=main_base),
            base = base,
            main_base= main_base
            )
        + '.' +  
        FromDecimal(
            number = ToDecimal(number=number_frac,base=main_base),
            base = base,
            main_base= main_base
            ))

if __name__ == "__main__":
    main()