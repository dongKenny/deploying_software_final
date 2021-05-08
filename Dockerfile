FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY ../deploying_software_final /app
CMD ["python", "app.py"]
