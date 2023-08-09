import os, sys

class CustomException(Exception):
    def __init__(self, error_message:Exception,error_details: sys):
        self.error_message = CustomException.get_detailed_error_message(error_message = error_message,error_details = error_details)

    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_details: sys) ->str:
        _, _, exce_tb = error_details.exc_info()

        exception_block_line_number = exce_tb.tb_frame.f_lineno
        try_block_line_number = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename

        error_message = f'''
        Error occured in execution of :
        [{file_name}] at
        try block line number : [{try_block_line_number}]
        and exception block line number : [{exception_block_line_number}]
        error message : [{error_message}]
        '''

        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repo_(self):
        return CustomException.__name__.str()


#a ,b ,c = 1,2,3
# if i want to access c then we can write _,_,c
# exce_tb means exception try block and exc_info() means execute information
# tb_frame.f_lineno  means we are executing try block frame by frame line by line
# tb_lineno means run try blocks line by line and in between which line has error will be stored in log directory.
# f_code.co_filename means folder by folder and file by file
# Run try and except block by going line by line and folder by folder  in src.
'''
try:
    1
    2
    3
except exception as e:
    raise CustomException(e, sys)
'''
