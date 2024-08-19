import shutil
import os

def zip_project(project_dir, output_filename):
    # Check if the directory exists
    if not os.path.isdir(project_dir):
        raise ValueError(f"Directory {project_dir} does not exist.")
    
    # Create a zip file of the directory
    shutil.make_archive(output_filename, 'zip', project_dir)
    print(f"Project {project_dir} zipped successfully as {output_filename}.zip")

if __name__ == "__main__":
    project_dir = r"C:\Users\adyaa\Desktop\DiabetesPredictor"
    output_filename = r"C:\Users\adyaa\Desktop\diabetesPredict"
    zip_project(project_dir, output_filename)
