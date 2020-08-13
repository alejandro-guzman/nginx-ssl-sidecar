FROM python:3.7.7-buster AS builder

WORKDIR /build

COPY README.md ./README.md
COPY setup.py ./setup.py
COPY simpleapi/ ./simpleapi

RUN pip install --upgrade pip setuptools wheel

RUN python setup.py bdist_wheel

FROM python:3.7.7-buster
COPY --from=builder /build/dist /tmp/dist

RUN pip install --compile /tmp/dist/*
RUN rm -rf /tmp/dist

ENTRYPOINT ["simple-api"]