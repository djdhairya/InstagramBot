from instagrapi import Client
with open("credentials.txt","r") as f:
    username,password=f.read().splitlines()
client =Client()
client.login(username,password)
hashtag="programming"
medias=client.hashtag_medias_recent(hashtag,20)
for i,media in  enumerate(medias):
    client.media_like(media.id)
    print(f"Liked post number {i+1} of hashtag {hashtag}")
    if i % 5 =0:
        client.user_follow(media.user.pk)
        print(f"Follwed user{media.user.username}")
        client.media_comment(media.i,"Awesome post")
        comment=random.choice(comments)
        print(f"Commented {comment} under post number {i+1}")