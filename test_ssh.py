import paramiko
import os
# 服务器相关信息,下面输入你个人的用户名、密码、ip等信息


ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ip = "54.254.249.245"
port =  22
user = "ubuntu"
password = "qwerdf886"
private = paramiko.RSAKey.from_private_key_file('/home/.ssh/authorized_keys/')
privatekey = os.path.expanduser(password)

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

key = paramiko.RSAKey.from_private_key_file(privatekey)
# 建立连接
ssh.connect(ip,port,user,password,pkey=key,timeout = 10)
#输入linux命令
stdin,stdout,stderr = ssh.exec_command("lh")
# 输出命令执行结果
result = stdout.read()
print(result)
#关闭连接
ssh.close()
