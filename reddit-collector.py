import praw
import csv
import time

KEYWORD = "war"

# Reddit API Client
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent=""
)

def collect_popular_comments(subreddit_name, keyword, label=None):
    subreddit = reddit.subreddit(subreddit_name)
    print(f"Searching in subreddit: {subreddit_name}")

    # Search posts containing the keyword

    for submission in subreddit.search(keyword, sort="relevance", limit=10000):  # adjust limit
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            if comment.score > 25:  # filter for popular comments
                yield {
                    #"subreddit": subreddit_name,
                    "submission_id": submission.id,
                    #"submission_title": submission.title,
                    #"comment_id": comment.id,
                    "comment_body": comment.body,
                    #"comment_score": comment.score
                    "label": label,
                }

ISRAEL_SUBREDDITS = ["Israel", "Jewish", "Judaism", "IDF"]
all_data = []

for subreddit in ISRAEL_SUBREDDITS:
    time.sleep(2)  # Sleep to avoid hitting API rate limits
    try:
        all_data.extend(collect_popular_comments(subreddit, KEYWORD, "with israel"))
    except Exception as e:
        print(f"Error collecting data from {subreddit}: {e}")
        time.sleep(120)  # Wait before retrying
        all_data.extend(collect_popular_comments(subreddit, KEYWORD, "with israel"))
        

PALESTINE_SUBREDDITS = ["Palestine", "MiddleEastNews", "AskMiddleEast", "Gaza"]

for subreddit in PALESTINE_SUBREDDITS:
    time.sleep(2)  # Sleep to avoid hitting API rate limits
    try:
        all_data.extend(collect_popular_comments(subreddit, KEYWORD, "with palestine"))
    except Exception as e:
        print(f"Error collecting data from {subreddit}: {e}")
        time.sleep(120)
        all_data.extend(collect_popular_comments(subreddit, KEYWORD, "with palestine"))

# Export results
with open("self_collected_war_subreddit_comments.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=all_data[0].keys())
    writer.writeheader()
    writer.writerows(all_data)
