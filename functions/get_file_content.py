import os

def get_file_content(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    full_file_path = os.path.join(working_directory, file_path)
    try:
        if(not file_path.startswith(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # elif(not os.path.isdir(file_path)):
        #     return f'Error: "{file_path}" is not a file'

        elif(file_path not in os.listdir(working_directory)):
            pass
    
        
        else:
            output_string = ""

            return output_string[:-1]
    except Exception as e:
        return f"Error: {e}"