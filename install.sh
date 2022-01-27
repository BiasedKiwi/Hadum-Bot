#! /bin/bash

echo "Starting Hadum install script..."

bash scripts/verify.sh # Run integrity check script
echo "Installing dependencies"
pipenv install || pip3 install -r requirements.txt. # Install dependencies with pipenv, if it fails, use pip3 instead.

echo "Find your Discord token here: https://discord.com/developers/applications/"
echo "Find your Reddit info here: https://www.reddit.com/prefs/apps"
echo "Please input your Discord token below". # Get config info
read DSC_TOKEN
echo "Please input your Reddit Client secret below"
read REDDIT_SECRET
echo "Please input your Reddit Client ID below"
read REDDIT_ID

echo "Configuring environment variables..." # Create environment variables
echo "TOKEN="$DSC_TOKEN > .env
echo "REDDIT_CLIENT_SECRET="$REDDIT_SECRET > .env
echo "REDDIT_CLIENT_ID="$REDDIT_ID > .env

echo "Done!"
