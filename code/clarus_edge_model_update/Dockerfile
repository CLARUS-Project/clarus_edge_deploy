FROM python:3.9-slim

# Install cron
RUN apt-get update && apt-get install -y cron

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY ./requirements.txt /code/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of the code
COPY . .

# Create a directory for the model
RUN mkdir -p model 

# Give execution rights on the cron job
RUN chmod +x cronjob.sh

# Run the cron job
RUN crontab crontab.txt

# Run the command on container startup to start cron in the foreground
CMD ["cron", "-f"]