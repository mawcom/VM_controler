import paramiko

cliente = paramiko.SSHClient()

cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

cliente.connect(
    hostname="192.168.56.10", 
    username="servico",
    password="3141" 
)

stdin, stdout, stderr = cliente.exec_command("ls -l /var/")

print(stdout.read().decode())

cliente.close()
