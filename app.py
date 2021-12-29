import re

with open("followers.txt") as f:
    text = f.read()
followers = re.findall(r'title="(.*?)" href="\/\1\/"', text)
print(f"Got {len(followers)} followers!")

with open("following.txt") as f:
    text = f.read()
following = re.findall(r'title="(.*?)" href="\/\1\/"', text)
print(f"Got {len(following)} following!")

print()

notFollowingYou = []

for f in following:
    if f not in followers:
        notFollowingYou.append(f)

print(f"These {len(notFollowingYou)} people are not following you:")

for f in notFollowingYou:
    print(f)
        