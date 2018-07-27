#!/usr/bin/env bash
set -e

# Choose command
case "$1" in
api)
    shift
    exec aioworkers -c config.yaml $@
    ;;
tests)
    shift
    pipenv install --dev --system
    pytest
    ;;
*) exec "$@"
esac

exit $?
