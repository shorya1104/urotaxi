import os
import platform
import subprocess

def check_docker_compose_installed():
    try:
        # Check if docker-compose is available in the system path
        result = subprocess.run(["docker-compose", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("Docker Compose is already installed.")
            return True
        else:
            print("Docker Compose is not installed.")
            return False
    except FileNotFoundError:
        print("Docker Compose is not installed.")
        return False

def install_docker_compose():
    try:
        # Define the Docker Compose version to install
        compose_version = "1.29.2"

        # Check the system architecture
        architecture = platform.architecture()[0]

        # Determine the appropriate Docker Compose binary URL based on the system architecture
        if architecture == "64bit":
            compose_url = f"https://github.com/docker/compose/releases/download/{compose_version}/docker-compose-Linux-x86_64"
        elif architecture == "32bit":
            compose_url = f"https://github.com/docker/compose/releases/download/{compose_version}/docker-compose-Linux-i386"
        else:
            print("Unsupported architecture.")
            return False

        # Download Docker Compose binary
        subprocess.run(["sudo", "curl", "-L", compose_url, "-o", "/usr/local/bin/docker-compose"], check=True)

        # Apply executable permissions
        subprocess.run(["sudo", "chmod", "+x", "/usr/local/bin/docker-compose"], check=True)

        # Verify installation
        result = subprocess.run(["docker-compose", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("Docker Compose installation successful.")
            return True
        else:
            print("Docker Compose installation failed.")
            return False
    except Exception as e:
        print(f"Error installing Docker Compose: {e}")
        return False

if __name__ == "__main__":
    if not check_docker_compose_installed():
        install_docker_compose()
