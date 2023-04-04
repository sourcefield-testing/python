#!/bin/sh -l

echo "Hello $1"
echo "${GITHUB_WORKSPACE}"
time=$(date)
echo "::set-output name=time::$time"
ls -l .
grep -R "class Foo" .
ssh-keygen -t rsa -P "" -b 4096 -m PEM -f jwtRS256.key
ssh-keygen -e -m PEM -f jwtRS256.key > jwtRS256.key.pub
cat jwtRS256.key.pub
