class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        '''
          l                 r
        [10, A] [20, A] [30, B] [40, B] [50, C]
        
        sort it based on time
        
        
        '''
        def fillInvalidTransactions(arr, ans):
            n = len(arr)
            
            for i in range(n):
                name1, time1, amount1, city1 = arr[i].split(",")
                
                if int(amount1) > 1000:
                    ans.append(arr[i])
                    continue
                
                for j in range(n):
                    name2, time2, amount2, city2 = arr[j].split(",")
                    
                    if city2 != city1 and abs(int(time1) - int(time2)) <= 60:
                        
                        ans.append(arr[i])
                        break
                        
        
        invalidTransactions = []
        hashmap = defaultdict(list)
        n = len(transactions)
        
        for i in range(n):
            transaction = transactions[i]
            name, time, amount, city = transaction.split(",")
            
            
            hashmap[name].append(transaction)
        
        
        for name in hashmap.keys():
            fillInvalidTransactions(hashmap[name], invalidTransactions)
            
        
        return invalidTransactions
        
        
        
