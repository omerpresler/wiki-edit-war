# Wikipedia Edit Wars: Bias and Conflict Analysis

This project analyzes edit wars and bias patterns in Wikipedia articles related to the Israeli-Palestinian conflict. It includes web scraping, sentiment analysis, bias classification, and social network analysis to understand editorial behavior on politically sensitive pages.

## 📌 Project Goals

- Identify bias (Pro-Israel / Pro-Palestinian / Neutral) in edit comments.
- Detect sentiment and urgency in revision activity.
- Visualize editing trends over time.
- Map revert-based interactions between editors.

## 📊 Key Features

- ✅ Keyword-enhanced Wikipedia revision crawler (topic-specific)
- ✅ Sentiment analysis using TextBlob
- ✅ Bias classification using a custom-trained NLTK + sklearn pipeline
- ✅ LLM evaluation (DeepSeek, DistilBERT, etc.) and performance benchmarking
- ✅ Network graph of revert behavior across editors
- ✅ Time-based analysis correlating edits with real-world events

## 📈 Notable Results

- Wikipedia edit volume spikes after major geopolitical events (e.g., Oct 2023 attacks).
- Most frequent reverts were self-reverts or between ideologically opposed editors.
- LLMs performed well on handcrafted examples but failed on large Reddit datasets.
- Final classifier: fast sklearn-based model trained on weakly-labeled Reddit data.

## 📁 Data Files
Place these two CSV files in your data/ folder:

- data/posts.csv

- data/reddit_comments_clean.csv

## 🤖 Pre-trained Models
In your models/ folder, download or clone the following Hugging Face model repositories (clickable links included for copy/paste convenience):

- deepseek-llm-7b   https://huggingface.co/deepseek-ai/deepseek-llm-7b-chat

- DeepSeek-V2-Lite  https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite

- bart-large-mnli   https://huggingface.co/facebook/bart-large-mnli

## 👤 Author

**Omer Presler**  
omerpr@post.bgu.ac.il

## 📄 License

MIT License – see the `LICENSE` file for details.
