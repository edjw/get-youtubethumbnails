from main import get_youtube_thumbnail

valid_test_urls = [
    "https://www.youtube.com/watch?v=BPo_0iAPYQY",
    "www.youtube.com/watch?v=BPo_0iAPYQY",
    "youtube.com/watch?v=BPo_0iAPYQY",
    "https://youtu.be/BPo_0iAPYQY",
    "youtu.be/BPo_0iAPYQY",
    "https://www.youtube-nocookie.com/embed/BPo_0iAPYQY",
    "www.youtube-nocookie.com/embed/BPo_0iAPYQY",
    "youtube-nocookie.com/embed/BPo_0iAPYQY",
    "https://www.youtube.com/watch?v=dnDTegvF_9k&index=2&list=PL8fxHB06heRO4gZ7m04-9weFSSow9NXMt&t=4s",
]
print("Valid URL tests\n")
for yt_url in valid_test_urls:
    print(get_youtube_thumbnail(yt_url))
print("\n-----\n")

invalid_test_urls = [
    "www.youtu.be/BPo_0iAPYQY",
    "https://www.youtube.com/watch?v=dnDTegvF_9Y",
    "https://www.youtube.com/feed/subscriptions",
    "https://www.youtube.com/feed/trending?disable_polymer=1",
    "https://google.com",
    "google.com",
    "www.google.com",
]

print("Invalid URL tests\n")
for yt_url in invalid_test_urls:
    print(get_youtube_thumbnail(yt_url))
