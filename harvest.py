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

    musk = MelonType("musk", "Muskmelon", 1998, "green", True, True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)
    
    cas = MelonType("cas", "Casaba", 2003, "orange", True, False)
    musk.add_pairing("strawberries and mint")
    all_melon_types.append(cas)
    
    cren = MelonType("cren", "Crenshaw", 1996, "green", True, False)
    cren.add_pairing("prosciutto")
    all_melon_types(cren)
    
    yw = MelonType("YW", "Yellow Watermelon", 2013, "yellow", True, True)
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    self.name = f"{self.name} this pairs well with {pairing}"


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # Fill in the rest


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