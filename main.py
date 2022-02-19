def BinToHex(number=1000):
    #словарь для перевода
    bin_alphabet = {
        '0000': '0', '000': '0', '00': '0', '0': '0',
        '0001': '1', '001': '1', '01': '1', '1': '1',
        '0010': '2', '010': '2', '10': '2',
        '0011': '3', '011': '3', '11': '3',
        '0100': '4', '100': '4',
        '0101': '5', '101': '5',
        '0110': '6', '110': '6',
        '0111': '7', '111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'A',
        '1011': 'B',
        '1100': 'C',
        '1101': 'D',
        '1110': 'E',
        '1111': 'F'
    }
    number = str(number)
    if len(number) <= 4:
        #заменяем число с помощью словаря
        result = bin_alphabet[number]
    elif len(number) > 4:
        result = ''
        while number.isdigit():
            #заменяем число с помощью словаря и прибавляем к результату
            result = bin_alphabet[number[-4:]] + result
            #убираем использованные значения
            number = number[:-4]
    return result

def BinToOctal(number=100):
    #словарь для перевода
    bin_alphabet = {
        '000': '0', '00': '0', '0': '0',
        '001': '1', '01': '1', '1': '1',
        '010': '2', '10': '2',
        '011': '3', '11': '3',
        '100': '4',
        '101': '5',
        '110': '6',
        '111': '7',
    }
    number = str(number)
    if len(number) <= 3:
        #заменяем число с помощью словаря
        result = bin_alphabet[number]
    elif len(number) > 3:
        result = ''
        while number.isdigit():
            #заменяем число с помощью словаря и прибавляем к результату
            result = bin_alphabet[number[-3:]] + result
            #убираем использованные значения
            number = number[:-3]
    return result

def OctalToBin(number='45'):
    #словарь для перевода
    alphabet = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111'
    }
    result = ''
    while number.isdigit():
        #заменяем число с помощью словаря и конкатинируем к результату
        result = result + alphabet[number[0:1]]
        #убираем использованные значения
        number = number[1:]
    return result    

def HexToBin(number='45'):
    #словарь для перевода
    alphabet = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    result = ''
    while number.isalnum():
        #заменяем число с помощью словаря и конкатинируем к результату
        result = result + alphabet[number[0:1]]
        #убираем использованные значения
        number = number[1:]
    return result    

def FromDecimal(number=1,base=2):
    result = ''
    if base == 16:
        alphabet = {
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

        while number > 0:
            #для шестнадцатеричной СЧ используем словарь
            result = alphabet[str(number % base)] + result
            number //= base
        return result
    else:
        #цикл, поступового ділення числа на 2 и запис частки в зміну result
        while number > 0:
            result = str(number % base) + result
            number //= base
        return result

def ToDecimal(number='101',base=2):
    if base == 16:
        hex_alphabet = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15
        }
        result = 0
        len_number = len(number)-1
        while number.isalnum():
            #формула для перевода в десятиричную СЧ (для шестнадцатеричной СЧ используем словарь)
            result = hex_alphabet[number[0:1]] * pow(base,len_number) + result
            len_number -=1
            number = number[1:]
        return result    
    else:
        result = 0
        len_number = len(number)-1
        while number.isdigit():
            #формула для перевода в десятиричную СЧ
            result = int(number[0:1]) * pow(base,len_number) + result
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

    #допустимые СЧ
    system_alphabet = ['2', '8', '10', '16']

    print('Number system you can choose: \n 2 - Binary \n 8 - Octal \n 10 - Deciminal \n 16 - Hexadecimal')

    base = input("Enter the number system to convert: ")
    #проверка на соответсвие в списке допустимых значений
    while base not in system_alphabet:
        print('Write a correct system!')
        base = input("Enter the number system to convert: ")
    base = int(base)

    main_base = input("Enter the main number system: ")
    #проверка на соответсвие в списке допустимых значений
    while main_base not in system_alphabet:
        print('Write a correct system!')
        main_base = input("Enter the main number system:: ")
    main_base = int(main_base)

    #проверка на корректность бинарной СЧ
    if main_base == 2:
        correct = 0
        number = '111'
        while correct != len(number):
            number = input("Enter a number: ")
            correct = 0
            #проходимся по символам, и проверяем на соответсвие цифрам 0 и 1
            for symbol in number:
                if symbol == '0' or symbol == '1' or symbol == ',' or symbol == '.':
                    correct +=1
            if correct != len(number):
                print("Enter a correct number in binary system!")
        if str(number).find('.') != -1:
            number = float(number)
        elif str(number).find(',') != -1:
            number = float(number.replace(',', '.'))
    #проверка на корректность шестнадцатеричной СЧ            
    elif main_base == 16 and (base == 10 or base == 2 or base == 8):
        number = '111'
        correct = 0
        while correct != len(number):
            number = input("Enter a number: ")
            correct = 0
            #масив допустимых букв 
            alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
            #проходимся по символам, и проверяем ялвяються они цифрами или допустимыми буквами
            for symbol in number:
                if symbol in alphabet or iscorrect_number(symbol):
                    correct +=1
            if correct != len(number):
                print("Enter a correct number!")
        if str(number).find('.') != -1:
            number = number
        elif str(number).find(',') != -1:
            number = number.replace(',', '.')        
    #проверка на корректность восьмеричной СЧ              
    elif main_base == 8 and (base == 2 or base == 16 or base == 10):
        number = '111'
        correct = 0
        while correct != len(number):
            number = input("Enter a number: ")
            correct = 0
            alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '.', ',']
            #проходимся по символам, и проверяем диапазон значений от 0 до 7
            for symbol in number:
                if symbol in alphabet:
                    correct +=1
            if correct != len(number):
                print("Enter a correct number!")
        if str(number).find('.') != -1:
            number = float(number)
        elif str(number).find(',') != -1:
            number = float(number.replace(',', '.'))
    else:
        number = input("Enter a number: ")
        #проверка, является ли введённое значение числом
        while not iscorrect_number(number):
            print('Write a correct and positive number!')
            number = input("Enter a number: ")
        #если числое дробное, то переводит его в тип float, и при надобности заменяет запятую на точку    
        if str(number).find('.') != -1:
            number = float(number)
        elif str(number).find(',') != -1:
            number = float(number.replace(',', '.'))
        else:             
            number = int(number)

    #выбор кол-во знаков в дробной части
    if str(number).find('.') != -1 and base != 16:
        round_frac = input('Enter what number to round up to: ') 
        while not round_frac.isdigit():
            print('Enter a correct number!')
            round_frac = input('Enter what number to round up to: ') 
        round_frac = int(round_frac)           

    #вызов функций конвертации, если число целое
    if str(number).find('.') == -1:
        if main_base == 10:
            print('Your number:', FromDecimal(number,base))
        elif main_base == 2 and base == 16:
            print('Your number in hex:', BinToHex(number))
        elif main_base == 2 and base == 8:
            print('Your number in octal:', BinToOctal(number))
        elif base == 10:
            print('Your number in decimal:', ToDecimal(number,main_base))
        elif main_base == 8 and base == 2:
            print('Your number in binary:', OctalToBin(number))        
        elif main_base == 16 and base == 2:
            print('Your number in binary:', HexToBin(number))
        elif main_base == 16 and base == 8:
            print('Your number in octal:', BinToOctal(HexToBin(number)))
        elif main_base == 8 and base == 16:
            print('Your number in hex:', BinToHex(OctalToBin(number)))

    #вызов функций конвертации, если число дробное
    if str(number).find('.') != -1:
        if main_base == 10:
            #*FromDecimal
            number_int = int(fraction_split(number,method='int'))
            number_frac = int(fraction_split(number,method='frac'))
            result = FromDecimal(number = number_int, base = base) + '.' + FromDecimal(number = number_frac, base = base)
            if base != 16:
                print('Your number:', round(float(result), round_frac))
            elif base == 16:
                print('Your number:', result)    
        elif main_base == 2 and base == 16:
            #*BinToHex
            number_int = int(fraction_split(number,method='int'))
            number_frac = int(fraction_split(number,method='frac'))
            result = BinToHex(number = number_int) + '.' + BinToHex(number = number_frac)
            print('Your number in hex:', result)
        elif main_base == 2 and base == 8:
            #*BinToOctal
            number_int = int(fraction_split(number,method='int'))
            number_frac = int(fraction_split(number,method='frac'))
            result = BinToOctal(number = number_int) + '.' + BinToOctal(number = number_frac)
            print('Your number in octal:', round(float(result), round_frac))
        elif base == 10:
            #*ToDecimal
            number_int = fraction_split(number,method='int')
            number_frac = fraction_split(number,method='frac')
            result = str(ToDecimal(number = number_int)) + '.' + str(ToDecimal(number = number_frac))
            print('Your number in decimal:', round(float(result), round_frac))
        elif main_base == 8 and base == 2:
            #*OctalToBin
            number_int = fraction_split(number,method='int')
            number_frac = fraction_split(number,method='frac')
            result = OctalToBin(number = number_int) + '.' + OctalToBin(number = number_frac)
            print('Your number in binary:', round(float(result), round_frac))        
        elif main_base == 16 and base == 2:
            #*HexToBin
            number_int = fraction_split(number,method='int')
            number_frac = fraction_split(number,method='frac')
            result = HexToBin(number = number_int) + '.' + HexToBin(number = number_frac)
            print('Your number in binary:', round(float(result), round_frac))
        elif main_base == 16 and base == 8:
            #*HexToOctal
            number_int = fraction_split(number,method='int')
            number_frac = fraction_split(number,method='frac')
            result = BinToOctal(HexToBin(number = number_int)) + '.' + BinToOctal(HexToBin(number = number_frac))
            print('Your number in octal:', round(float(result), round_frac))
        elif main_base == 8 and base == 16:
            #*OctalToHex
            number_int = fraction_split(number,method='int')
            number_frac = fraction_split(number,method='frac')
            result = BinToHex(OctalToBin(number = number_int)) + '.' + BinToHex(OctalToBin(number = number_frac))
            print('Your number in hex:', result)      

if __name__ == "__main__":
    main()