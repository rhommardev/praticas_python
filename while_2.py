while True: # type: ignore
    age = input("enter your age: ")
    if age.isdigit():
        age_int = int(age)
        if 1 <= age_int <= 120:
            print(f"You are {age_int} years old!")
            break
        else:
            print("invalid age. please try again")