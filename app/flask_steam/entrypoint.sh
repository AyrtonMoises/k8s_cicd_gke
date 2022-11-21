#!/bin/bash

flask db upgrade || exit 1

exec "$@"
