default:
    @just --list --unsorted

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
