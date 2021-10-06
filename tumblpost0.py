import pytumblr

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  'blah',
  'blah',
  'blah',
  'blah'
)

print("Choose type. 0=Text, 1=Quote")
choice = input()

if (choice == "0"):
	print("Enter title:")
	title1 = input()
	print("Enter body:")
	body1 = input()
	client.create_text("andalsomuchcattle",title=title1,body=body1)
else:
	print("Enter quote:")
	quote1 = input()
	print("Enter source:")
	source1 = input()
	client.create_quote("andalsomuchcattle",quote=quote1,source=source1)  



