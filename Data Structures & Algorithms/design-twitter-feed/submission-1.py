class Twitter:

    '''
    users: [following], [tweets]

    tweets: time, id
     
    '''


    def __init__(self):
        self.time = 0
        self.users = {}

    def addUser(self, userId):
        if userId not in self.users:
            self.users[userId] = [{userId}, []]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.addUser(userId)
        self.time += 1
        self.users[userId][1].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.addUser(userId)
        heap = []

        for followeeId in self.users[userId][0]:
            for tweet in self.users[followeeId][1]:
                if len(heap) < 10:
                    heapq.heappush(heap, tweet)
                elif tweet[0] > heap[0][0]:
                    heapq.heappushpop(heap, tweet)

        return [tweetId for time, tweetId in sorted(heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.addUser(followerId)
        self.addUser(followeeId)
        self.users[followerId][0].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.addUser(followerId)

        if followerId == followeeId:
            return

        self.users[followerId][0].discard(followeeId)