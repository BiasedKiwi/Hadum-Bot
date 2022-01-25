#! /bin/bash

echo "Starting Hadum install script..."

sudo bash scripts/verify.sh

echo "Find your Discord token here: https://discord.com/developers/applications/"
echo "Find your Reddit info here: https://www.reddit.com/prefs/apps"
echo "Please input your Discord token below"
read DSC_TOKEN
echo "Please input your Reddit Client secret below"
read REDDIT_SECRET
echo "Please input your Reddit Client ID below"
read REDDIT_ID

echo "Configuring environment variables..."
echo "TOKEN="$DSC_TOKEN > .env
echo "REDDIT_CLIENT_SECRET="$REDDIT_SECRET > .env
echo "REDDIT_CLIENT_ID="$REDDIT_SECRET > .env

echo "Done!"