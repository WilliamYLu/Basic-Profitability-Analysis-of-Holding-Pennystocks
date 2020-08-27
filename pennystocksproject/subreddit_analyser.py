import praw
import re
import pprint

class stock:
    def __init__(self, share_purchase, price):
        self.price = price
        self.share_purchase = share_purchase

reddit = praw.Reddit(client_id="R6XxWae2CTlBwQ",
                     client_secret="EIAfVDjte2_YHAM8dXpjlL54_1s",
                     user_agent="pennystocksproject by SuperNoobyGamer",
                     password="williamberkeley1225",
                     username ="SuperNoobyGamer"
                     )

list_of_non_stock_names = ["DD","BUY", 'MMA', 'FDA',"HQ",'NEXT', 'BEYO', 'AIR', 'DUE', 'DILI', 'INSI', 'DUST', 'FEDE', 'STOC', 'THAT', 'WILL', 'GO', 'TO', 'JUPI', 'BACK', 'RESE', 'POST', 'GET', 'IMO', 'PCI', "FA", 'NDA', 'ADHD', 'SSR', "TA", 'BS', 'ON', 'ROCK', 'MUST', 'READ', "NEW","SCAM","NEWS", "INC", "PR", "THE", "WHY", "EVER", 'ACH', 'COVI', 'WAKE', 'UP', 'AND', 'SMEL', 'COFF', "FLIR", "HUGE", "WATC"]
stock_name_pattern = re.compile("\$[A-Z]+|[A-Z]{2,4}")
for submission in reddit.subreddit("pennystocks").top(limit=10000):
    if (submission.link_flair_text == ("DD")):
        #print(submission.title, submission.author, submission.link_flair_text)
        #pprint.pprint(vars(submission))
        words = submission.title.split(" ")
        goodWords = {"hello"}
        goodWords.remove("hello")
        for word in words:
            if stock_name_pattern.search(word)!= None and "DD" not in word:
                match = stock_name_pattern.search(word)
                if match.group(0) not in list_of_non_stock_names:
                    goodWords.add(match.group(0).replace("$",""))
        if len(goodWords) > 0:
            print(goodWords)
