from enum import Enum

class Report(Enum):
    """Enum to display document headers

    Arguments:
        Enum {enum} -- [Report headers]
    """
    HEADING = "Executive Report"
    OPERATIONS = "Operations Summary"
    SALES = "Sales Summary"
    MARKETING = "Marketing Summary"
    IT = "Information Technology Summary"