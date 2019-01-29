#lab4-3

def ReverseName(name):
    """Returns the "last_name, first_names" version
    of the name.
    """
    parts = name.split()
    return parts.pop() + ', ' + ' '.join(parts)

def main():
    NAMES = ["Jack Sparrow", "George Washington", 
             "Tiny Sparrow", "Jean Ann Kennedy"]
    def ReverseThem():
        reversed_names = []
        for name in NAMES:
            reversed_names += [ReverseName(name)]
        for name in sorted(reversed_names):
            print (name)
    ReverseThem()
main()


