import tweepy,csv,TwitterAPIKey#TwitterAPIKey.pyで、認証を受けたアカウントのkeyを保持
from datetime import timedelta


acountpass="***"#@以下のユーザ名
OUTPUT_FILE_NAME=acountpass+".csv"
FOLD_PATH= "/Users/***/***/"
OUTPUT_FILE= FOLD_PATH+"/"+OUTPUT_FILE_NAME

#認証keyを呼び出し
CK=TwitterAPIKey.CK
CS=TwitterAPIKey.CS

#API認証
auth=tweepy.OAuthHandler(CK,CS)
api=tweepy.API(auth)

#ツイート取得
tweet_data = []
for tweet in tweepy.Cursor(api.user_timeline,screen_name =acountpass,exclude_replies = True).items():
    tweet_data.append([tweet.id,str(tweet.created_at+timedelta(hours=9)),tweet.text.replace('\n',''),tweet.favorite_count,tweet.retweet_count])

#csv出力
with open(OUTPUT_FILE_NAME, 'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id","created_at","text","fav","RT"])#get data item
    writer.writerows(tweet_data)
pass
