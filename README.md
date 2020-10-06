<<<<<<< HEAD
# docker-pyftpdlib
Simple FTP server with pyftpdlib


## Running the server:
```
1) docker-compose up
[I 2016-04-29 18:01:49] >>> starting FTP server on 0.0.0.0:21, pid=5
[I 2016-04-29 18:01:49] concurrency model: async
[I 2016-04-29 18:01:49] masquerade (NAT) address: None
[I 2016-04-29 18:01:49] passive ports: None
```

In another terminal run `ftp localhost` and you should get something like this:
```
Connected to 192.168.99.100.
220 pyftpdlib 1.5.0 ready.
Name (192.168.99.100:akogut): user
331 Username ok, send password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp>

or you can install filezile and connect using host : localhost , user : user , password : password , port : 21
```

## Develop by
Rehmat Ali Sayany
