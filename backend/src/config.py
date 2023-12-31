from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITH")
environment = os.getenv("ENV", "development")


env_variables = {
    "secret_key": secret_key,
    "algorithm": algorithm,
    "environment": environment,
}

origins = ["http://localhost:3001"]
methods = ["POST", "GET", "PUT", "DELETE"]
