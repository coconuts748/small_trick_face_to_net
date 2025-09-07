import requests

original_ip_pool = []
available_ip_pool = []

def original_pool(get_ip_url):
    """
    Total progress as:
    First: Get the ips.....
    Second: Check whether available.......
    Third: Return the available ips(AS to column_format).....
    """
    # get_ip_url = 'http://www.zdopen.com/ShortProxy/GetIP/?api=202508310622313322&akey=9ccd5b3572e6013a&count=111111&fitter=2&timespan=5&type=3'

    try:
        r= requests.get(get_ip_url)
        if r.status_code == 200:
            print()
            json_format = r.json()
            data = json_format['data']
            proxy_list = data['proxy_list']
            for i in proxy_list:
                ######
                ip = i['ip']
                port = i['port']
                integrated_ip = f'{ip}:{port}'
                ######
                print(integrated_ip)
                original_ip_pool.append(integrated_ip)
            print('all original ips are stored successfully')
            return original_ip_pool

        else:
            print(r.status_code)

    except Exception as e:
        print('11111')
        print(e)

# original_pool('http://www.zdopen.com/ShortProxy/GetIP/?api=202508310622313322&akey=9ccd5b3572e6013a&count=6&fitter=2&timespan=5&type=3')


def whether_available():
    original_pool('typing_url_here..........')
    try:
        print()
        for i in original_ip_pool:
            each_proxy = {
                'http': 'http://' + i,
                'https': 'https://' + i
            }
            test_url = 'https://www.baidu.com/'
            try:
                r = requests.get(test_url, proxies=each_proxy)
                if r.status_code == 200:
                    print(f'this ip: {i} is available')
                    available_ip_pool.append(i)

                else:
                    print(f'this ip: {i} is NOT available')
                    pass

            except Exception as e:
                print('33333')
                print(e)

    except Exception as e:
        print('22222')
        print(e)

# whether_available()


def build_ip_pool(source_url):
    original_pool(source_url)
    whether_available()

# build_ip_pool('type_url_here.....')