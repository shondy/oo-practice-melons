############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name 
        self.pairings = []

    def __repr__(self):
        return f"{self.code}, {self.name}"

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""


    all_melon_types = []

    muskmelon = MelonType("musk", "1998", "green", True, True, "Muskmelon")
    muskmelon.pairings = ["mint"]
    casaba = MelonType("cas", "2003", "orange", True, False, "Casaba")
    casaba.pairings = ["strawberries", "mint"]
    crenshaw = MelonType("cren", "1996", "green", False, False, "Crenshaw")
    crenshaw.pairings = ["prosciutto"]
    yellow_watermelon = MelonType("yw", "2013", "yellow", False, True, "Yellow Watermelon")
    yellow_watermelon.pairings = ["ice cream"]

    all_melon_types.extend([muskmelon, casaba, crenshaw, yellow_watermelon])
    # print(all_melon_types)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
        print(f"{melon_type.name} pairs with")
        for pairing in melon_type.pairings:
            print(f"- {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_dict = {}

    for melon_type in melon_types:
        key = melon_type.code
        value = melon_type
        # print(key, value)
        melon_type_dict[key] = value
        
    return melon_type_dict


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field_harvest, harvester_name):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_harvest = field_harvest
        self.harvester_name = harvester_name
    
    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field_harvest != 3:
            return True
        return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_types = make_melon_types()

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_objects = []
    
    melon_1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
       
    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")


    return [melon_1, melon_2]

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            sell_status = "CAN BE SOLD"
        else: 
            sell_status = "NOT SELLABLE"

        print(f"Harvested by {melon.harvester_name} from Field {melon.field_harvest} ({sell_status})")


# make_melon_types()
# print_pairing_info(make_melon_types())
# print(make_melon_type_lookup(make_melon_types()))
get_sellability_report(make_melons(make_melon_types()))
