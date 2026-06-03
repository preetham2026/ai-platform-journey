FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY day12.py .
COPY ritham_farm.db .
EXPOSE 5000
CMD ["python", "day12.py"]
