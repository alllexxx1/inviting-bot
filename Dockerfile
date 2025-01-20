FROM python:3.11.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    make \
    sqlite3

RUN python3 -m pip install --upgrade pip

COPY /configuration/requirements.txt  .
COPY Makefile  .
RUN make install

COPY . .

RUN chmod a+x migration.sh
RUN make migrate

CMD ["make", "run"]
