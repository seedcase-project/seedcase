# Setup the Seedcase Instruction

## Download and install Docker

Please download the Docker for your operating system from this link
<https://docs.docker.com/get-docker/>. There are several steps involved,
make sure to do them all for your operating system.

Your will download and install the Docker engine and Docker's user
friendly application as Docker desktop. Please follow the instruction to
download and install the application.

## Start Docker Engine

Start the Docker Engine by using the Docker Desktop application you
installed. Make sure Docker is running properly, run the command
`docker --version` in the terminal or shell. If you find the warning
message "Cannot connect to the Docker daemon" in the output, it means
that the docker engine is not started on your local, please check if the
docker desktop started properly.

## Some basic Docker command

Some of the docker commands you may use, you could try it from your
command line tool.

1.  `docker help` list all docker commands.
2.  `docker ps` list running docker containers.
3.  `docker images` list all created local docker images.
4.  `docker start` Start one or more docker containers.
5.  `docker stop` stop one or more containers.
6.  `docker compose up` Run the docker containers from the docker
    compose file.
7.  `docker compose down` Stop and remove all docker containers from the
    docker compose file.

## Setup the environment file

Create a copy of the `env_example` file, to fill in with your details,
using this Terminal command, assuming starting directory is `seedcase`:

``` bash
cp env_example .env.django
```

Open the copied `.env.django` file and fill in your details for
`DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, and
`DJANGO_SUPERUSER_PASSWORD`. For the password, make it up. Use these
details when logging in to the admin part of the web application.

## Run the docker containers

Use the command line tool to access the current folder by running to
below code. You will need to run this as "root" user (e.g. `sudo` for
Linux):

<!-- TODO: What is root for Mac or Windows? -->

``` bash
docker compose up -d --build
```

Docker will then try to download all the required packages, make an
image to the local computer, and try to run it. Once done, it should
print something like:

```
⠿ Container demo_version_containers-db-1          Started       0.3s
⠿ Container django_webapp                         Started       0.5s
```

Which indicates that Docker is ready.

## Check the Web application

Open an browser and type in the address <http://127.0.0.1:8080/>. You
should be able to see the landing page of Seedcase Portal. You could try
to access the admin part of the portal with address
<http://127.0.0.1:8080/admin>, using the username and password you set
up in the `.env.django` file. After you log in to the admin part, you
could try to add more data.

## Stop and run the docker containers.

To stop the container, while in the main `seedcase/` folder, run:

``` bash
docker compose down
```

It will stop and remove all the containers, but all the data will be
stored in the local computer. To start the container again, run the same
command like above except without the `--build`, since you've already
built the image.

``` bash
docker compose up -d
```

## Build and run tests

To build, start and run all tests, run the command under the main
`seedcase/` folder. Please utilize this script to ensure the successful
completion of all tests following any modifications made to the code.

``` bash
sh integration_build.sh
```

<!-- TODO: Where does the data get saved? -->
