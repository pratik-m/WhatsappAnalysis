"""general.py
this module has the common statistic related fucntions
"""


def list_users(df):
	""" prints list of users

	Parameters:
	df : Pandas dataframe
	Dataframe of all messages

	"""

print('List of Users\n')

for user in df.user.unique():
print(user)


def print_msg_stats(df):
""" prints general stats about the messages
- Total messages
- Total messages per hour
- Total number of words & letters
- Total days in chat
- Average lenght of messages
- Average response time of messages
- Total # of media item sent

Args:
df (Dataframe): Dataframe of all messages


Retruns:
None

Notes:

Raises:

Todo:


"""

df['count_word'] = df.message.apply(lambda msg: len(msg.split()))
df['count_letter'] = df.message.apply(lambda msg: len(msg))

print(f'Total # of messages sent: {df.message.count}')
print(f'Total # of words in messages: {df.count_word.sum()}')
print(f'Total # of words in messages: {df.count_letter.sum()}')

#Total # of days in chat
print(f'Total days in chat: {df.date.count()}')

# average lenght of message
print(f'Average lenght of message: {df.count_word.avg()}')



# Media Stats
# there are 2 types of media - images and videos

# df['msg_image'] = df.message_clean.str.find('image omitted')
# df['msg_video'] = df.message_clean.str.find('video omitted')

# df.msg_image = df.msg_image.apply(lambda x: 0 if x < 0 then 1)
# df.msg_video = df.msg_video.apply(lambda x: 0 if x < 0 then 1)

# print(f'Total # of images shared: {df.msg_image.sum()}')
# print(f'Total # of video shared: {df.msg_video.sum()}')








