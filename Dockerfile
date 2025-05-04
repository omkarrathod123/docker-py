FROM python
WORKDIR /app
COPY . /app

CMD [ "python", "index.py" ]