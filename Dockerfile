FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /supermarket
COPY requirements.txt /supermarket/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /supermarket/
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
