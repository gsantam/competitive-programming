class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_dict = dict()
        for trip in trips:
            if trip[1] not in trip_dict:
                trip_dict[trip[1]] = 0
            trip_dict[trip[1]]+=trip[0]
            if trip[2] not in trip_dict:
                trip_dict[trip[2]] = 0        
            trip_dict[trip[2]]-=trip[0]

        trip_location = sorted(list(trip_dict.keys()))
        total_capacity = capacity
        for location in trip_location:
            total_capacity-=trip_dict[location]
            if total_capacity<0:
                return False
        return True
