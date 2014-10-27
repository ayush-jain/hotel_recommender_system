from math import sqrt
info={}
def readFile():
	
	#name of the hotels
	hotels = {}
	info = {}
	count = 0
	c=0
	file= open("Collaborativeinput.txt")
	line=file.readline()
	while line != "":
		user=line.split()[0]
		#if user=="END":
			#print "info"
			#break
		hotel=line.split()[1]
		#print hotel
		rating=line.split()[4]
		#print rating
		if float(rating) > 0.0:
			info.setdefault(user,{})
			info[user][hotel] = float(rating)
			c+=1
		
		line=file.readline()
	#print info
	#print c
	return info




#Returns a distance-based similarity score for user1 and user2

def distance_Similarity(info, user1, user2):
	#Get the list of shared_hotels
	si = {}
	for item in info[user1]:
		if item in info[user2]:
			si[item] = 1

	#if they have no rating in common, return 0
	if len(si) == 0: 
		return 0

	#Add up the squares of all differences
	sum_of_squares = sum([pow(info[user1][item]-info[user2][item],2) for item in info[user1] if item in info[user2]])

	return 1 / (1 + sum_of_squares)


#Returns the Pearson correlation coefficient for u1 and u2 
def similarity_pearson(info,u1,u2):
	#Get the list of mutually rated items
	si = {}
	for item in info[u1]:
		if item in info[u2]: 
			si[item] = 1

	#if they are no rating in common, return 0
	if len(si) == 0:
		return 0

	#sum calculations
	n = len(si)

	#sum of all preferences
	sum1 = sum([info[u1][it] for it in si])
	sum2 = sum([info[u2][it] for it in si])

	#Sum of the squares
	sum1Sq = sum([pow(info[u1][it],2) for it in si])
	sum2Sq = sum([pow(info[u2][it],2) for it in si])

	#Sum of the products
	pSum = sum([info[u1][it] * info[u2][it] for it in si])

	#Calculate r (Pearson score)
	num = pSum - (sum1 * sum2/n)
	den = sqrt((sum1Sq - pow(sum1,2)/n) * (sum2Sq - pow(sum2,2)/n))
	if den == 0:
		return 0

	r = num/den

	return r

#Returns the best matches for user from the info dictionary

def topMatches(info,user,n=5,similarity=similarity_pearson):
	scores = [(distance_Similarity(info,user,other),other) for other in info if other != user]
	scores.sort()
	scores.reverse()
	return scores[0:n]


#Gets recommendations for a user by using a weighted average
#of every other user's rankings

def getRecommendations(info,user,similarity=similarity_pearson):
	totals = {}
	similarity_Sums = {}

	for other in info:
		#don't compare user to himself
		if other == user:
			continue
		sim = distance_Similarity(info,user,other)

		#ignore scores of zero or lower
		if sim <= 0: 
			continue
		for item in info[other]:
			#only score hotels he hasent been yet
			if item not in info[user] or info[user][item] == 0:
				#Similarity * score
				totals.setdefault(item,0)
				totals[item] += info[other][item] * sim
				#Sum of similarities
				similarity_Sums.setdefault(item,0)
				similarity_Sums[item] += sim

	#Create the normalized list
	rankings = [(total/similarity_Sums[item],item) for item,total in totals.items()]

	#Return the sorted list
	rankings.sort()
	rankings.reverse()
	return rankings


#Function to transform user, item - > Item, user
def transforminfo(info):
	results = {}
	for user in info:
		for item in info[user]:
			results.setdefault(item,{})

			#Flip item and user
			results[item][user] = info[user][item]

	return results





#Create a dictionary of items showing which other items they are most similar to.

def calculateSimilarItems(info,n=10):
	result = {}
	#Invert the preference matrix to be item-centric
	iteminfo = transforminfo(info)
	c=0
	for item in iteminfo:
		
		c+=1
		if c%100==0:
			print "%d / %d" % (c, len(iteminfo))
		#Find the most similar items to this one
		scores = topMatches(iteminfo,item,n=n,similarity=distance_Similarity)
		result[item] = scores
	return result

def getRecommendedItems(info, itemMatch, user):
	userRatings = info[user]
	scores = {}
	totalSim = {}

	#loop over items rated by this user
	for (item, rating) in userRatings.items():

		#Loop over items similar to this one
		for (similarity, item2) in itemMatch[item]:

			#Ignore if this user has already rated this item
			if item2 in userRatings:
				continue
			#Weighted sum of rating times similarity
			scores.setdefault(item2,0)
			scores[item2] += similarity * rating
			#Sum of all the similarities
			totalSim.setdefault(item2,0)
			totalSim[item2]+=similarity

	#Divide each total score by total weighting to get an average
	rankings = [(score/totalSim[item],item) for item,score in scores.items()]

	#Return the rankings from highest to lowest
	rankings.sort()
	rankings.reverse()
	return rankings

def get_collab(t,n):
	li=[]
	info=readFile()
	#print info['2']
	#d1=distance_Similarity(info,'1','2')
	#pk=similarity_pearson(info,'1', '2')
	#sc=topMatches(info,t,n=5,similarity=pk)
	rank1=getRecommendations(info,t)
	#result1=transforminfo(info)
	result2=calculateSimilarItems(info,n=10)
	rank2=getRecommendedItems(info,result2,t)
	li.append(rank1[0:n])
	li.append(rank2[0:n])
	#print li[0]
	#print "\n"
	#print li[1]
	return li

#get_collab('3',10)