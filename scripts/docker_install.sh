#! /bin/bash

echo "Please enter your Discord bot token: "
read token
echo "Please enter your Reddit application secret below"
read reddit_secret
echo "Please enter your Reddit application ID below"
read reddit_id
echo "Please enter your Reddit username below"
read reddit_user
echo "Building using Docker..."

docker build --build-arg token=$token \
 --build-arg reddit_secret=$reddit_secret \
  --build-arg reddit_id=$reddit_id \
   --build-arg reddit_user=$reddit_user -q .