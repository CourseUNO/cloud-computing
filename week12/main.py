import os
import socket
import uvicorn
from ec2_metadata import ec2_metadata
from fastapi import FastAPI



app = FastAPI()

db = 'use RDS' if os.environ.get("RDS") else 'do not use RDS'

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
msg = f"Hello from ECS, {ip_address}-{hostname}; {db}"


@app.get("/")
async def root():

    try:
        return {
            "message": msg,
            "metadata": {
                "public_ipv4": ec2_metadata.public_ipv4,
                "public_hostname": ec2_metadata.public_hostname,
                "region": ec2_metadata.region,
                "instance_id": ec2_metadata.instance_id,
                "domain": ec2_metadata.domain
            }
        }
    except:
        return {"message": msg}




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
