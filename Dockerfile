FROM python:3.8

WORKDIR /Hadum

# Installs dependencies

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Build Arguments

ARG token
ARG reddit_secret
ARG reddit_id
ARG reddit_user

# Environment variables

ENV DB_IP=localhost

ENV TOKEN=${token}

ENV REDDIT_CLIENT_SECRET=${reddit_secret}
ENV REDDIT_CLIENT_ID=${reddit_id}
ENV REDDIT_USER_AGENT=${reddit_user}

# Runs the bot

WORKDIR /Hadum/src
CMD [ "python", "main.py" , "-v"]
