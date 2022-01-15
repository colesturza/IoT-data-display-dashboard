#  IoT-data-display-dashboard

A simple flask app that receives MQTT messages from an IoT device and displays the data on a dashboard. The data is stored in a MongoDB database. Chart.js is used to display the data. The Chart.js zoom and streaming plugins are used to make viewing the data easier. The app is meant to be deployed using Kubernetes and Docker. A DockerFile is provided in the app's directory.
