# constant
NUM_MAP = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        '20': 'twenty',
        '30': 'thirty',
        '40': 'fourty',
        '50': 'fifty',
        '60': 'sixty',
        '70': 'seventy',
        '80': 'eighty',
        '90': 'nighty'
    }


def Num_Eng(str, len):
    if len == 1:
        return NUM_MAP[str]
    elif len == 2:
        if str[0:1] == '0':
            return NUM_MAP[str[1]]
        elif str[0:1] < '2':
            return NUM_MAP[str]
        else:
            tmpStr = str[0:1] + '0'
            if (str[1] == '0'):
                return NUM_MAP[tmpStr]
            else:
                return NUM_MAP[tmpStr] + ' ' + NUM_MAP[str[1]]
    elif len == 3:
        if str[0:1] == '0':
            return Num_Eng(str[1:], 2)
        else:
            if str[1:] == "00":
                return Num_Eng(str[0:1], 1) + ' hundred'
            else:
                return Num_Eng(str[0:1], 1) + ' hundred and ' + Num_Eng(str[1:], 2)
    else:
        return '0'


def ChequeWriter(str_dollar, str_cent):
    
    # seperate dollar strings
    len_dollar = len(str_dollar)
    str_billion = 'NaN'
    str_million = 'NaN'
    str_thousand = 'NaN'
    str_single = str_dollar
    if len_dollar == 10:
        str_billion = str_dollar[0:1]
        str_million = str_dollar[1:4]
        str_thousand = str_dollar[4:7]
        str_single = str_dollar[7:]
    elif len_dollar > 6:
        count_m = len(str_dollar) - 6
        str_million = str_dollar[0:count_m]
        str_thousand = str_dollar[count_m:count_m+3]
        str_single = str_dollar[count_m+3:]
    elif len_dollar > 3:
        count_s = len(str_dollar) - 3
        str_thousand = str_dollar[0:count_s]
        str_single = str_dollar[count_s:]

    # map it to English
    dollar_Eng = ''
    if str_billion != 'NaN':
        dollar_Eng += Num_Eng(str_billion, len(str_billion)) + " billion"
    
    if str_million != 'NaN' and str_million != '000':
        if str_billion != 'NaN':
            dollar_Eng += ", "
        dollar_Eng += Num_Eng(str_million, len(str_million)) + " million"
    
    if str_thousand != 'NaN' and str_thousand != '000':
        if str_billion != 'NaN' or str_million != 'NaN':
            dollar_Eng += ", "
        dollar_Eng += Num_Eng(str_thousand, len(str_thousand)) + " thousand"
    
    if str_single == '000':
        dollar_Eng += " DOLLARS"
    else:
        if str_billion != 'NaN' or str_million != 'NaN' or str_thousand != 'NaN':
            dollar_Eng += ", "
        dollar_Eng += Num_Eng(str_single, len(str_single)) + " DOLLARS"
    
    if str_cent == '00':
        cent_Eng = ''
    else:
        cent_Eng = ' AND ' + Num_Eng(s_cent, 2) + ' CENTS'

    return dollar_Eng + cent_Eng


def my_ut():
    number_list=[]
    word_list=[]
    for (number,word) in zip(number_list,word_list):
        if word == ChequeWriter(number[:-3], number[-2:]):
            print("Pass")
        else:
            print("Fail")

if __name__ == "__main__":
    monetary_val = input("Please input a monetary value (Format - *.**): ")
    s_dollar = monetary_val[0:len(monetary_val) - 3]
    s_cent = monetary_val[len(monetary_val) - 2:]
    print(ChequeWriter(s_dollar, s_cent))
    my_ut()
