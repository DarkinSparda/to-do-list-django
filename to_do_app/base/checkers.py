

def complete_check(lst):
    for item in lst:
        if item.complete == False:
            return False
        else:
            continue
    return True

