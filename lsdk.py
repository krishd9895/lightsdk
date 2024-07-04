import os
import threading
import time
from lightning_sdk import Studio


def run_command_in_studio(studio, command):
    try:
        print(f"Attempting to run '{command}' within the studio...")
        result = studio.run(command)

        if isinstance(result, tuple) and len(result) == 2:
            output, exit_code = result
            print(f"Command '{command}' output:\n{output}")
            if exit_code == 0:
                print(f"Command '{command}' ran successfully.")
            else:
                print(f"Command '{command}' exited with code {exit_code}")
        else:
            print(f"Command result:\n{result}")
    except Exception as e:
        print(f"Error running command '{command}' in studio: {e}")


def main():
    print("Starting Lightning AI authentication and studio creation process...")

    # Retrieve the authentication credentials from environment variables
    user_id = os.environ["user_id"]
    api_key = os.environ["api_key"]
    username = os.environ["username"]
    studio_name = os.environ["studio_name"]

    if not user_id or not api_key or not username:
        print("Environment variables for user ID, API key, or username are not set.")
        exit(1)

    
    teamspace = "Vision-model"
    print(f"Preparing to create Studio '{studio_name}' in teamspace '{teamspace}' for user '{username}'...")

    # Initialize the Studio
    try:
        studio = Studio(name=studio_name, teamspace=teamspace, user=username, create_ok=True)
        print(f"Studio '{studio_name}' initialized successfully.")
    except Exception as e:
        print(f"Error initializing studio: {e}")
        exit(1)

    # Start the Studio
    try:
        print(f"Attempting to start Studio '{studio_name}'...")
        studio.start()
        print(f"Studio '{studio_name}' has been started successfully.")
    except Exception as e:
        print(f"Error starting studio: {e}")
        exit(1)

    # Commands to run in parallel
    commands = ["python3 wmltb.py", "python3 zmltb.py"]

    # Run commands every 6 minutes
    while True:
        # Create threads for each command
        threads = []
        for command in commands:
            thread = threading.Thread(target=run_command_in_studio, args=(studio, command))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        print("Commands executed. Sleeping for 6 minutes...")
        time.sleep(6 * 60)  # Sleep for 6 minutes


if __name__ == "__main__":
    main()
