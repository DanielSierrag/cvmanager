FROM python:3.13.2-alpine3.21

RUN addgroup app && adduser -S -G app app
RUN apk add --no-cache \
    mariadb-dev \
    gcc \
    musl-dev \
    python3-dev
USER app
WORKDIR /app/
COPY --chown=app:app requirements.txt .
RUN pip install -r requirements.txt
# RUN pipenv shell
COPY --chown=app:app . .
# COPY . .
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]