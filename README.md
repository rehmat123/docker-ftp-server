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
=======
# docker-ftp-server
Containerize application to make FTP server using python and docker

Steps </b>

1) clone project
2) run 'docker-compose up'
3) open ftp://localhost:21
>>>>>>> 842ef57b977d6cc192cdbd8d572b6216c277d36d
