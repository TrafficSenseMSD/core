"""
Custom exception classes to provide more useful output when Excel parsing fails. 

"""

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

class ParsedConfigNotImplementedError(TSCoreError):
    """

    Parameters
    ----------
    message: explanation of the error

    """

    def __init__(self, message):
        self.message = message
