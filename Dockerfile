FROM python:3.12-bookworm

# Lazımi paketləri quraşdır
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends ffmpeg git \
    && rm -rf /var/lib/apt/lists/*

# İş qovluğu
WORKDIR /app

# Faylları konteynerə kopyala
COPY . .

# Python paketləri quraşdır
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# start faylının icazəsini düzəlt
RUN chmod +x start

# Prosesləri idarə et
CMD ["bash", "-c", "gunicorn app:app --bind 0.0.0.0:8000 & exec ./start"]
