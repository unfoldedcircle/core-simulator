FROM python:3.11-slim-bullseye

WORKDIR /app

RUN apt update && apt -y install git && \
    git clone https://github.com/unfoldedcircle/integration-python-library.git && \
    apt clean

RUN cd integration-python-library && \
    pip3 install build setuptools setuptools_scm && \
    python3 -m build && \
    pip3 install --force-reinstall dist/ucapi-*-py3-none-any.whl

ENV UC_INTEGRATION_INTERFACE=0.0.0.0

WORKDIR /app/integration-python-library/examples

CMD ["python3", "setup_flow.py"]
