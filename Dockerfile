FROM python:3.9-alpine

# setting environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# setting working directory
WORKDIR /code

# copying requirements file before hand help
COPY requirements.txt /code/

# install dependencies
RUN apk add --no-cache musl-dev g++ libstdc++
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install pandas

# copy all files
COPY . /code/
