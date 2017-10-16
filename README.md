# Twitter illust collector

This script collects 2d illust from twitter lists and posts them to slack.

## Getting Started

```
git clone https://github.com/joisino/twitter_illust_collector.git
cd twitter_illust_collector
```

At first, clone the repository.

```
pip install -r requirements.txt
```

Then, install dependencies.

```
emacs config.py
```

Next, you have to fill twitter API keys and slack API URL in `config.py`.

```
python3 twitter_illust_collector.py
```

Finally, you can run the script and it collects illusts and post them to slack.

You can register this script to cron and it automatically collects images.
