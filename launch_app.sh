#!/bin/bash

docker build -t file-management-app .

docker run -p 5001:5001 file-management-app
