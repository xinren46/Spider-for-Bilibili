import re
import requests
import json
import headers_test


def get_response(url, headers, cookies):
    response = requests.get(url=url, headers=headers, cookies=cookies)

    return response


def get_video_audio_info(response):
    # 视频音频的源码段
    html_1 = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]  # 第一个playinfo后json是视频信息
    video_audio_html = json.loads(html_1)

    video_url = video_audio_html['data']['dash']['video'][0]['backup_url'][0]  # 视频url
    audio_url = video_audio_html['data']['dash']['audio'][0]['backup_url'][0]  # 音频url
    name = re.findall('<title data-vue-meta="true">(.*?)_', response.text)[0]  # 名字 name

    return video_url, audio_url, name


def get_subtitle_info(response):
    try:
        subtitle_url = re.findall('subtitle_url":"(.*?)"', response.text)[0]  # 字幕url
        subtitle_url = str(subtitle_url.replace(r'\u002F', '/'))

        return subtitle_url

    except IndexError:

        return 0


def download_video(info_tuple):
    print('video-audio-downloading...')

    video_url = info_tuple[0]
    audio_url = info_tuple[1]
    video_name = info_tuple[2] + '.mp4'
    audio_name = info_tuple[2] + '.mp3'

    video_response = requests.get(url=video_url, headers=headers_test.get_headers()[1])
    audio_response = requests.get(url=audio_url, headers=headers_test.get_headers()[1])
    #
    with open(video_name, 'wb') as fp_v:
        fp_v.write(video_response.content)

    with open(audio_name, 'wb') as fp_a:
        fp_a.write(audio_response.content)


def download_subtitle(subtitle_url, name):
    subtitle_response = requests.get(url=subtitle_url)

    with open(name + '.json', 'w', encoding='utf-8') as fp_s:
        fp_s.write(subtitle_response.text)
        print('subtitle download!')
