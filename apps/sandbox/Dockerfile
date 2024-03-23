FROM ubuntu:22.04

# Set the timezone to Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/Europe/Berlin /etc/localtime && echo Europe/Berlin > /etc/timezone

# Update package lists and install necessary dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip openjdk-8-jdk curl git

# Set environment variables for Java
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV PATH $PATH:$JAVA_HOME/bin

# Install Node.js version 20.x
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
RUN apt-get install -y nodejs

# Install quicktype globally
RUN npm install -g quicktype

# # Copy only the requirements file first
# COPY requirements.txt .

# Install project dependencies
RUN pip3 install poetry
# RUN pip3 install -r requirements.txt

# Download and verify Apache Spark
RUN curl -fsSL https://dlcdn.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz -o spark.tgz \
    && if [ -s spark.tgz ]; then echo "Spark download successful."; else echo "Error: Spark download failed."; exit 1; fi \
    && tar xzf spark.tgz \
    && mv spark-3.5.1-bin-hadoop3* /opt/spark \
    && rm spark.tgz

# Set environment variables for Spark
ENV SPARK_HOME /opt/spark
ENV PATH $PATH:$SPARK_HOME/bin

# Copy the rest of your project files
COPY . .

# Expose port 80 if your application listens on that port
EXPOSE 80

# Set the working directory
WORKDIR /src

RUN poetry shell

# set the python interpreter to it
RUN poetry env use python3


# Set the default command to run your application
CMD ["python3", "main.py"]


