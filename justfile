# Install necessary Python packages
install-py-deps:
  python3 -m pip install -r seedcase/requirements.txt

# Start up the docker container (with build)
start-docker:
  docker compose -f docker-compose.yml up -d --build

# Close the docker container
stop-docker:
  docker compose -f docker-compose.yml down

# Resume running docker container (without build)
resume-docker:
  docker compose -f docker-compose.yml up -d

# Install any necessary packages for development
install-dev-py-deps:
  python3 -m pip install black

# Run Python code formatter
format-python:
  python3 -m black ./