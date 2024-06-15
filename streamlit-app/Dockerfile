
FROM python:3.9-slim


WORKDIR /app


COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8501


CMD ["streamlit", "run", "--server.port", "8501", "--server.enableCORS", "false", "--server.headless", "true", "--browser.serverAddress", "0.0.0.0", "app.py"]
