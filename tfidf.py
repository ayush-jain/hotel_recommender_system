from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
from sklearn.feature_extraction import text
from sklearn import decomposition
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.svm import LinearSVC
from sklearn.neighbors import NearestCentroid
import numpy
import processing

#train_set = ["Bel Aire West We pre paid bill Hotels charge 377 55 AND incorrectly charged 136 25 stay Bel Aire West Hotel advertised 4 Star hotel gourmet meal King size bed However upon arrival absolute opposite true We given room full size bed hard rock NO room service three day fresh bed linen still long black hair stuck unwashed comforter last guest fresh towel trash picked There coffeemaker coffee In room fridge microwave however plate silverware plastic ware There NO gourmet meal They served velveeta cheese omelette ham Thanksgiving dinner tough leather The heater work properly took serveral hour room heat We told could get money back pre paid Hotels And impossible find another hotel Thanksgiving weekend knew forced stay Upon going manager Cliff Singleton response laugh argue At first tried claim never stayed hotel When I finally able reach describe horrible experience Mr Singleton continued laugh beligerent argue responsible correcting 4 Star rating hotel Hotels com responsible changing rating It seemed used screaming customer way screaming Then December 1 2003 long checked Thanksgiving weekend Mr Singleton charged u 136 25 claiming show hotel But three horrible day I called bank let know I double billed already pre paid Hotels I fill complaint form Meanwhile Mr Singleton allowed take 513 80 account legally this place is a fraud and a nightmare","Nice trendy hotel location bad I stayed hotel one night As fairly new place taxi driver know want drive Once I eventually arrived hotel I pleasantly surprised decor lobby ground floor area It stylish modern I found reception staff geeting Aloha bit place I guess briefed say keep coroporate image As I Starwood Preferred Guest member I given small gift upon check It couple fridge magnet gift box nevertheless nice gesture My room nice roomy tea coffee facility room get two complimentary bottle water plus toiletry bliss The location great It last metro stop need take taxi planning going see historic site Beijing ok I chose breakfast hotel really tasty good selection dish There couple computer use communal area well pool table There also small swimming pool gym area I would definitely stay hotel I plan travel central Beijing take long time The location ok plan lot shopping big shopping centre minute away hotel plenty eating option around including restaurant serve dog meat","clean room good location poor service check friend arrived different country different time greeted lousy way bellboy help luggage doorman open door receptionist took 5 minute greet u smile despite guest lobby sum pleasant room 2 bedroom suite spacious comfy basic amenity bathroom spacious separate bathtub shower area equipped l occitaine toiletry provide u new one even though finished ask receptionist concierge TWICE getting toiletry shower washing machine brilliant 4 u clever enough work wash dry 4 day Ended laundry hand location central within walking distance train station food place slight difficulty getting taxi though 7eleven round corner starbucks ground floor breakfast small good spread standard egg station fruit bread local congee hot food massage spa massage Chinese pedicure pedicurist man told u maggie cheung went massage ago quality massage pedicure average","A hidden gem We stayed hotel 4 night start holiday 3 night returning UK We chose hotel change main chain hotel Beijing stayed previous visit This lovely hotel within reasonable walking distance hutongs lake Houhai amp Quanhai The metro line short walk hotel taxi cheap plentiful main road near hotel Despite busy part Beijing hotel exceptionally quite peaceful We suite ground floor room 407 The bed giantic Chinese bed quite hard The pillow best pillow I ever slept linen spotlessly clean room The lounge room furntiure classical Chinese carved wood gorgeous look comfortable sit We computer room free internet ace bonus The room bathroom spotless Due position room lot natural light Breakfast included deal ok The main problem food hot fact somtimes even warm That said good variety staff helpful friendly All staff helpful would highly recommend hotel anyone doesn wish stay tall concrete block every room","Good overall service Just came back week hotel The Al Manar hotel apartment part ABC group located 10 minute drive Dubai international Airport cost around 40 dirham taxi 7 00 We big room including kitchen area consists frige freezer washing machine microwave toaster kettle electric hob You also get basic cuttlery fridge mini bar Non Alcoholic drink It also secure safe nice table chair ironing board iron important flat screen TV The hotel ten minute taxi drive Al mamzar beach park cost around 14 dirham 2 50 entry fee park five dirham 0 90p There pool area place eat male female changing area lovely beach The gold spice souk market far away like kind thing I would recommend going Wild Wadi Water park great fun adult kid get great picture Burj Al Arab We went bed breakfast The breakfast best ve holiday however worst The downside fantastic view room construction site next door however hardly noticed spent day sight seeing Noise cannot notice window fully double glazed The staff quite friendly always willing help There small pool rooftop sun lounger shower area toilet important tan Location wise ok however decide travel Jumeirah end cost taxi around 60 dirham 10 way venture futher afield There partially completed dubai metro un manned automatic train Like DLR London get around town running Jebal Ali Rashidya called red line started 7 week ago However hotel need get taxi Deira city centre station 10 min away Its modern clean average single trip costing 4 5 dirham le 1 00 You buy silver card 6 dirham top go A bit like oyster card London underground way cheaper The green line completed mid 2010 The thing must get right compartment woman child carriage others mixed Perfect want go emirate mall There good place eat nearby hotel serving western indian food I quite enjoyed iranian chicken sandwich made fresh bread accross road Drinks cheap stock need due heat I would recommend hotel anyone average budget ","Not Burj Al Arab safe centrally located hotel suitable budget minded traveller I single female traveler stopped Dubai three night way Rwanda Being alone first trip Dubai I required economical hotel secure area easy access historical sight I researched several hotel Trip Advisor settled Admiral Plaza I read review complaining establishment always people hard please I nothing compliment staff service The front desk staff went way help The complimentary shuttle I ordered 7 00 m right time take airport The price including breakfast buffet reasonable around 270 Cad total stay The breakfast wasn fancy certainly lot variety hot cold food available The waiter continually cleared table replenished dish My room clean quiet I enjoy exploring new area foot found Admiral Plaza great location The abras nearby wishing cross creek visit Gold Spice Souks I would highly recommend nearby Heritage House adjacent school On Burj side Museum provides interesting cool respite heat 40 degree June The bus terminal nearby want visit Burj Al Arab Mall Emirates I also took Taxi Burj Al Arab Palm Atlantis In brief I enjoyable stopover Dubai I would certainly stay The Admiral Plaza future visit","Awful noisy felt unsafe Don confuse Americana 5 Inn 4244 N Las Vegas Blvd The red blue door stair agains white building good cute kitsch kind way thing place I think partner booked must read review Americana 5 Tripadvisor As drove road along side motel first thing I noticed room middle second storey boarded Then I noticed fire That bode well I thought hey thing happen kept open mind The room smell unlike reviewer However late November I know would like summer The electrical socket outlet hole wall big ie dangerous looking gap The toilet seat lid nasty cheap soft plastic torn several place There microwave fridge however microwave television wall bracket door could opened I intended use fridge incredibly noisy So much I trouble getting sleep woke 4am It louder road noise loud The door additional lock quite flimsy Anyone could broken quite easily There gap around door let daylight draught No breakfast I wouldn wanted Don stay As someone else daid I d almost rather sleep car Before arrived booked one night via web considered staying extra night Vegas We didn bother No wifi","Best bang buck If go expecting brand new top line furniture bellboy carry luggage re disapointment But go open mind knowing 2 star hotel look like look like disapointments The hotel large room The pool pretty small clean time There 2 security guard walking around property 24 hour day There good size casino 5 restaurant option including daily breakfast lunch dinner buffet The hotel 10 minute drive downtown 15 minute drive strip The room clean everyday got back My wife I impressed service room price definetely staying next time around When wife I travel thing use room sleep store luggage rest time exploring If sound like hotel disapoint","good location average hotel Just thought give update hotel stayed 7th nov night seeing top gear live show close earl court really good hotel nice overall good reception area lounge nicely decorated The room stayed 2 double bed basement couple stair go room tidy clean bed sheet mark tv bad reception good kept cutting skippin back sky3 lol bathroom tiny everything close sink toliet shower shower alrite though noise coming chair table moving upstairs around 630am onwards wall thin hear peolple next door Otherwise average hotel","solid rock 22 Jermyn always favourite You cannot beat location small private hotel central London I stayed ten year ago husband en route Athens I returned suite find nothing changed even decor upgraded television set While familiarity comforting traveling alone could said 22 could good spiff paint job new carpet etc The best part 22 however staff They cannot enough help I required bit assistance OUTSTANDING every way They always default choice You might get fancier lobby trendier room won get better service Try Veraswamy Indian dinner around corner go Fortnum Mason choose picnic enjoy room"] #Documents
#test_set = ["Stunning My spouse I live New Delhi stayed Aman celebrate anniversary I agree previous reviewer lived Delhi life I say confidence far best hotel city The highlight room We basic one bedroom suite absolutely gorgeous I say even though I slightly preferred room Amanbagh Judging Amans picture I d say probably one nicest looking room repertoire The plunge pool area daybed large balcony especially gorgeous light streaming jharokas The service good massage room well done The head assistant manager amazingly helpful helped wife set surprise showed room wanted see could pick one best view many little thing On downside lobby area well area unimpressive food ho hum tailored Indian palate choice vegetarian food sparse The hookah made u terrible steer clear They claim mughal architecture aside one two design feature complaining The pool nice nearly good Amans Also I would suggest going September properly open want avail following service hammam steam sauna one told aforehand unavailability We Sunday church nearby huge procession going like 4 morning They sang loud song atrocious boot really ruined night I couldn sleep 3 hour So check I know Sunday morning thing occasion Despite shortcoming hopefully temporary room amazing I justify taking star","Great location This great location term shopping seeing attractive part downtown Chicago The hotel relatively inexpensive part town overall quality There aspect place drawback noted prior review First place hampered inadequate elevator Even though five find waiting fair amount including getting lobby street level Second room small I corner room 11th floor measured roughly 9 x 11 leaving little room beyond taken bed desk There virtually drawer space closet bathroom also tight For one person acceptable European sailboat kind way The room nicely done fairly good quality bedding finish In talking guest I got impression room somewhat larger though expansive As aspect breakfast anemic buffet priced 15 00 The hotel large workout area top floor Overall I think Allerton fairly good option especially price","excellent convenient amenable staff I used recomened Amber Inn least past 5 year maybe longer My organization co sponsers 2 event year end august early december People come country even canada france complaint stayed I always let people know room service meal brought want may opt costly downtown hotel Most eaten restaurant whose management changed thru year I yet recieve complaint Ms Smith staff always resourceful courteous professional Extremely patient I added canceled last minute never rude like I m bothering job Unfortunately never enough room event occur many one going city People place hotel accused showing favoritism assigning Amber Inn could get room wait late book especially people stay Amber brag good treated courtesy employee breakfast good for them We staying Amber Inn end month Hats Ms Smith demand nothing le complete customer satisfaction staff life expectation","Great value money I stayed one night Al Bustan Centre Residence transit Dubai Positives Price At around US 75 hotel absolute bargain Dubai city traditionally expensive hotel Friendly efficient staff While I dealt staff check check professional courteous efficient My room key waiting I arrived Check check took minute Room I booked studio room 3255 pleasantly surprised The room large around 450 sq foot 43 sq meteres decent size The bathroom also decent size good bath shower basic toiletry I use kitchen facility noted plenty pot pan glass large fridge microwave Good curtain blocked intense morning sun light Air conditioning good important city hot Dubai Furniture room amenity appeared modern good condition Sound proofing room excellent 24 hour reception I arrived around midnight slightly worried given cheap price hotel would closed There need worry plenty staff available lobby front desk Negatives Traffic While really hotel fault traffic hotel airport horrendous It took around 80 minute reach airport I would missed flight luckily I watch accidentally set different time zone one hour behind I intended leave hotel 10am inadvertently left 9am However trip airport hotel via taxi around midnight took 10 minute Location Unless looking transit hotel spend one night location hotel little going It long way Dubai traffic bad end spending time taxi Long walk bag The room corridor extremely long walk reception room least room I probably half mile long If lot luggage consider asking room near elevator Overall I surprised read negative view hotel Trip Advisor While hotel far best Dubai offer represents fantastic value money It big downfall location inconvenient everywhere except airport I would definitely stay transiting Dubai"] #Query

#test_set1=["Nice trendy hotel location bad I stayed hotel one night As fairly new place taxi driver know want drive Once I eventually arrived hotel I pleasantly surprised decor lobby ground floor area It stylish modern I found reception staff geeting Aloha bit place I guess briefed say keep coroporate image As I Starwood Preferred Guest member I given small gift upon check It couple fridge magnet gift box nevertheless nice gesture My room nice roomy tea coffee facility room get two complimentary bottle water plus toiletry bliss The location great It last metro stop need take taxi planning going see historic site Beijing ok I chose breakfast hotel really tasty good selection dish There couple computer use communal area well pool table There also small swimming pool gym area I would definitely stay hotel I plan travel central Beijing take long time The location ok plan lot shopping big shopping centre minute away hotel plenty eating option around including restaurant serve dog meat"]


def read_hotels(city,dict):
	#print len(train_set)
	if(city=='beijing'):
		f=open('hotel2.txt')
	hotels=[]
	inx=0
	location=f.readline().strip('\n').split(':')[1]
	line=f.readline().split(':')
	name=line[1].strip('\n')
	#print line
	line=f.readline().strip('\n').split(':')[1]
	while(line!=''):
		tset=[]
		for i in range(0,5):
			#print line
			tset.append(line)
			if(i==4):
				break
			line=f.readline().strip('\n').split(':')[1]
		line=f.readline()
		hotels.append(tset)
		dict[inx]=(name,location)
		inx=inx+1
		if(line==''):
			break
		#print "=====Hello",line	
		line=f.readline()	
		name=line.split(':')[1].strip('\n')
		line=f.readline().strip('\n').split(':')[1]
		#print line
		#print name
		#if(name==[]):
		#	break
		#else:
		#	name=name[1]		
		#line=f.readline().split(':')		
	
	#print hotels
	return hotels


def calculate_Topic(arr,t_l):
	count={}
	inx=0
	for w in t_l:
		count[inx]=0
		for i in w:
			if(arr[i]!=0):
				count[inx]=count[inx]+1
				#print inx,arr[i]
		inx=inx+1
	#print count
	inverse = [(value, key) for key, value in count.items()]
	return max(inverse)[1]		


def calculate_target(t1,t2,t3):
	sc=[]
	
	for i in range(0,len(t1)):
		a=[0]*5
		a[t1[i]]=a[t1[i]]+1
		a[t2[i]]=a[t2[i]]+1
		a[t3[i]]=a[t3[i]]+1
		m=numpy.array(a).argsort()[::-1]
		sc.append(m[0])
	return sc

def calculate_sentiment(str,positive,negative):
	p=0
	n=0
	for i in str.split():
		if i in positive:
			p=p+1
			#print i
		if i in negative:
			n=n+1
			#print "hello------"
			#print i
	if(n==0):
		p=p+1
		n=n+1
		
	return p/n
	
#print calculate_sentiment(test_set1[0])

def calculate_result(t_s,t_c,t_t,positive,negative,train_set):
	result=0
	for i in range(0,len(t_s)):
		c=t_c[t_t[i]]
		c=float(c)/len(train_set) 
		d=calculate_sentiment(t_s[i],positive,negative)
		#print d
		result=result+(c*d)	
	return result


def get_results(city,no):
	processing.preprocessing()
	pre=open('preprocess1.txt')
	train_set=[]
	line=pre.readline()
	while(line!=''):
		train_set.append(line)
		#print line
		line=pre.readline()
	#print train_set	
	pos=open('positive-words.txt')
	neg=open('negative-words.txt')
	positive=[]
	negative=[]
	for i in pos.read().split():
		positive.append(i)	

	for j in neg.read().split():
		negative.append(j)

	stopWords = stopwords.words('english')
	vectorizer = CountVectorizer(stop_words = stopWords)
	transformer = TfidfTransformer()

	#train_set=get_traindata()
	

	#l=[]
	#l.append(test_set)
	#l.append(test_set1)

	#trainVectorizerArray = vectorizer.fit_transform(train_set).toarray()
	#print vectorizer.get_feature_names()
	#testVectorizerArray = vectorizer.transform(test_set).toarray()
	#testVectorizerArray1 = vectorizer.transform(l[1]).toarray()
	#print 'Fit Vectorizer to train set', trainVectorizerArray
	#print 'Transform Vectorizer to test set', testVectorizerArray
	#print testVectorizerArray1[0]

	#transformer.fit(trainVectorizerArray)
	v= vectorizer.fit_transform(train_set)
	#print v.toarray()
	tfidf= transformer.fit_transform(v)
	#transformer.fit(testVectorizerArray)

	#tfidf = transformer.transform(trainVectorizerArray)
	#print tfidf.todense()

	#print("done in %0.3fs." % (time() - t0))
	#print nmf.components_
	# Inverse the vectorizer vocabulary to be able
	feature_names = vectorizer.get_feature_names()
	#print (feature_names)
	#if 'area' in feature_names: 
	print (feature_names)

	print ("\n")
	#-------

	nmf = decomposition.NMF(n_components=3, init='random',random_state=0).fit(tfidf.todense())
	topic_list=[]
	l= int(len(feature_names)/5)
	#print l
	for topic_idx, topic in enumerate(nmf.components_):
		topic_list.append(topic.argsort()[:-l-1:-1])
    
    #print("Topic #%d:" % topic_idx)
    #print (topic)
	#print "Hello----"
	#print topic_list


	train_target=[]	
	for arr in v.toarray():
		train_target.append(calculate_Topic(arr,topic_list))
	#print train_target
	#clf = MultinomialNB()
	#clf2= LinearSVC()
	#clf1=NearestCentroid()
	#clf.fit(tfidf.todense(),train_target)
	#clf1.fit(tfidf.todense(),train_target)
	#clf2.fit(tfidf.todense(),train_target)
	#print (clf.predict(X_test))
	#print (clf1.predict(X_test))
	#print (clf2.predict(X_test))
	#print "Hello"
	ch2 = SelectKBest(chi2, k=l*2)
	X_train = ch2.fit_transform(tfidf.todense(), train_target)

	cs= ch2.scores_.argsort()[::-1]
	cs_featurenames=[]
	cs=cs[:l*2]
	for x in cs:
		cs_featurenames.append(feature_names[x])

	print (cs_featurenames)
	print "\n"

	nmf1 = decomposition.NMF(n_components=3, init='random',random_state=0).fit(X_train)
	topic_list=[]
	l= int(len(feature_names)/5)
	#print l
	for topic_idx, topic in enumerate(nmf1.components_):
		z=topic.argsort()[:-l-1:-1]
		topic_list.append(z)
		print("Topic #%d:---------------------------------------" % topic_idx)
		for y in z:
			print cs_featurenames[y]
    #print (topic)
	#print "Hello----"    
	#print topic_list
	train_target=[]	
	for arr in X_train:
		train_target.append(calculate_Topic(arr,topic_list))

	#---------
	#print "hello"
	#print train_target
	#print ch2.get_feature_names()
	#print X_train
	#print train_target
	#print "=--------------"
	#print ta
	#print X_test
	train_count=[0]*4
	#print train_target
	for x in train_target:
		train_count[x]=train_count[x]+1
	#print "hello"
	#print train_count	


	clf = MultinomialNB()
	clf2= LinearSVC()
	clf1=NearestCentroid()
	clf.fit(X_train,train_target)
	clf1.fit(X_train,train_target)
	clf2.fit(X_train,train_target)	
	dic={}
	hotels=read_hotels(city,dic)
	temp=[]
	for each in hotels:
		temp.append(calculate(vectorizer,transformer,train_count,ch2,each,clf,clf1,clf2,positive,negative,train_set))
	res=[]	
	temp1=numpy.array(temp).argsort()[::-1]
	#print temp1
	print "Top %d recommendations are as follows[in the FORMAT Index,(Hotel name,Location),Score]:\n" %no

	for g in temp1[:no]:
		print g,dic[g],temp[g]
		res.append(dic[g])

	return res	

def calculate(vectorizer,transformer,train_count,ch2,test_set,clf,clf1,clf2,positive,negative,train_set):

	ta = vectorizer.transform(test_set).toarray()
	X_test=transformer.transform(ta).todense()
	X_test = ch2.transform(X_test)
	test_target1= clf.predict(X_test)
	test_target2= clf1.predict(X_test)
	test_target3= clf2.predict(X_test)

	#print test_target1, test_target2, test_target3

	test_target= calculate_target(test_target1,test_target2,test_target3)
	
	

	#print (positive)
	#print ("----")
	#print (negative)
		
	#print test_set
	r=calculate_result(test_set,train_count,test_target,positive,negative,train_set)
	return r

#get_results('beijing',3)