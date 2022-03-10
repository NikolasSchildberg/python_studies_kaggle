def is_truthy(to_be_eval='no_value_given'):
    """Returns truth value of given input (tested by an if statement)

    Parameter: to_be_eval (False is default)
    """
    if (to_be_eval == 'no_value_given'):
        return print("is_truthy: no_value_given")
    if (to_be_eval):
        return(True)
    else:
        return(False)


print("Truthy imported :)")
