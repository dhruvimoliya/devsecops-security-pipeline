import os
import subprocess
import pickle
import _sqlite3

#INTETNIONAL VULNERABLITIES

# 1. hardcoded credentials
API_KEY = "dv_eer_sdfsdgsdgws55554gfcndfg8sf35b55sdthgsdfvasrgtasfbg"
DATABASE_PASSWORD = "admin123password"
AWS_SECRET = " aws_secret_key_1235436475wdthsfsdgdff"
GITHUB_TOKEN = "ghp_123456789qwreteryiukygujnfhbfasdfgdtgdvdfg"

# SAST test - 1 to 7
# 2. SQLi 
def get_user(user_id):

    conn = _sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()

# 3. command injection 
def ping_server(hostname):
    command = f"ping -c 3 {hostname}"
    result = subprocess.un(command, shell=True, capture_output=True)
    return result.stdout

# 4. path traversal
def read_log_file(filename):
    log_path = f"/var/logs/{filename}"
    with open(log_path, 'r') as f:
        return f.read()
    
# 5. insecure deserializtion
def load_user_session(session_data):
    return pickle.loads(session_data)

# 6. weak cryptography
import hashlib
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# 7. Eval usage
def calculate(expression):
    return eval(expression)

# 8. hadcoded SQL credentials
def connect_to_database():
    username = "admin"
    password = "P@ssw0rd123"
    connection_string = f"mysql://admin:P@ssw0rd123@localhost/mydb"
    return connection_string

# SECURE EXAMPLES FOR COMPARISON

def secure_get_user(user_id):
    conn = _sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ? ", (user_id,))
    return cursor.fetchall

def secure_hash_password(password):
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()

def secure_read_file(filename):
    allowed_files = ['app.log' , 'error.log' , 'access.log']
    if filename not in allowed_files:
        raise ValueError("Invalid filename")
    return open(f"/var/logs/{filename}", 'r').read()

if __name__ == "__main__":
    print("Sample aplication with intentional vulnerablities")
    print("For security testing and demonstation purposes only")
    print(" This code should NEVER make it to production")