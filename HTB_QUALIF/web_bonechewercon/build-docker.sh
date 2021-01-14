#!/bin/bash
docker build --tag=web_bonechewercon .
docker run -p 1337:80 --rm --name=web_bonechewercon web_bonechewercon