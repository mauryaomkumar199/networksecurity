import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename 
    
    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
        
if __name__=='__main__':
    try:
        logger.logging.info("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
           raise NetworkSecurityException(e,sys)


# import sys
# from networksecurity.logging import logger

# class NetworkSecurityException(Exception):
#     def __init__(self, error_message, error_details: sys):
#         """
#         Custom exception class for handling errors with detailed traceback information.

#         :param error_message: The original error message.
#         :param error_details: sys module for extracting exception info.
#         """
#         super().__init__(error_message)  # Initialize the base exception class
#         _, _, exc_tb = error_details.exc_info()

#         # Extract traceback details
#         self.lineno = exc_tb.tb_lineno
#         self.file_name = exc_tb.tb_frame.f_code.co_filename
#         self.error_message = (
#             f"Error occurred in python script name [{self.file_name}] "
#             f"line number [{self.lineno}] error message [{error_message}]"
#         )

#     def __str__(self):
#         return self.error_message

# if __name__ == '__main__':
#     try:
#         logger.info("Enter the try block")
#         a = 1 / 0
#         print("This will not be printed", a)
#     except Exception as e:
#         raise NetworkSecurityException(e, sys)
