# Services

- dashboard
- data_collector

The main service is contained in the `./dashboard/` directory. The `mqtt_data_collector` service is used to subscribe to the MQTT broker and store data in the MongoDB database. The `mqtt_data_collector` service was created to prevent duplicate instances of data being collected and stored in the database. The dashboard service is meant to be scaled out horizontally so that many users can view the data without experiencing latency.

To test changes made during development use the Docker Compose file provided. This will build and run the various containers needed. For quick changes being made to either of the flask apps, it is easier to run them outside of a container first.