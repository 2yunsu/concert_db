# concert_db

https://platform.openai.com/api-keys
위 링크에서 회원가입 후 API Key 발급.
발급 후, 해당 코드를 본인의 notion 등에 저장.

  git clone https://github.com/2yunsu/concert_db/

  pip install openai re

두 파일의 api_key = "" 사이에 자신의 API Key 입력.

  client = OpenAI(
      api_key="Your API Key",
  )

chatgpt_images.py 실행 시,
concert_db.csv 파일과 같이 csv 파일의 2열에 이미지 링크 정리

  python chatgpt_images.py
