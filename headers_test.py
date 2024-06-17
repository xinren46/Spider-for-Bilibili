def get_headers():
    headers = {
        'Accept-Encoding': '',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
        'referer': 'https://www.bilibili.com/'
    }

    cookie = {}
    cookie_temp = "buvid3=E6BF7841-F113-2893-86CC-689FEEE1C6F192864infoc; b_nut=1715664892; CURRENT_FNVAL=4048; _uuid=95FE1C510-BACE-82A5-773E-66814109D43C591439infoc; buvid_fp=c1c307962dab16715b57438344a29984; buvid4=216B42FB-9745-34E8-DEA9-CC6500879B2B94493-024051405-wwxMkPf2bkD6yEKn4IwC0u6auoxoj2QadRirOaMxyMmJFRrPahjPwq6QFLibVAUd; rpdid=|(Y|Ym))uR~0J'u~ulYYR)m); enable_web_push=DISABLE; header_theme_version=CLOSE; home_feed_column=4; browser_resolution=1229-603; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTg3MDM3NzgsImlhdCI6MTcxODQ0NDUxOCwicGx0IjotMX0.etfDEgOyfmDW8r5nvvPZpORk6uzx52NGxKNyl1jqYoY; bili_ticket_expires=1718703718; b_lsid=411035612_190252EED03; bsource=search_baidu; SESSDATA=511903d8%2C1734162778%2C411e8%2A62CjDV43pCgmr3XIzN5ED9ZgdIaR1gTj5LY0yz_INEmCEPX2gEWx1HTAnDfKn-d6yLLLISVlRTVXhRVWpXdWR5LWFXb0NtYV9fRFlDNndNZktYYzcwNVBnckNHWjJCMzYwcjI1cEN4ZUF5cVUyNVpTeUZfMVJ6QVM2N2l2V01jdnBYZ2tVOExFejhBIIEC; bili_jct=697f97a3ba327deb4c3b96d22329c91b; DedeUserID=404270928; DedeUserID__ckMd5=92d940d808d40991; sid=65tck0mu"

    for i in cookie_temp.split(';'):
        cookie[i.split('=')[0]] = i.split('=')[1]

    return cookie, headers
