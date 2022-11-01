class CS88Error(Exception):
    pass

def divides(x, y):
    assert y != 0, "Dont divide by 0!"
    return x % y == 0

def divides24(x):
    return safely_divedes(x, 24)

def safely_divedes(x, y):
    try:
        value = divides(x, y)
        print(f'Figured out: {value}')
        return value
    except AssertionError as err:
        print('An error occured')
        print(err)
        return False


def get_age_in_days():
    try:
        age = float(input("What is your age? "))
        assert age > 0, "Negative age, really?"
        age_in_days = age * 365 + (age // 4)
        if age_in_days < (365 * 10):
            raise CS88Error('You seem young!')
        print(f"your age in days: {age_in_days}")
    except AssertionError:
        print("Need an age > 0")
    except CS88Error as e:
        print('Catching CS88Error')
        raise e
    except:
        print("Need a valid age")

# get_age_in_days()
