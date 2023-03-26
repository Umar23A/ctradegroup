FROM python:3
RUN mkdir /ctrade
COPY . /ctrade
WORKDIR /ctrade
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
