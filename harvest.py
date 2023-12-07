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

melon_types = make_melon_types()
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
print_pairing_info(melon_types)

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

make_melon_type_lookup(melon_types)


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape, color, harvested_from, harvested_by):
        self.melon_type = melon_type
        self.shape = shape
        self.color = color
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by
    
    def is_sellable(self):
        """Should return True or False based if it should be sold"""

        # if shape and color ratings > 5, True, and not field 3 (sellable)
        if self.shape >= 5 and self.color >= 5 and not self.harvested_from == 3:
            # sellable_melons.append(melon)
            return True 
        # otherwise, False (<5)
        else: 
            return False
        

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    # Fill in the rest
    # order: self, melon_type, shape, color, harvested_from, harvested_by
    melons_by_id = make_melon_type_lookup(melon_types)
    
    # from lab hint:
    # melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    
    melon_1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melons_by_id["yw"],3, 4, 2, "Sheila")
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    melon_9 = Melon(melons_by_id["yw"] 10, 7, 3, "Michael") 

    melons = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]
    # return a list
    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    
    for melon in melons:
        harvested_by = f"Harvested by {melon.harvested_by}"
        field = f"Field #{melon.harvested_from}"
        sellable = "CAN BE SOLD" if melon.is_sellable() else "NOT SELLABLE" 
        print(f"{harvested_by} from {field} {sellable}")

get_sellability_report(melons)