FROM python:3.14-slim

WORKDIR /app

COPY *.py .
CMD ["python", "Inventory_manager.py"]