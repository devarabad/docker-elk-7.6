# Docker ELK Stack 7.6 #
Docker ELK Stack 7.6 (Elasticsearch Cluster with Basic Configuration for Kibana and Logstash)

## Requirements ##
* Docker Installed
* Docker resource memory must be 4GB or higher
    * If you are using Docker Desktop, go to Settings > Advanced and set the memory to 4GB or higher

### Getting Started ###
1. Go to the project directory
    ```
    $ cd docker-elk-7.6
    ```
2. Run stack using docker compose
    ```
    $ docker-compose up --build
    # To exit, press CTRL+C
    ```
3. To teardown the stack
    ```
    $ docker-compose down
    ```

### Accessing the Application ###
1. Check the docker machine's ip if using Docker Toolbox, for Docker Desktop use localhost instead
    ```
    $ docker-machine ip
    http://{docker-machine-ip} or http://localhost
    ```
2. Access and validate the services
    ```
    # Elasticsearch
    $ curl http://localhost:9200
    $ curl -X GET "localhost:9200/_cat/nodes?v&pretty"

    # Kibana
    $ curl http://localhost:5601

    # Logstash
    # Run sample python program
    $ cd logstash
    $ python send-message-to-logstash-via-tcp.py
    ```