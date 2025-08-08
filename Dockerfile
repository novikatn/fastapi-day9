FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync

COPY . .

EXPOSE 8000

CMD ["./bin/start.sh"]