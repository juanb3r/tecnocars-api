# El siguiente archivo es la configuración de Dockerfile

# set the base image. Since we're running
# a Python application a Python base image is used
FROM python:3.9.5
# set a key-value label for the Docker image
LABEL maintainer="Dager Almanza"
# copy files from the host to the container filesystem.
# For example, all the files in the current directory
# to the  `/app` directory in the container
COPY . .
#  defines the working directory within the container
WORKDIR /

ENV PATH=sqlite:///tecnocars.db
# run commands within the container.
# For example, invoke a pip command
# to install dependencies defined in the requirements.txt file.
RUN pip install -r requirements.txt
# provide a command to run on container start.
# For example, start the `app.py` application.
CMD [ "python", "uvicorn", "config:app", "--reload"]
# To expose the desire port
EXPOSE 8000
