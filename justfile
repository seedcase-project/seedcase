@_default:
    just --list --unsorted

# Run Python code styler.
style-python:
  # From https://black.readthedocs.io/en/stable/usage_and_configuration/black_docker_image.html
  docker run \
    --rm \
    --volume $(pwd):/py-style \
    --workdir /py-style \
    pyfound/black:latest_release \
    black .

# Generate PNG images from PlantUML files
generate-puml:
  docker run --rm -v $(pwd):/puml -w /puml ghcr.io/plantuml/plantuml:latest -tpng "**/*.puml"

# Start up the docker container (with build)
start-docker:
  docker compose -f docker-compose.yml up -d --build

# Close the docker container
stop-docker:
  docker compose -f docker-compose.yml down

# Resume running docker container (without build)
resume-docker:
  docker compose -f docker-compose.yml up -d

# Update the Django migration files
update-migrations:
  python manage.py makemigrations