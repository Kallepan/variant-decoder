#!/bin/bash
docker rm -f uta_20170117
docker run -d --name uta_20170117 -p 15032:5432 biocommons/uta:uta_20170117