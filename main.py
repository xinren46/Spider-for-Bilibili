### by xinren46 ###

from get_download import *
import headers_test

base_url = 'https://www.bilibili.com/video/BV1SS4y1D7de'  # 改bv号爬取即可  change BV string to go

if __name__ == '__main__':
    tuple_1 = headers_test.get_headers()  # 取请求头
    response = get_response(url=base_url, cookies=tuple_1[0], headers=tuple_1[1])

    info_tuple = get_video_audio_info(response)  # 取视频音频url
    subtitle_url = get_subtitle_info(response)  # 取字幕url

    if subtitle_url == 0:
        print('No automatic subtitle generation, end downloading subtitles.')
    else:
        download_subtitle(subtitle_url, info_tuple[2])

    download_video(info_tuple)

    print('over!')
