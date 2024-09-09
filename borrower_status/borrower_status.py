""""
Description: An enum is containing valid Borrower Statuses.
Author: Enzo kneipp
Date: sep/08
"""
from enum import Enum

class BorrowerStatus(Enum):
    """
    This represents what the possible statuses could be for library users>
    """
    ACTIVE = 0
    INACTIVE = 1
    DELINQUENT = 2
 
