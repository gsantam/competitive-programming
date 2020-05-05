class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        ended_functions = [0 for i in range(n)]
        running = None
        exclusive_time = [0 for i in range(n)]
        for log in logs:
            log  = log.split(":")
            f_id = int(log[0])
            type_ = log[1]
            timestamp = int(log[2])
            
            if type_ == "start":
                stack.append(f_id)
                if running is not None:  
                    exclusive_time[running]+=(timestamp - prev_timestamp) 
                prev_timestamp = timestamp 
                    
                
            if type_ == "end":
                exclusive_time[running]+=(timestamp - prev_timestamp)  +1
                if len(stack)>0:
                    stack.pop()
                if len(stack)>0:
                    f_id = stack[len(stack)-1]
                    
                prev_timestamp = timestamp  +1
                   
            running = f_id
            
        return [time for time in exclusive_time]
        
