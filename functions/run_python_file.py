import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        if(working_directory and file_path):
            working_directory = os.path.abspath(working_directory)
            full_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
        if(not full_file_path.startswith(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif(not os.path.isfile(full_file_path)):
            return f'Error: File "{file_path}" not found.'
        elif(file_path[-3:] != ".py"):
            return f'Error: "{file_path}" is not a Python file.'

        else:
            result = subprocess.run(["python3",full_file_path], capture_output=True, timeout=30)
            stdout = result.stdout.strip()
            stderr = result.stderr.strip()
            if(not stdout and not stderr):
                return "No output produced."
            output_string = f"STDOUT: {stdout}\nSTDERR: {stderr}"
            if result.returncode != 0:
                output_string += f"\nProcess exited with code {result.returncode}"
            return output_string
        
    except Exception as e:
        return f"Error: executing Python file: {e}"