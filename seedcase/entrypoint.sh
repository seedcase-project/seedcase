#!/bin/sh

## Function to be called if any step of the deployment fails.
fail_deploy() {
    if [ -n "$1" ]; then
        echo "Failing deployment: $1"
    else
        echo "Failing deployment"
    fi
    exit 1  # proceed no further!
}

# If the development flag is set, perform the development specific database actions
if [ ${DEVELOPMENT:-0} == 1 ]; then
  echo "For development configuration, run flush"
  python manage.py flush --no-input || fail_deploy "Flush Failed"
fi

yes | python manage.py makemigrations || fail_deploy "Make Migration Failed"
python manage.py migrate --run-syncdb || fail_deploy "Migrate Failed"

# If the development flag is set, use env superuser info to create default user
if [ ${CREATE_SUPERUSER:-0} == 1 ]; then
  echo "Setup default superuser for development"
  python manage.py createsuperuser --no-input
  echo "Completed Setup sueper user"
fi

exec "$@"
