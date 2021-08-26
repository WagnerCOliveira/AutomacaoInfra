#!/bin/bash
source .virtualenvs/testinfra/bin/activate
pytest -v dnsTest.py 
deactivate
