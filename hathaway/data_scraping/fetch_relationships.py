import requests
import time

def get_followers(access_token, user_id, count=200, cursor=0):
    url = 'https://api.weibo.com/2/friendships/followers.json'
    params = {
        'access_token': access_token,
        'uid': user_id,
        'count': count,
        'cursor': cursor
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get('users', []), data.get('next_cursor', 0)


def crawl_limited_followers(access_token, user_id, max_followers):
    followers = []
    cursor = 0

    while len(followers) < max_followers:
        users, cursor = get_followers(access_token, user_id, cursor=cursor)
        if not users:
            break
        followers.extend(users)

        # 如果已经达到上限，截取到达上限的部分并停止
        if len(followers) > max_followers:
            followers = followers[:max_followers]
            break

        time.sleep(1)  # 避免频率限制，每次请求间隔一段时间

    return followers


# 示例调用
access_token = 'your_access_token'
user_id = 'target_user_id'
max_followers = 500  # 设置最多爬取500个粉丝

limited_followers = crawl_limited_followers(access_token, user_id, max_followers)

print(f"Total followers fetched: {len(limited_followers)}")
