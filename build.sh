# config
image_name=example/example-fastapi-login
image_tag="1.0.0"
full_image_name=${image_name}:${image_tag}

# build
cd "$(dirname "$0")"
DOCKER_BUILDKIT=1 docker build --no-cache --platform linux/amd64 . -t "${full_image_name}" -f Dockerfile
# DOCKER_BUILDKIT=1 docker build --platform linux/amd64 . -t "${full_image_name}" -f Dockerfile
