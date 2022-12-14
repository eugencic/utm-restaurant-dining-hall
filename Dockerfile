FROM python:3.11.0rc2-bullseye

# Make a directory for the application
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy our source code
COPY /app .

# Expose port
EXPOSE 3000

# Run the application
CMD ["python", "-u", "dining_hall.py"]