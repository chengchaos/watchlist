#!/usr/bin/env bash

gunicorn --config=config.py app:app

