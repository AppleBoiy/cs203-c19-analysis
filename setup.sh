#!/usr/bin/env bash

python3 prerequisite.py || python prerequisite.py

kaggle datasets download -d yasirabdaali/corona-virus-covid19-us-counties && unzip corona-virus-covid19-us-counties.zip
