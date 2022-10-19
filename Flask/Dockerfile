FROM python:3.9.6
WORKDIR /usr/src/Flask
COPY . .
CMD ["python", "-m", "venv", "."]
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000:5000
ENV PYTHONUNBUFFERED=1
CMD ["python","-u","main.py"]