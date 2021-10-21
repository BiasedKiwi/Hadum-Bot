FROM python:3.8

WORKDIR /Hadum

# Installs dependencies

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Build Arguments

ARG token

# Environment variables

ENV DB_IP=localhost
ENV TOKEN=$token

# Runs the bot

WORKDIR /Hadum/src
CMD [ "python", "main.py" , "-v"]
