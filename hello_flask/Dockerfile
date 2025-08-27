# Build stage
FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install flask redis
EXPOSE 5007
CMD ["python","app.py"]