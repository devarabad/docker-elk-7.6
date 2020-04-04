# Create custom image for kibana

# Pull image
FROM docker.elastic.co/kibana/kibana:7.6.2

# Remove default kibana config
RUN rm -f /usr/share/kibana/config/kibana.yml

# Replace pre-defined config
ADD config/kibana.yml /usr/share/kibana/config/kibana.yml