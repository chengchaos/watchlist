#!/usr/bin/env bash

cat log/gunicorn.pid | xargs kill

