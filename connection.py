import paramiko # type: ignore


import func 

cliente = paramiko.SSHClient()

cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

cliente.connect(
    hostname="192.168.56.10", 
    username="servico",
    password="3141" 
)
    
print(func.Syslog(3141, cliente))
cliente.close()
