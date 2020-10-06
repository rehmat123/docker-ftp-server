import os.path
import argparse

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def run_ftpd(user, password, host, port, passive, anon):
    authorizer = DummyAuthorizer()
    authorizer.add_user("rehmat", "rehmat", "files/rehmat", perm="elradfmw")
    if anon:
        authorizer.add_anonymous("files/nobody")

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.permit_foreign_addresses = True

    passive_ports = map(int, passive.split('-'))
    handler.passive_ports = range(passive_ports[0], passive_ports[1])
    

    server = FTPServer(("127.0.0.1", 21), handler)
    server.serve_forever()


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--user', default='user',
        help="Username for FTP acess (user will be created)")
    parser.add_argument('--password', default='password',
                        help="Password for FTP user.")
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8000)
    parser.add_argument('--passive', default='3000-3010',
                        help="Range of passive ports")
    parser.add_argument('--anon', action='store_true',
                        help="Allow anonymous access")
    args = parser.parse_args()
    run_ftpd(**vars(args))

if __name__ == '__main__':
    main()
