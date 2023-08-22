#!/bin/bash

black --line-length=79 .
ruff check . --fix
