import os
import shutil
import ollama


def generate_doxygen_comments(file_content):
    prompt = f"""
    Analyze the following C++/Java/Python code and generate appropriate comments in Doxygen format:
    {file_content}
    """
    response = ollama.generate(model='codellama', prompt=prompt)
    #response = ollama.completion(model="code-gen", prompt=prompt)  # Adjust the model and API details

    print(response)
    return response['response']



def copy_files_to_output(base_directory, output_directory, file_extension):
    # Iterate through the base directory and all subdirectories
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            # Check if the file ends with the specified extension
            if file.endswith(file_extension):
                # Construct the full file path in the base directory
                file_path = os.path.join(root, file)
                
                # Create the corresponding path in the output directory
                relative_path = os.path.relpath(root, base_directory)  # Get the relative path
                output_path = os.path.join(output_directory, relative_path)  # Create the new path
                
                # Ensure the output directory exists
                os.makedirs(output_path, exist_ok=True)
                
                # Copy the file to the output directory, maintaining the name and structure
                output_file_path = os.path.join(output_path, file)
                
                # Write the file's contents to the new file in the output directory
                with open(file_path, 'r') as input_file:
                    file_contents = input_file.read()
                
               
                annotated_content = generate_doxygen_comments(file_contents)
                # Write the contents to the new file
                with open(output_file_path, 'w') as output_file:
                    output_file.write(annotated_content)
                
                print(f"Generated: {output_file_path}")

if __name__ == "__main__":
    # Input: Base directory, output directory, and file extension
    base_directory = input("Enter the base directory: ")
    output_directory = input("Enter the output directory: ")
    file_extension = input("Enter the file extension (e.g., .cpp, .py): ")
    
    # Copy files and maintain directory structure
    copy_files_to_output(base_directory, output_directory, file_extension)
