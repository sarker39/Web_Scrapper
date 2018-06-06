import datetime

now = str(datetime.datetime.now())
date = now.split(' ')[0].strip()

datesplit = date.split('-')
print(datesplit)
newdate = datesplit[0]+'/'+datesplit[1]+'/'+datesplit[2]
print(newdate)

star_search_index=['star-live', 'in-focus', 'literature', 'law-our-right', 'country','newspaper']
url = 'https://www.thedailystar.net/' + star_search_index[0]

print(url)