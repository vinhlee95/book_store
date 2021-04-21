#!/bin/bash
# See: https://docs.docker.com/compose/startup-order/

set -e

#host="$1"
#shift

# Expect a linked database container named 'db'.
cmd="$@"

until psql $DATABASE_URL -c '\l'; do  # If no linked db container, try DATABASE_URL
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

exec $cmd
