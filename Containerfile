FROM registry.access.redhat.com/ubi8-minimal:latest

RUN microdnf install python3

WORKDIR rapitester

COPY rapitester.py .
COPY resources .



