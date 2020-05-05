from collections import deque


class Solution:
    
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = deque()
        queue.append((id,0))
        seen = set()
        watchedVideos_ = {}
        while len(queue)>0:
            element  = queue.popleft()
            element_id = element[0]
            element_level = element[1]
            if element_level<=level and element_id not in seen:
                seen.add(element_id)
                if element_level == level:
                    for video in watchedVideos[element_id]:
                        if video not in watchedVideos_:
                            watchedVideos_[video] = 0 
                        watchedVideos_[video]+=1
                        
                for friend_id in friends[element_id]:
                    queue.append((friend_id,element_level+1))
        sorted_videos  = sorted([(watchedVideos_[video],video) for video in watchedVideos_])
        return [x[1] for x in sorted_videos]
            
                        
        
        
        
