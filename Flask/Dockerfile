FROM python:3.9.6
WORKDIR /usr/src/Flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000:5000
CMD ["python", "main.py"]