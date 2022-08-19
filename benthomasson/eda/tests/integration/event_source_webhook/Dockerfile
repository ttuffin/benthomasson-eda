FROM registry.access.redhat.com/ubi9/python-39
USER 0

RUN pip install requests
RUN mkdir /scripts && chmod a+rwx /scripts
COPY ./scripts/webhook_client.py /scripts
