# Services

- dashcboard
- db (for development)
- mqtt_broker (for development)

The main application is contained in dashboard. The `db` directory contains a Dockerfile to containerize a MongoDB database for development purposes.

To test changes made during development use the Docker Compose file provided. This will build and run the various containers needed. For quick changes being made to the flask app it is easier to run it outside of a container first with a .