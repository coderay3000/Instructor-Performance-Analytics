import sys
import logging

def error_messsage_detail(error: Exception,error_detail:sys) -> str:
    """
    Extracts detailed error information including file name, line number, and the error message.

    :param error: The exception that occurred.
    :param error_detail: The sys module to access traceback details.
    :return: A formatted error message string.

    """
    #Extract the tracebook details (exception information)
    _,_,exc_tb = error_detail.exc_info()
    
    #Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    #create a formatted error message string with file name,line number and the error message
    line_number = exc_tb.tb_lineno
    error_message = f"Error occured in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"

    return error_message

class MyException(Exception):
    """
    Myexception class for handling errors in the application.
    
    """

    def __init__(self,error_message:str,error_detail:sys):
        """
        Initializes the MyException instance with an error message and error details.

        :param error_message: The error message to be associated with the exception.
        :param error_detail: The sys module to access traceback details.
        """
         # Call the base class constructor with the error message
        super().__init__(error_message)

        # Format the detailed error message using the error_message_detail function
        self.error_message = error_messsage_detail(error_message,error_detail)

    def __str__(self) -> str:
        """
        Returns the string representation of the error message.
        """
        return self.error_message   
    