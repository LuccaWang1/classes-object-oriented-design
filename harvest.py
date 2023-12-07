############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""


    # not related to self, all shared (applies to every melon)
    # ex) type = fruit


    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        # self.pairings = [mint, strawberry, etc etc]
        # Muskmelon = MelonType() 
        self.code = code 
        self.first_harvest = first_harvest
        self.color = color 
        self.is_seedless = is_seedless 
        self.is_bestseller = is_bestseller 
        self.name = name

    def __repr__(self):
        return f"<{self.code}: {self.name}>"

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest

        self.pairings.append(pairing)

        # self.pairings = []
        # pairing = mint / strawberries & mint / ice cream / prosciutto 


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code 


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # order is: self, code, first_harvest, color, is_seedless, is_bestseller, name

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)
    
    cas = MelonType("cas", 2003, "orange", True, False, "Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)
    
    cren = MelonType("cren", 1996, "green", True, False, "Crenshaw")
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)
    
    yw = MelonType("YW", 2013, "yellow", True, True, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types

melon_types_woo = make_melon_types()
# info is then stored in variable

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    # all_melon_types = Muskmelon, Casaba, Crenshaw, Yellow Watermelon
    #self.pairings = [(appended to already)] -> yw.add_pairing("ice cream")
    #call the class with the init with the list of pairings 

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:  
            print(f"-{pairing}")
    
    # print(self.name = f"{self.name} pairs well with /n- {pairing[0]} /n- {painting[1]}")

    return None
print_pairing_info(melon_types_woo)

# melon_types_woo = make_melon_types()
# info is then stored in variable

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # Fill in the rest
    melon_type_dict = {}
    # melon_key = melon_types[0]
    
    # melon type code = melon_type_woo[1]
    # expected output YW: Yellow Watermelon
    # for loop -> for YW not in melon_type_dict 
    #for idx, will_be_key in range(len(melon_types)):
        # for melon_key not in melon_type_dict:
        #     melon_type_dict[melon_key] = []
        #     melon_type_dict[melon_key].append[]
    for melon in melon_types:
        if melon.code not in melon_type_dict:
            melon_type_dict[melon.code] = melon

    # melon_type_dict[key] = "Melon Type"
    # >>> (output) -> melon_type_dict { YW: "Yellow Watermelon"}
    # return a dictionary whose keys are reporting codes, values are melon type for that code

    return melon_type_dict

make_melon_type_lookup(melon_types_woo)


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    # Fill in the rest