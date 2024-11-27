# concert_db

https://platform.openai.com/api-keys
위 링크에서 회원가입 후 API Key 발급.
발급 후, 해당 코드를 본인의 notion 등에 저장.

터미널에서, 아래와 같이 입력하여 코드 복사.
```
  git clone https://github.com/2yunsu/concert_db.git)
```
터미널에서, 아래와 같이 입력하여 필요한 모듈 다운로드.
```
  pip install openai re
```
chatgpt_images.py 파일 5번째 줄에, api_key = "" 사이에 아까 발급 받은 자신의 API Key 입력.
```
  client = OpenAI(
      api_key="Your API Key",
  )
```
concert_db.csv 파일과 같이 csv 파일의 2열에 이미지 링크 추가
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
