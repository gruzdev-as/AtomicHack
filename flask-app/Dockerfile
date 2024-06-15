
FROM python:3.9-slim


WORKDIR /app


RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py


EXPOSE 5000


CMD ["flask", "run", "--host=0.0.0.0"]
