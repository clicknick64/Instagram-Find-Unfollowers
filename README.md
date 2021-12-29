# Instagram: Find non followers

Simple script to find who doesn't follow you back without giving it your password

## Usage

- Go into your Instagram profile on a browser
- Click on followers
- Scroll all the way down until all followers are loaded
- Right-click and press Inspect (element)
- Right-click the \<html\> tag (second line) in the elements tab and copy the element
- Paste it into **followers.txt**
- Do the same for the following and paste it in **following.txt**
- Run **python3 app.py**