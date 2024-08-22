# Use the official Nginx image as a base
FROM nginx:latest

# Copy custom configuration file to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Create the custom content directory
RUN mkdir -p /var/opt/nginx/html

# Copy the custom index.html to the new directory
COPY index.html /var/opt/nginx/html/index.html

# Expose port 80
EXPOSE 80

