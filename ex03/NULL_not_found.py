def NULL_not_found(object: any) -> int:
    if object is None: print("Nothing: None " + str(type(object)))
    elif isinstance(object, float) and object != object: print("Cheese: nan " + str(type(object)))
    elif object is False: print("Fake: False " + str(type(object)))
    elif object == 0: print("Zero: 0 " + str(type(object)))
    elif object == str(""): print("Empty: " + str(type(object)))
    else: print("Type not Found")
    return 1