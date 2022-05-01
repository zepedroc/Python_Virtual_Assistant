import speedtest

test = speedtest.Speedtest()


def list_closest_servers():
    print()
    print('-------Servidores Mais Próximos-------')
    for server in test.get_closest_servers():
        print()
        print('Url: ', server['host'])
        print('Localização: ', server['name'], ', ', server['cc'])
        print('Providenciado por: ', server['sponsor'])


def list_internet_connection_info():
    server = test.get_best_server()
    print()
    print('Operadora: ', test.config['client']['isp'])
    print('Localização: ', server['name'], ',', server['cc'])
    print('Latência: ', server['latency'], 'ms')
    print()
    # Values in Mb/s with 2 decimals
    print(f'Velocidade Download:  {test.download() / 1024 / 1024:.2f}Mb/s')
    print(f'Velocidade Upload:  {test.upload() / 1024 / 1024:.2f}Mb/s')
