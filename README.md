# Django Project Template
This is a Django project template that can be used as a starting point for new Django projects. It comes with a set of Make commands that make it easy to build and run the project in a Docker container.

# Features
- Easy to use: Just clone the repository and start customizing.
- Docker integration: Run the project in a Docker container using the provided Dockerfile and Docker Compose configuration.
- Make commands: Use the provided Make commands to build, run, and test the project.
- Customizable: Modify the settings, templates, and static files to suit your needs.


# Installation
To use this Django project template, follow these steps:

- Clone the repository: git clone <repository-url>
- Set up a virtual environment: python3 -m venv env
- Activate the virtual environment: source env/bin/activate
- Install the required packages: pip install -r requirements.txt
- Copy the example environment variables: cp .env.example .env
- Customize the environment variables in the .env file to match your project requirements.
- To run the project using Docker, build and start the containers using the provided Make commands: make up

# Usage
To start a new Django project based on this template, follow these steps:
- Create a new directory for your project: mkdir myproject
- Copy the contents of this repository into your project directory: cp -r <path-to-repo>/* myproject/
- Customize the .env file to set your project-specific environment variables.
- Use the provided Make commands to build, run, and test your project.

# Make Commands
- up: Builds and starts the Docker containers.
- destroy: Stops and removes the Docker containers and their volumes.
- migrations: Runs Django's makemigrations command inside the Docker container.
- migrate: Runs Django's migrate command inside the Docker container.
- test: Runs all tests using pytest inside the Docker container.
- test_specific_file: Runs tests in a specific file using pytest inside the Docker container.
- isort: Runs isort inside the Docker container to sort the imports.
- flake: Runs flake8 inside the Docker container to check for PEP 8 style violations.
- black: Runs black inside the Docker container to format the code.

# Contributing
If you find a bug or have a suggestion for improving this project template, please open an issue or submit a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
