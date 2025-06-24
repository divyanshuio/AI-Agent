import os
from functools import reduce

def get_files_info(working_directory, directory=None):
    
    working_directory = os.path.abspath(working_directory)
    directory = os.path.join(working_directory, directory)
    print(directory)
    print(working_directory)
    try:
        if(not directory.startswith(working_directory)):
            return f'Error: Cannot list "{directory}" as it is   outside the permitted working directory'
        
        elif(not os.path.isdir(directory)):
            return f'Error: "{directory}" is not a directory'
        
        else:
          
            contents_of_directory = os.listdir(directory)
            print("CONTENTS: ",contents_of_directory)
            
            output_string = ""

            for item in contents_of_directory:
                file = os.path.join(directory, item)
                output_string += f"- {item}: file_size={os.path.getsize(file)} bytes, is_dir={os.path.isdir(file)}\n"

            return output_string[:-1]
    except Exception as e:
        return f"Error: {e}"
        
