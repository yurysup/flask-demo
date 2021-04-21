# Demo flask application

Sandbox project for Python/Flask web app.

## Installation & prerequisites

1. Install Git:
><https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>

2. Install Docker & Docker Compose:

><https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9> - installation for Amazon EC2\
<https://docs.docker.com/compose/install/> - Docker official\
<https://docs.docker.com/engine/install/> - Docker Compose official

## Usage

### Docker

Clone repo and run docker-compose:
```bash
git clone https://github.com/yurysup/flask-demo.git
cd flask-demo
docker-compose up -d --build
```
Check if containers are running via:
```bash
docker-compose ps
```

Gunicorn will be listening on 80 port.

### Grafana

Configure dashboard for Prometheus [nodeExporter](https://github.com/prometheus/node_exporter). Any dashboard from existing collection could be used, like:
><https://grafana.com/grafana/dashboards/11074>