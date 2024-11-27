from openai import OpenAI

client = OpenAI(
    api_key="",
)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "위 이미지에서 공연자, 공연 장소, 공연 시기, 공연 내용을 csv 파일 형식으로 순서대로 나열해줘."},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://ticketimage.interpark.com/Play/image/large/24/24016428_p.gif",
          },
        },
      ],
    }
  ],
  max_tokens=100,
)

# print("response: ", response)
# print("response.choices[0]: ", response.choices[0])
print("response.choices[0].message: ", response.choices[0].message)