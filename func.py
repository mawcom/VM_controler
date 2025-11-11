def Syslog(password,client):
    stdin, stdout, stderr = client.exec_command("sudo -S tail /var/log/syslog")
    stdin.write(f"{password}\n")
    stdin.flush()
    saida = stdout.read().decode()

    return saida

def storage(client):
    stdin, stdout, stderr = client.exec_command("free -h")
    saida = stdout.read().decode()

    return saida

def system_info(client):
    stdin, stdout, stderr = client.exec_command("uname -a")
    saida = stdout.read().decode()

    return saida

def cpu_usage(client):
    stdin, stdout, stderr = client.exec_command("uptime")
    saida = stdout.read().decode()

    return saida

def whoami(client):
    stdinA, stdoutA, stderrA = client.exec_command("hostname")
    stdin, stdout, stderr = client.exec_command("w")
    saida =  f"usuario atual: {stdoutA.read().decode()}\n {stdout.read().decode()}"

    return saida

def ip(client):
    stdin, stdout, stderr = client.exec_command("ip a")
    saida = stdout.read().decode()

    return saida

