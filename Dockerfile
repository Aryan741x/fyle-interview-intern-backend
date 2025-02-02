FROM python:3.11-slim
WORKDIR /app
COPY . .   
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=core.server  
ENV FLASK_RUN_HOST=0.0.0.0  
ENV FLASK_RUN_PORT=5000  
ENV FLASK_ENV=development  
CMD ["flask", "run"]