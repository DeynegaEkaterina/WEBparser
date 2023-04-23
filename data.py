headers = {
    'authority': 'alpindustria.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,nl;q=0.8',
    # 'cookie': 'session_id=191629199; session_key=fpfmn; _ym_uid=1682173637928830714; _ym_d=1682173637; tmr_lvid=dfdc06f4b17faef611033a858ae27c9b; tmr_lvidTS=1682173637264; _userGUID=0:lgs2r1l9:RI0wYJnnA9HmiVLnIb6uQfzT~HPAx6Wf; PHPSESSID=ac1103cc6434ac137fdbd1523805508f; _ga=GA1.2.811155030.1682173638; _gid=GA1.2.1282476162.1682173638; _ym_visorc=w; ssaid=c8b72070-e119-11ed-91af-7508ad76af0f; _ym_isad=1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; iwaf_fingerprint=5dea374830c47b90cdde145e13ea141a; subscribe_panel=0; utmParams=?div=catalog&cat=knigi&page=1; utmParams=?div=catalog&cat=knigi&page=1; tmr_detect=1%7C1682176756509; _gat_gtag_UA_10925516_10=1; _gat_UA-10925516-7=1; _dc_gtm_UA-10925516-7=1; _gat=1; mindboxDeviceUUID=1ff9bd98-2556-4119-8cbc-0085c6ccb2de; directCrm-session=%7B%22deviceGuid%22%3A%221ff9bd98-2556-4119-8cbc-0085c6ccb2de%22%7D; iwaf_scroll_event=1457; __tld__=null; iwaf_click_event=72x165',
    'dnt': '1',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.2.806 Yowser/2.5 Safari/537.36',
}
cookies = {
    'session_id': '191629199',
    'session_key': 'fpfmn',
    '_ym_uid': '1682173637928830714',
    '_ym_d': '1682173637',
    'tmr_lvid': 'dfdc06f4b17faef611033a858ae27c9b',
    'tmr_lvidTS': '1682173637264',
    '_userGUID': '0:lgs2r1l9:RI0wYJnnA9HmiVLnIb6uQfzT~HPAx6Wf',
    'PHPSESSID': 'ac1103cc6434ac137fdbd1523805508f',
    '_ga': 'GA1.2.811155030.1682173638',
    '_gid': 'GA1.2.1282476162.1682173638',
    '_ym_visorc': 'w',
    'ssaid': 'c8b72070-e119-11ed-91af-7508ad76af0f',
    '_ym_isad': '1',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    'iwaf_fingerprint': '5dea374830c47b90cdde145e13ea141a',
    'subscribe_panel': '0',
    'utmParams': '?div=catalog&cat=knigi&page=1',
    'utmParams': '?div=catalog&cat=knigi&page=1',
    'tmr_detect': '1%7C1682176756509',
    '_gat_gtag_UA_10925516_10': '1',
    '_gat_UA-10925516-7': '1',
    '_dc_gtm_UA-10925516-7': '1',
    '_gat': '1',
    'mindboxDeviceUUID': '1ff9bd98-2556-4119-8cbc-0085c6ccb2de',
    'directCrm-session': '%7B%22deviceGuid%22%3A%221ff9bd98-2556-4119-8cbc-0085c6ccb2de%22%7D',
    'iwaf_scroll_event': '1457',
    '__tld__': 'null',
    'iwaf_click_event': '72x165',
}

url: str = "https://alpindustria.ru/"

# В комментарии указано реальное количество страниц в каждой категории
# Для сокращения времени выполнения кода количество страниц было уменьшено

nav = [[f"{url}?div=catalog&cat=odejda&page=", 2], #235
       [f"{url}?div=catalog&cat=obuv&page=", 2],#59
       [f"{url}?div=catalog&cat=turisticheskoe-snaryajenie&page=", 2],#168
       [f"{url}?div=catalog&cat=alpinistskoe-snaryajenie&page=", 2],#134
       [f"{url}?div=catalog&cat=gornye-lyji&page=", 2],#53
       [f"{url}?div=catalog&cat=ekspedicionnye-lyji&page=", 2],#33
       [f"{url}?div=catalog&cat=splitbordy&page=", 2],#2
       [f"{url}?div=catalog&cat=knigi&page=", 2]]#10