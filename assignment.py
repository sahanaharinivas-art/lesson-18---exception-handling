def check_age(age):
    try:
        age = int(age)
        if age< 0:
            raise ValueError("age cannot be negative.")
        if age % 2 ==0:
            print("the age {age} is even.")
        else:
            print("the age {age} is odd.")
    except ValueError as e:
        print(f"invalid age entered{e}")
    user_input = input("enter your age:")
    check_age(user_input)
    print(" your age is", even or odd)
    