import praw
import pandas as pd

# Reddit API Client
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent=""
)

# Subreddits and Keywords
subreddits = ["israel", "palestine", "worldnews", "news", "politics"]
search_keywords = ["israel", "palestine", "gaza", "idf", "hamas", "zionism", "occupation"]
limit_posts = 50
comments_per_post = 20

# Heuristic keyword lists
pro_israel_keywords = [
    "idf", "hamas is a terrorist", "support israel", "stand with israel",
    "defend israel", "anti-semitism", "hezbollah", "rockets from gaza", "terrorist"
]

pro_palestine_keywords = [
    "free palestine", "end the occupation", "zionist", "genocide", "apartheid",
    "israel is the aggressor", "resistance", "colonialism", "israeli war crimes"
]

def auto_label(text):
    s = text.lower()
    israel_score = sum(1 for kw in pro_israel_keywords if kw in s)
    palestine_score = sum(1 for kw in pro_palestine_keywords if kw in s)

    if israel_score > palestine_score:
        return "pro_israel"
    elif palestine_score > israel_score:
        return "pro_palestine"
    elif israel_score == 0 and palestine_score == 0:
        return "neutral"
    else:
        return "neutral"  # fallback for ties

# Scrape + label
data = []

for sub in subreddits:
    print(f"Scraping subreddit: r/{sub}")
    for post in reddit.subreddit(sub).search(" OR ".join(search_keywords), limit=limit_posts, sort='top'):
        post.comments.replace_more(limit=0)
        for comment in post.comments[:comments_per_post]:
            label = auto_label(comment.body)
            data.append({
                "text": comment.body,
                "subreddit": sub,
                "post_title": post.title,
                "url": post.url,
                "label": label
            })

# 💾 Save to CSV
df = pd.DataFrame(data)
df.to_csv("reddit_comments_auto_labeled.csv", index=False)
print(f"Saved {len(df)} comments to reddit_comments_auto_labeled.csv")
print(df["label"].value_counts())
