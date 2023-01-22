from __future__ import annotations
from typing import NoReturn

import requests
import logging
from datetime import datetime
from functools import reduce

DAILY_CHINALIST_URL = 'https://raw.githubusercontent.com/pexcn/daily/gh-pages/chinalist/chinalist.txt'
DAILY_GFWLIST_URL = 'https://raw.githubusercontent.com/pexcn/daily/gh-pages/gfwlist/gfwlist.txt'
MY_CHINALIST_PATH = 'script/my_chinalist.txt'
MY_GFWLIST_PATH = 'script/my_gfwlist.txt'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_online_list(url: str) -> list[str]:
    logging.info(f'Fetching online list... ({url})')
    try:
        response = requests.get(url, timeout=10)
        online_list = response.text.split()
        logging.info(f'Fetched {len(online_list)} URLs.')
        return online_list
    except requests.exceptions.ConnectionError:
        logging.critical('Connection error.')
        exit(1)


def get_local_list(path: str) -> list[str]:
    logging.info(f'Reading local list... ({path})')
    try:
        with open(path) as file:
            local_list = file.read().split()
    except FileNotFoundError:
        local_list = []
    logging.info(f'Read {len(local_list)} URLs from {path}.')
    return local_list


def joint_list(*lists: list[str]) -> list[str]:
    logging.info('Jointing lists...')
    jointed_list = set()
    jointed_list.update(*lists)
    # noinspection PyTypeChecker
    logging.info(f'Got {reduce(lambda a, b: f"{a}+{b}", [len(l) for l in lists])}={sum(len(l) for l in lists)} URLs. '
                 f'After jointing, remain {len(jointed_list)} URLs.')
    return sorted(jointed_list)


def filter_list(ori_list: list[str], filter_out_list: list[str]) -> list[str]:
    logging.info('Filtering list...')
    f_list = set(filter_out_list)
    df_list = set('.' + f for f in f_list)
    filtered_list = list(
        filter(
            lambda o: (
                    o not in f_list
                    and
                    (
                        o.count('.') <= 1  # TLD/2LD, shortcut
                        or
                        all(not o.endswith(d) for d in df_list)  # match subdomain
                    )
            ),
            ori_list
        )
    )
    logging.info(f'Got {len(ori_list)} URLs to be filtered, {len(filter_out_list)} URLs to be filtered out. '
                 f'After filtering, remain {len(filtered_list)} URLs.')
    return filtered_list


def update_txt(new_list: list[str], path: str) -> NoReturn:
    logging.info(f'Updating {path}...')
    with open(path, 'w') as file:
        file.write('\n'.join(new_list))


def main():
    old_list = get_local_list('chinalist_plain.txt')

    daily_chinalist = get_online_list(DAILY_CHINALIST_URL)
    daily_gfwlist = get_online_list(DAILY_GFWLIST_URL)
    my_gfwlist = get_local_list(MY_GFWLIST_PATH)
    filtered_list = filter_list(daily_chinalist, joint_list(daily_gfwlist, my_gfwlist))

    my_list = get_local_list(MY_CHINALIST_PATH)
    jointed_list = joint_list(filtered_list, my_list)

    if jointed_list == old_list:
        logging.info('No update.')
        return

    info = f'[AutoProxy 0.2.9]\n! Updated: {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")}'
    omega_list = [info, '! This chinalist only works with SwitchyOmega.',
                  '! For other versions, please check https://github.com/Rongronggg9/chinalist']
    smart_list = [info, '! This chinalist is expected to be used on SmartProxy.',
                  '! For other versions, please check https://github.com/Rongronggg9/chinalist']
    for url in jointed_list:
        omega_list.append(f'||{url}')
        smart_list.append(f'@@||{url}')

    update_txt(omega_list, 'chinalist_omega.txt')
    update_txt(smart_list, 'chinalist_smart.txt')
    update_txt(jointed_list, 'chinalist_plain.txt')

    logging.info('Update finished.')


if __name__ == '__main__':
    main()
