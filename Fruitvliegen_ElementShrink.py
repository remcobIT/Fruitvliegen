# The next algorithm is the as the original FindandSwap.
# The only difference is that the sorting begins at the end of the list
# instead of at the begin.
from collections import deque

class Genome(object):
	
	def __init__(self, array, history, swaps, elements, score, swapLengthTotal):
		self.array = array
		self.history = history
		self.swaps = swaps
		self.elements = elements
		self.score = score
		self.swapLengthTotal = swapLengthTotal
		
# initialize variables
melanoStart = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
#melanoStart = [14, 23, 2, 11, 24, 18, 21, 6, 1, 10, 7, 20, 3, 8, 13, 22, 12, 25, 15, 5, 17, 9, 19, 4, 16]
history = []
swaps = 0
score = 0
swapLengthTotal = 0
prQueue = []
prQueueScore = []
archive = dict()

print "\n" + "Start: " + str(melanoStart)

# minimum future swaps
elements = 1
for a in range(len(melanoStart)):
	if a == 24:
		break
	if melanoStart[a] + 1 != melanoStart[a + 1] and melanoStart[a] - 1 != melanoStart[a + 1]:
		elements += 1

score = swaps + elements
print "Score: " + str(score) + "\n"

archive[tuple(melanoStart)] = True
prQueue.append(Genome(melanoStart, history, swaps, elements, score, swapLengthTotal))
prQueueScore.append(score)

# make new objects until one object is fully sorted
while prQueue[0].elements != 1:
	
	# take array with best score so far and put in archive
	melanoBest = prQueue[0]
	myDeque = deque(prQueue)
	myDeque.popleft()
	prQueue = list(myDeque)
	
	scoreBest = prQueueScore[0]
	myScoreDeque = deque(prQueueScore)
	myScoreDeque.popleft()
	prQueueScore = list(myScoreDeque)
			
	print "Array: " + str(melanoBest.array)
	print "History: " + str(melanoBest.history)
	print "Swaps: " + str(melanoBest.swaps)
	print "Elements: " + str(melanoBest.elements)
	print "Score: " + str(melanoBest.score)
	print "Total Swap Length: " + str(melanoBest.swapLengthTotal) + "\n"
	
	melanoTuple = tuple(melanoBest.array)
	historyTuple = tuple(melanoBest.history)
	
	# iterate over all possible swaps
	for i in range(len(melanoBest.array)):
		if i == 24:
			break
		for j in range(len(melanoBest.array)):
			if i + j + 2 > 25:
				break

			melano = list(melanoTuple)
			addToHistory = list(historyTuple)
			addToHistory.append(melanoTuple)
			swaps = melanoBest.swaps
			swapLengthTotal = melanoBest.swapLengthTotal

			# do swap and add to swapLengthTotal and swaps
			swapLengthTotal += len(melano[i:i + j + 2])
			melano[i:i + j + 2] = reversed(melano[i:i + j + 2])
			swaps += 1

			# if not in archive, determine elements of new array
			elements = 1
			for m in range(len(melano)):
				if m == 24:
					break
				if melano[m] + 1 != melano[m + 1] and melano[m] - 1 != melano[m + 1]:
					elements += 1
						
			elementShrink = False
			if elements < melanoBest.elements:
				elementShrink = True
				
			# compare array with archive, if amount of elements shrinked
			inArchive = True
			if elementShrink == True:
				if tuple(melano) not in archive:
					archive[tuple(melano)] = True
					inArchive = False
				
			# if not in archive, put in queue
			if inArchive == False:
				# determine score of new array
				score = swaps + elements

				# make object and put in right place of priority queue
				# if score is bigger than the last in queue, add object to the end
				if len(prQueue) == 0 or score >= prQueue[-1].score:
					prQueueScore.append(score)
					prQueue.append(Genome(melano, addToHistory, swaps, elements, score, swapLengthTotal))
				# else, find the right place in queue and insert
				else:
					placeInQueue = prQueueScore.index(score + 1)
					prQueueScore.insert(placeInQueue, score)
					prQueue.insert(placeInQueue, Genome(melano, addToHistory, swaps, elements, score, swapLengthTotal))

				
print "---------------RESULT---------------"
print "Array: " + str(prQueue[0].array)
print "History: " + str(prQueue[0].history)
print "Swaps: " + str(prQueue[0].swaps)
print "Elements: " + str(prQueue[0].elements)
print "Score: " + str(prQueue[0].score)
print "Total Swap Length: " + str(prQueue[0].swapLengthTotal)