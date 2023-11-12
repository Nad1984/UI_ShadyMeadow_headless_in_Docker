FROM python:3.8-alpine3.10 as compiler

WORKDIR /app/

RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

RUN echo "http://dl-4.alpinelinux.org/alpine/v3.10/main" >>/etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.10/community" >>/etc/apk/repositories

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ui_test/ .

FROM python:3.8-alpine3.10 as runner

WORKDIR /app/

RUN apk update \
    && apk add chromium chromium-chromedriver \
    && apk add libffi-dev

RUN pip install pytest

COPY --from=compiler /opt/venv /opt/venv

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . /app/

ENV BASE_URL=$BASE_URL

CMD python -m pytest -s

