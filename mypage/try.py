import os
import subprocess
import sys

# Define the virtual environment directory name
VENV_DIR = "venv"

def create_venv():
    """Creates a virtual environment and installs dependencies."""
    print("Creating virtual environment...")
    subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])

    # Activate the virtual environment and install requirements
    activate_venv()

    print("Installing dependencies from requirements.txt...")
    if os.path.exists("requirements.txt"):
        # Determine pip path based on the operating system
        pip_executable = os.path.join(VENV_DIR, "Scripts", "pip") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "pip")
        subprocess.check_call([pip_executable, "install", "-r", "requirements.txt"])
    else:
        print("requirements.txt not found!")
        sys.exit(1)

def activate_venv():
    """Activates the virtual environment."""
    print("Activating virtual environment...")
    if os.name == "nt":  # For Windows
        activate_script = os.path.join(VENV_DIR, "Scripts", "activate")
    else:  # For UNIX-based systems (Linux, macOS)
        activate_script = os.path.join(VENV_DIR, "bin", "activate")

    return activate_script

def start_django_server():
    """Starts the Django development server."""
    python_executable = os.path.join(VENV_DIR, "Scripts", "python") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")
    print("Starting Django server...")
    subprocess.check_call([python_executable, "manage.py", "runserver"])

if __name__ == "__main__":
    # Check if virtual environment directory exists
    if not os.path.exists(VENV_DIR):
        create_venv()
    else:
        activate_venv()

    # # Start the Django server
    start_django_server()
