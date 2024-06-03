FROM public.ecr.aws/docker/library/python:3.11.6-slim-bookworm

# Update and install dependencies
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    build-essential cmake poppler-utils tesseract-ocr libgl1 && \
    apt-get install -y --no-install-recommends \
    libglib2.0-0 libmagic-mgc libmagic1 libnss3 libnspr4 libdbus-1-3 libatk1.0-0 && \
    apt-get install -y --no-install-recommends \
    libatk-bridge2.0-0 libcups2 libdrm2 libxcb1 libxkbcommon0 libatspi2.0-0 libx11-6 && \
    apt-get install -y --no-install-recommends \
    libxcomposite1 libxdamage1 libxext6 libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 libasound2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install lambda web adapter
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.7.0 /lambda-adapter /opt/extensions/lambda-adapter

WORKDIR /backend

COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./app ./app

ENV PORT=8000
EXPOSE ${PORT}
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
