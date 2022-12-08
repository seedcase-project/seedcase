# Setup the Seedcase Instruction

## 1. Download and install Docker

Please download the Docker for your operating system from this link https://docs.docker.com/get-docker/

Your will download and install the Docker engine and Docker's user friendly application as Docker desktop. Please follow the instruction to download and install the application.

## 2. Start Docker Engine

The easy to start the Docker Engine is just start the Docker Desktop application from you computer. Make sure the docker is running properly you could use your command line tool to check, with command "docker --version". If you find the warning message "Cannot connect to the Docker daemon" in the output, it means that the docker engine is not started on your local, please check if the docker desktop started properly.

## 3. Some basic Docker command

Some of the docker commands you may use, you could try it from your command line tool.
1. "docker help" list all docker commands
2. "docker ps" list running docker containers
3. "docker images" list all created local docker images
4. "docker start" Start one or more docker containers.
5. "docker stop" stop one or more containers
6. "docker compose up" Run the docker containers from the docker compose file
7. "docker compose down" Stop and remove all docker containers from the docker compose file.

## 4. Setup the Environment file
Please create a file named as ".env.django" in this folder. Find the file named "env_example", copy and paste all the content in it to the new file (.env.django) you just created. Please fill up "DJANGO_SUPERUSER_USERNAME", "DJANGO_SUPERUSER_EMAIL" and "DJANGO_SUPERUSER_PASSWORD" in the file ".env.django" and save it. You will later use this username and password to login to the admin part of the web application.

## 5. Run the docker containers
Please use the command line tool, access the current folder. Run "Docker compose up -d --build" under this folder. Docker will try to download all the required packages, images to the local, and try to run it. After a while, you should be able to find the print out of "Container demo_version_containers-db Started, Container django_webapp Started". It means all the docker containers configuration are completed.

## 6. Check the Web application

Open an browser, type the address "http://127.0.0.1:8080/". You should be able to see the landing page of Seedcase Portal. You could try access the admin part of the portal with address "http://127.0.0.1:8080/admin", and please use the username and password you setup previously to login. After you login to the admin part, you could try to add more data, such as organization data, project data.

## 7. Stop and run the docker containers.

If you need to stop the containers, please run command "docker compose down" from this folder. It will stop and remove all the containers, but all the data will be store in the local. If you need to start the containers again, you could run "docker compose up -d" since you already have the docker images builded in your local.
