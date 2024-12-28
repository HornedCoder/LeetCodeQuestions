'''
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
 '''

class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If key is not Present we make a new empty list for key to store.
        if key not in self.timeMap:
            self.timeMap[key] = []
        #Now we add the timestamp and value pair to the dictionary
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        #If timestamp is smaller than the first timestamp return Null.
        if key not in self.timeMap:
            return ""
        
        #There are 4 base cases

        timeSeries = self.timeMap[key]
        l, r = 0, len(timeSeries)-1
        #1st if timestamp is less than the first timeStamp of series.
        #Return "" in this case
        if timeSeries[0][0] > timestamp:
            return ""
        
        #2nd Case that timestamp exactly matches with most recent timeSeries,
        #3rd case whem timestamp greater than last timeSeries
        if timeSeries[r][0] <= timestamp:
            return timeSeries[r][1]
        

        #4th case if timestamp is between two sorted timeSeries.
        while l < r:
            m = (l+r+1)//2
            if timeSeries[m][0] <= timestamp:
                l = m
            else:
                r = m-1
        return timeSeries[l][1]
            



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
