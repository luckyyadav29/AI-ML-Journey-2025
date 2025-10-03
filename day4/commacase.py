def comma_code(items):
    if not items:   # handle empty list
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]


# Test cases
spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))       # apples, bananas, tofu, and cats

print(comma_code(['apples'])) # apples
print(comma_code([]))         # '' (empty string)
