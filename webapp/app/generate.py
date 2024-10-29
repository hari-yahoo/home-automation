import os
import ollama

# Function to send file contents to Ollama and receive annotated comments
def generate_doxygen_comments(file_content):
    prompt = f"""
    Analyze the following C++/Java/Python code and generate appropriate comments in Doxygen format and add the same in appropriate places:
    {file_content}
    """
    response = ollama.generate(model='codellama', prompt=prompt)
    #response = ollama.completion(model="code-gen", prompt=prompt)  # Adjust the model and API details

    print(response)
    return response['response']
    
# Function to handle a single file
def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    annotated_content = generate_doxygen_comments(content)

    # Save the annotated file (can choose to overwrite or save as a new file)
    annotated_file_path = file_path.replace('.py', '_annotated.py')  # Adjust extension based on your files
    with open(annotated_file_path, 'w') as annotated_file:
        annotated_file.write(annotated_content)

# Function to walk through the directory and process each source file
def process_directory(source_directory):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith('.py'):  # Adjust for your file types (e.g., .java, .py)
                file_path = os.path.join(root, file)
                process_file(file_path)

# Run the script on your source directory
process_directory('\\Hari\\workspace\\rpa\\bot')
