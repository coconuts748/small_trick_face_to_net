from 已完成.attack.build_ip_pool import available_ip_pool,build_ip_pool
from 已完成.attack.attack_content import attack_content
from 已完成.attack.attack_progress_page1 import first_ui
from 已完成.attack.attack_progress_page2 import second_ui


def total_control_here(ip_source_net):
    first_ui(ip_source_net)
    second_ui()

# total_control_here(ip_source_net='https://www.baidu.com/') #type ip source net here.......
