from openai import OpenAI
client = OpenAI()

def get_dream_story_and_interpretation(dream_text):
    # 꿈을 스토리로 작성
    response_story = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"다음 꿈의 스토리가 짧고 부족한데, 좀 더 풍부하면서도 오리지널에서 벗어나지 않게 한 문단으로 반말로 작성해줘: {dream_text}"}
        ]
    )
    story = response_story.choices[0].message.content

    # 꿈의 의미 풀이
    response_interpretation = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"다음 꿈의 의미를 뻔하지 않고 재미있게 한 문단으로 존댓말로 해석해줘: {dream_text}"}
        ]
    )
    interpretation = response_interpretation.choices[0].message.content

    return story, interpretation

if __name__ == "__main__":
    dream_text = input("꿈 내용을 입력하세요: ")

    story, interpretation = get_dream_story_and_interpretation(dream_text)

    print("\n--- 꿈 이야기 ---")
    print(story)
    print("\n--- 꿈 풀이 ---")
    print(interpretation)