#Download base image python 3.5
FROM python:3.5
RUN echo "Asia/Tehran" > /etc/timezone

WORKDIR /my_bot

COPY ./requirements.txt /my_bot/requirements.txt

RUN pip install -r requirements.txt

COPY ./ /my_bot

CMD ["python3.5", "default_bot.py"]

