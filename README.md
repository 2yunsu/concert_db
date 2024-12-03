# concert_db

https://platform.openai.com/api-keys
링크에서 회원가입 후 API Key 발급.

발급 후, 해당 코드를 본인의 notion 등에 저장.

API 비용 결제(1000토큰에 0.002$).

터미널에서, 아래와 같이 입력하여 코드 복사.
```
git clone https://github.com/2yunsu/concert_db.git
```

터미널에서, 아래와 같이 입력하여 가상환경 생성 및 필요한 모듈 다운로드.
```
conda create -n concert_db python=3.11
```
```
conda actiavate concert_db
```
```
pip install openai re
```
chatgpt_images.py 파일 5번째 줄에, api_key = "" 사이에 아까 발급 받은 자신의 API Key 입력.
```
client = OpenAI(
  api_key="Your API Key",
  )
```
concert_db.csv 파일과 같이 csv 파일의 2열에 이미지 링크 추가.
```
number, URL
1, https://ticketimage.interpark.com/Play/image/large/24/24016428_p.gif
2, https://ticketimage.interpark.com/Play/image/large/P0/P0004075_p.gif
...
```
터미널에서, 아래와 같이 입력하여 파이썬 파일 실행.
```
python chatgpt_images.py
```

출력 예시
```
response_content:  
임현정, 예술의전당, 2024-12-05, 피아노 협주곡 1, 2, 3, 4 및 파가니니 주제에 의한 랩소디

response_content:  
SEO PIL WON, 체임버홀, 2024-12-04 19:30, 쇼팽 에튀드 전곡 연주

response_content:  
정문채, 금호아트홀, 12.7, 기타 독주회
```
chatgpt_images.py 파일의 아래 코드에서 "포스터의 공연자,..." 문구를 수정하여 프롬프트 수정이 가능하며, max_token을 통해 출력 최대 토큰을 조절 가능.
```
messages=[
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "포스터의 공연자, 공연 장소, 공연 시기, 공연 내용만 csv 파일 형식으로 순서대로 나열하고 다른 말은 하지마."},
            {
                "type": "image_url",
                "image_url": {"url": image_url},
            },
        ],
    }
],
max_tokens=100,
```

이후, 생성된 concert_db_added.csv 파일에 공연자, 공연 장소, 공연 시기, 공연 내용 추가되어 저장됨.

ref)
https://platform.openai.com/docs/guides/vision
