class User:
    def __init__(self, userId):
        self.userId = userId
        self.tweets = []
        self.followers = set()


class Twitter:
    
    def __init__(self):
        self.users = {}
        self.timestamp = 0
        
    def checkUser(self, userId):
        if userId not in self.users:
            self.users[userId] = User(userId)
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.checkUser(userId)
        
        user = self.users[userId]
        user.tweets.append((self.timestamp, tweetId))
        self.timestamp += 1
    
    def addTweets(self, userId, maxHeap):
        
        user = self.users[userId]
        tweets = user.tweets
        
        n = len(tweets)
        
        if n > 0:
            tweet_time, tweetId = tweets[n - 1]
            heapq.heappush(maxHeap, (-tweet_time, tweetId, n - 1, tweets) )
        
    
    def getNewsFeed(self, userId: int) -> List[int]:
        self.checkUser(userId)
        recent_tweets = []
        
        maxHeap = []
        heapq.heapify(maxHeap)
        
        self.addTweets(userId, maxHeap)
        
        for followerId in self.users[userId].followers:
            self.addTweets(followerId, maxHeap)
            
        
        while len(recent_tweets) < 10 and len(maxHeap) > 0:
            tweet_time, tweetId, index, tweets = heapq.heappop(maxHeap)
            
            recent_tweets.append(tweetId)
            
            if index - 1 >= 0:
                prev_tweet_time, prev_tweetId = tweets[index - 1]
                heapq.heappush(maxHeap, (-prev_tweet_time, prev_tweetId, index - 1, tweets))
        
        
        return recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        
        self.checkUser(followerId)
        self.checkUser(followeeId)
        
        user = self.users[followerId]
        user.followers.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.checkUser(followerId)
        self.checkUser(followeeId)
        
        user = self.users[followerId]
        user.followers.discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
