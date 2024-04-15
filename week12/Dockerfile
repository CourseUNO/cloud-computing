FROM python:latest

WORKDIR /app
# Copy requirements.txt
COPY * .
# Install the specified packages
RUN pip install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["python", "main.py"]