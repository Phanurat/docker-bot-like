# Dockerfile
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Update and install necessary dependencies
RUN apt-get update \
    && apt-get install -y wget unzip \
    && rm -rf /var/lib/apt/lists/*

# Download and install Chrome browser (if needed)
# You can uncomment and use these lines if you need Chrome installed in your container
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
#     && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
#     && apt-get update \
#     && apt-get install -y google-chrome-stable \
#     && rm -rf /var/lib/apt/lists/*

# Download and install ChromeDriver
RUN wget https://chromedriver.storage.googleapis.com/$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin/ \
    && rm chromedriver_linux64.zip

# Copy Python script and requirements file to the container
COPY requirements.txt .
COPY event-action/event-link-post.py event-action/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for Python
ENV PYTHONUNBUFFERED=1

# Command to run the Python script
CMD ["python", "./event-action/event-link-post.py"]
