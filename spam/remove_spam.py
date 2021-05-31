menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

#using generator and loop, to remove spam from menu, printed separated by comma
for data in menu:
    removed_spam = ", ".join((item for item in data if item != "spam"))
    print(removed_spam)

#join with list, list should contain all strings
data = ["dog", "rabbit", "snake", "mouse", "cat"]
result = ", ".join(data)
print(result)