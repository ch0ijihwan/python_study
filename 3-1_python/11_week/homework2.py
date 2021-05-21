lyrics = 'Half of my hear is in Havana'

lyrics_one = lyrics.split()
lyrics_two = (lyrics.upper()).split()
t_list= []

for i in zip(lyrics_one,lyrics_two):
    t_list.append(i)

print(t_list)
