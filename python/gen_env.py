import socket
import secrets
import argparse
from pathlib import Path

ENV_FILE = ".env"
DB_PASS_ENV = "DB_PASS"
IMG_TAG = "IMG_TAG"

def is_port_free(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.bind(("127.0.0.1", port))
            return True
        except OSError:
            return False

def find_free_port(start: int = 8000, end: int = 8999) -> int:
    for port in range(start, end + 1):
        if is_port_free(port):
            return port
    raise RuntimeError(f"No free port found in {start} - {end}")

def generate_db_pass():
    return secrets.token_urlsafe(24)


def read_env_file(path):
    data = {}
    path = Path(path)
    if not path.exists():
        return data
    for line in path.read_text().splitlines():
        line = line.strip()
        key, value = line.split("=", 1)
        data[key] = value.strip()
    return data

def write_env_file(path, data):
    path = Path(path)
    lines = [f"{key}={value}" for key, value in data.items()]
    path.write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Gen env file")
    parser.add_argument("--dev", action="store_true", help="Set project env")
    parser.add_argument("--deploy", action="store_true")
    parser.add_argument("--prj_name", default="backend")
    parser.add_argument("--img_tag", default="latest")
    args = parser.parse_args()

    env_data = read_env_file(ENV_FILE)
    if args.dev:
        env_data["PRJ_ENV"] = "dev"
    else:
       env_data["PRJ_ENV"] = "prod"
    env_data["PRJ_NAME"] = args.prj_name

    if "APP_PORT" not in env_data:
        env_data["APP_PORT"] = str(find_free_port(8080, 8090))

    if DB_PASS_ENV not in env_data or not env_data["DB_PASS_ENV"]:
        env_data["DB_PASS_ENV"] = generate_db_pass()

    if args.deploy:
        env_data[IMG_TAG] = args.img_tag
    
    write_env_file(ENV_FILE, env_data)
    print("Env file updated")

if __name__ == "__main__":
    try:
        main()
    except RuntimeError as error:
        print(f"Error: {error}")
