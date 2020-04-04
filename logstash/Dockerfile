# Create custom image for logstash
# - Installed logstash-input-tcp plugin

# Pull image
FROM docker.elastic.co/logstash/logstash:7.6.2

# Install logstash-tcp plugin
# RUN bin/logstash-plugin update
RUN bin/logstash-plugin install logstash-input-tcp

# Remove default logstash config
RUN rm -f /usr/share/logstash/pipeline/logstash.conf

# Replace pre-defined config and pipeline
ADD pipeline/ /usr/share/logstash/pipeline/
ADD config/ /usr/share/logstash/config/