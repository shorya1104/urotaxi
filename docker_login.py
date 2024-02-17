import docker

def login_to_registry(username, password, registry_url):
    # Initialize Docker client
    client = docker.from_env()

    # Login to the registry
    try:
        client.login(username=username, password=password, registry=registry_url)
        print("Login to Docker registry successful")
    except docker.errors.APIError as e:
        print(f"Failed to login to Docker registry: {e}")

if __name__ == "__main__":
    # Replace these values with your Docker registry credentials and URL
    username = "shoryasngh"
    password = "Shorya@_1104"
    registry_url = "https://hub.docker.com/"

    login_to_registry(username, password, registry_url)
