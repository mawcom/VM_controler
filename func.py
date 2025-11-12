import paramiko

# informações do sistema 

def Syslog(password,client):
    while True:
        escolha = input(str("qual parte você deseja: \n 1: head \n 2: cat \n 3: tail"))
        if escolha == "1":
            escolha = "head"
            break
        if escolha == "2":
            escolha = "cat"
            break
        if escolha == "3":
            escolha = "tail"
            break
        else:
            print("comando invalido")

    stdin, stdout, stderr = client.exec_command(f"sudo -S {escolha} /var/log/syslog")
    stdin.write(f"{password}\n")
    stdin.flush()

    resposta = f"Syslog:\n{stdout.read().decode()}\nerr0{stderr.read().decode()}"

    return resposta

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

#gerenciamento de arquivos e diretórios

def listdic(client):
    dic = input("digite o caminho: ")
    stdin, stdout, stderr = client.exec_command(f"ls -la {dic}")

