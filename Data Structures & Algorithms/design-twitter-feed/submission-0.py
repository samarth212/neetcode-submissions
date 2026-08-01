class Twitter:

    '''
    users: [following], [tweets]

    tweets: time, id
     
    '''


    def __init__(self):
        self.time = 0
        self.users = {}
        self.tweets = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.users:
            self.users[userId] = [[userId], []]

        self.time +=1

        self.users[userId][1].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:

        if userId not in self.users:
            self.users[userId] = [[userId], []]

        heap = []
        following = self.users[userId][0]
        for user in following:
            tweets = self.users[user][1]
            for tweet in tweets:
                if len(heap) < 10:
                    heapq.heappush(heap, tweet)
                elif tweet[0] > heap[0][0]:
                    heapq.heappushpop(heap, tweet)

        return [tweetId for time, tweetId in sorted(heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = [[followerId], []]

        self.users[followerId][0].append(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = [[followerId], []]
        else: self.users[followerId][0].remove(followeeId)
        
        
