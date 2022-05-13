import random

def standing():
    """returns out random standing pose name"""
    f = open('names/standing.txt')
    lines = f.readlines()

    names = []

    for line in lines:
        if line != "\n":
            names.append(line)

    random_name = random.choice(names)

    return("\n"+ random_name)

def fold():
    """returns random seated fold pose name"""
    f = open('names/folds.txt')
    lines = f.readlines()

    names = []

    for line in lines:
        if line != "\n":
            names.append(line)

    random_name = random.choice(names)

    return(random_name)

def backbend():
    """returns random backbend name"""
    f = open('names/backbends.txt')
    lines = f.readlines()

    names = []

    for line in lines:
        if line != "\n":
            names.append(line)

    random_name = random.choice(names)

    return(random_name)

def twist():
    """returns random twist name"""
    f = open('names/twists.txt')
    lines = f.readlines()

    names = []

    for line in lines:
        if line != "\n":
            names.append(line)

    random_name = random.choice(names)

    return(random_name)

def arm_balance():
    """returns out random arm balance name"""
    f = open('names/arm_balances.txt')
    lines = f.readlines()

    names = []

    for line in lines:
        if line != "\n":
            names.append(line)

    random_name = random.choice(names)

    return(random_name)

def inversion():
    """returns out random inversion name"""
    f = open('names/inversions.txt')
    lines = f.readlines()

    names = []

    for line in lines:
        if line != "\n":
            names.append(line)

    random_name = random.choice(names)

    return(random_name)

def seated():
    """returns out random seated pose name"""
    f = open('names/seated.txt')
    lines = f.readlines()

    names = []

    for line in lines:
        if line != "\n":
            names.append(line)

    random_name = random.choice(names)

    return(random_name)

def supine():
    """returns out random supine pose name"""
    f = open('names/supine.txt')
    lines = f.readlines()

    names = []

    for line in lines:
        if line != "\n":
            names.append(line)

    random_name = random.choice(names)

    return(random_name)