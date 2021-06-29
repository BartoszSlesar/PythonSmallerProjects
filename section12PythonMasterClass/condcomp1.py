menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
print(meals)

meals = [meal for meal in menu if "spam" not in meal]
print(meals)

x = 15
# conditional expression
expression = "Twelve" if x == 12 else "unknown"
print(expression)

# conditional expression + list comprehension
print("*" * 80)
meals = [meal if "spam" not in meal else "a meal skipped" for meal in menu]
print(meals)
print("*" * 80)
for meal in menu:
    # "contains egg" is default in expression, not use in production, only to experiment, that this is possible
    print(meal, "contains chicken" if "chicken" in meal else "contains bacon" if "backon" in meal else "contains egg")
