#!/bin/bash

exec uvicorn src.app.example:app --host 0.0.0.0 --port 3030 --log-level info