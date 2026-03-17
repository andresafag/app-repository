# Use the official Postgres image as a base
FROM postgres:16

# Set environment variables for PostgreSQL
# These variables configure the initial database setup
ENV POSTGRES_USER=$POSTGRES_USER
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD
ENV POSTGRES_DB=$POSTGRES_DB


# Optional: Copy initialization scripts
# Scripts placed in the /docker-entrypoint-initdb.d/ directory will be run
# when the container is first created with an empty data volume
COPY ./init.sql /docker-entrypoint-initdb.d/

