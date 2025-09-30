# Function to generate pip install command
def generate_pip_command(package):
    # Your code here...
    return f"pip install {package}"


# Given a package name, run the above function
package_name = input()
print(generate_pip_command(package_name))
