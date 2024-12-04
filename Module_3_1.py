calls = 0

def cout_calls():
    global calls
    calls += 1

def string_info(word):
    global calls
    cout_calls()
    return (len(word), word.upper(), word.lower())


def is_contains(animals):
    global calls
    cout_calls()
    list_ = ['крокодил', "макака", "слон", "жираф"]
    if animals.lower() in list_:
        return True
    else:
        return False

print(string_info("крокОдил"))
print(string_info("диноЗавр"))
print(is_contains('сЛон'))
print(is_contains("Велосипед"))
print(calls)