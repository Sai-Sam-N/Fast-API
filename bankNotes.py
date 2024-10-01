# Uses the pickle file for classification
# Parameters required - variance, skewness, curtosis, entropy

from pydantic import BaseModel 

# A class that describes the Bank Notes Measurements - inherits BaseModel from pydantic
class BankNote(BaseModel):
    # <variable_name> : <data_type>
    variance : float
    skewness : float
    curtosis : float
    entropy : float

# This can also be done using requests rather than pydantic.
# But, pydantic is more useful since it enforces type hints at runtime, and provides user friendly errors when data is invalid.