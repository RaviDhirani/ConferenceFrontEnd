# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6
ENV PYTHONUNBUFFERED 1
# create root directory for our project in the container
RUN mkdir /Project1

# Set the working directory to /music_service
WORKDIR /quiz-web-application-django

# Copy the current directory contents into the container at /music_service
ADD . /quiz-web-application-django

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
