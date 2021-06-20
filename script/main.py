import requests
from datetime import datetime


def get_online_list(url):
    response = requests.get(url)
    online_list = response.text.split()
    return online_list


def get_local_list(path):
    with open(path) as file:
        local_list = file.read().split()
    return local_list


def joint_list(*lists):
    jointed_list = []
    for single_list in lists:
        jointed_list.extend(single_list)
    return sorted(jointed_list)


def update_txt(list, path):
    with open(path, 'w') as file:
        file.write('\n'.join(list))


if __name__ == '__main__':
    daily_chinalist_url = 'https://raw.githubusercontent.com/pexcn/daily/gh-pages/chinalist/chinalist.txt'
    my_chinalist_path = 'script/my_chinalist.txt'

    daily_chinalist = get_online_list(daily_chinalist_url)
    my_list = get_local_list(my_chinalist_path)
    jointed_list = joint_list(daily_chinalist, my_list)

    info = f'! Updated: {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")}'
    omega_list = ['[AutoProxy 0.2.9]', info]
    smart_list = ['[AutoProxy 0.2.9]', info]
    for url in jointed_list:
        omega_list.append(f'||{url}')
        smart_list.append(f'@@||{url}')

    update_txt(omega_list, 'chinalist_omega.txt')
    update_txt(smart_list, 'chinalist_smart.txt')
