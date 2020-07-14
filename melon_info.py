"""Print out all the melons in our inventory."""


from melons import melons #This call imports the dictionary in melons.py


def print_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon_name, melon_attributes in melons.items():

        print("")
        print(f'{melon_name.upper()}') #Prints melon name

        for melon_attribute, melon_value in melon_attributes.items():

            print(f'{melon_attribute}: {melon_value}') #Prints melon attributes


print_melons(melons) #Call the function