# Python/Oracle Docker Image

This image is based on the official Python image and adds the Oracle Instant Client.

The FastAPI framework is installed and a simple example is provided, running on port 8000
## Usage

Set the .env file with local environmental variables

```
DB_USERNAME=user
DB_PASSWORD=12345
DB_SERVER=192.168.68.10/orcl_db_name
```


```bash ./start.sh```

If you want to run verbosly, you can use:

```bash docker-compose up --build```
