## 1. Base image: Choose a Python image
FROM python:3.10-slim

# 2. Set a working directory inside the container
WORKDIR /app

# 3. Copy your project files into the container
COPY . .

# 4. Install the dependencies
RUN pip install pandas scikit-learn matplotlib

# 5. Expose a port (optional, only if running a web app)
# EXPOSE 5000

# 6. Command to run your ML script
CMD ["python", "day-3.py"]
