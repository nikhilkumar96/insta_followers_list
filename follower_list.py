# Get instance
import instaloader
L = instaloader.Instaloader()

username = ''
password = ''

# Login or load session
L.login(username, password)        # (login)


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "shab_e_intizaar")

# Print list of followees




followers_list = []
for followee in profile.get_followers():
    username = followee.username
    followers_list.append(str(username))



following_list = []

for following in profile.get_followees():
    username = following.username
    following_list.append(str(username))

count =0
for item in following_list:
    if item not in followers_list:
        print(item)
        count += 1

print('total = ', count-1)

