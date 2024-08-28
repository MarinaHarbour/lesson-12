calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    string_1 = str(string)
    parameter = (len(string_1), string_1.upper(), string_1.lower())
    count_calls()
    return parameter


def is_contains(string, list_to_search):
    string_2 = str(string).lower()
    list_1 = list(list_to_search)
    count_calls()
    for i in range(len(list_1)):
        if str(list_to_search[i]).lower() == string_2:
            result = True
            break
        else:
            result = False
    return result


print(string_info('Hello'))
print(string_info('Orange'))
print(is_contains('Hello', ['ello', 'Heolol', 'hElLo']))
print(is_contains('Orange', ['Orgean', 'egnarO']))
print(calls)
