import speedtest

test = speedtest.Speedtest()


def list_closest_servers():
    print()
    print('-------Closest Servers-------')
    for server in test.get_closest_servers():
        print()
        print('Url: ', server['host'])
        print('Location: ', server['name'], ', ', server['cc'])
        print('Provider: ', server['sponsor'])


def list_internet_connection_info():
    server = test.get_best_server()
    print()
    print('ISP: ', test.config['client']['isp'])
    print('Location: ', server['name'], ',', server['cc'])
    print('Latency: ', server['latency'], 'ms')
    print()
    # Values in Mb/s with 2 decimals
    print(f'Download Speed:  {test.download() / 1024 / 1024:.2f}Mb/s')
    print(f'Upload Speed:  {test.upload() / 1024 / 1024:.2f}Mb/s')
