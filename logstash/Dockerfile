# Create custom image for logstash
# - Installed logstash-input-tcp plugin
# - Installed logstash-input-gelf plugin

# Pull image
FROM docker.elastic.co/logstash/logstash:7.6.2

# RUN bin/logstash-plugin update
# Install logstash-tcp input plugin
RUN bin/logstash-plugin install logstash-input-tcp
# Install logstash-gelf input plugin
RUN bin/logstash-plugin install logstash-input-gelf

# Remove default logstash config
RUN rm -f /usr/share/logstash/pipeline/logstash.conf

# Replace pre-defined config and pipeline
ADD pipeline/ /usr/share/logstash/pipeline/
ADD config/ /usr/share/logstash/config/