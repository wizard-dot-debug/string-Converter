   # snake_cased_char_list = []
    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #         converted_character = '_' + char.lower()
    #         snake_cased_char_list.append(converted_character)
    #     else:
    #         snake_cased_char_list.append(char)
    # snake_cased_string = ''.join(snake_cased_char_list)
    # clean_snake_cased_string = snake_cased_string.strip('_')

    # return clean_snake_cased_string
    

# def snake_convert_string(pascal_or_camel_cased_string):


# def snake_case_converter(a):
#    snake_converted_string = ['_' + i.lower() if i.isupper() else i for i in a]
#    return ''.join(snake_converted_string).strip('_')

# def print_snake_string():
#    b = 'welcome to string coverter.\n'
#    print(b.title())
#    a = 'Give your string to convert:\n '
#    pascal_or_camel_cased_string = input(a.title())
#    print()
#    print(f'Your Converted String Is:\n\n {snake_case_converter(pascal_or_camel_cased_string)}\n\nThank You For Using The Program.')

# print_snake_string()
   
   


def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')
 
def main():
    print(convert_to_snake_case('iLoVEALPha'))
    
main()