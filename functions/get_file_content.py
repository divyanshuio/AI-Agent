import os

def get_file_content(working_directory, file_path):
    try:
        if(working_directory and file_path):
            working_directory = os.path.abspath(working_directory)
            full_file_path = os.path.join(working_directory, file_path)
    
        if(not full_file_path.startswith(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        elif(not os.path.isfile(full_file_path)):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        else:
            with open(full_file_path, "r") as f:
                file_content_stirng = f.read(10000)
                extra = f.read(1)
            
            if(extra):
                file_content_stirng += '\n[...File "{file_path}" truncated at 10000 characters]'
            
            return file_content_stirng
    except Exception as e:
        return f"Error: {e}"
    
