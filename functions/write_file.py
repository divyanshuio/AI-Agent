import os

def write_file(working_directory, file_path, content):
    try:
        if(working_directory and file_path):
            working_directory = os.path.abspath(working_directory)
            full_file_path = os.path.join(working_directory, file_path)
    
        if(not full_file_path.startswith(working_directory)):
            return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
        
        
        else:
            if(not os.path.exists(full_file_path)):
                os.makedirs(os.path.dirname(full_file_path), exist_ok=True)

            with open(full_file_path, "w") as f:
                f.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"