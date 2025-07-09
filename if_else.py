

is_male = True

is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male not tall")


if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("you are male and not tall")
elif not(is_male) and is_tall:
    print("you are not a male and you are tall")
else:
    print("You are not a male and not tall")