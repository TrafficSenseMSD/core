from ts_core.core_exceptions import *

class ParsedSchemaError(TSCoreError):
    """
    Exception raised when downstream processors of the parsed Excel config
    sheet encounter a structure error. 
    
    Parameters
    ----------
    message: explanation of the error

    """

    def __init__(self, message):
        self.message = message
