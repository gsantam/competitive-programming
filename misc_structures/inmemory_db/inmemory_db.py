class InMemoryDB:
    def __init__(self):
        self.db = dict()
    def set(self,key,field,value,timestamp = None, ttl = None):
        if key not in self.db:
            self.db[key] = {}
        self.db[key][field] = (value,timestamp,ttl)
    
    def set_at(self,key,field,value,timestamp):
        self.set(key,field,value,timestamp)

    def set_at_with_ttl(self,key,field,value,timestamp,ttl):
        self.set(key,field,value,timestamp,ttl)

    def exists(self,key,field,timestamp):
        if key in self.db and field in self.db[key]: 
            _,timestamp_val,ttl_val = self.db[key][field]
            if not timestamp or not ttl_val:
                return True
            if  timestamp >= timestamp_val and timestamp<=timestamp_val+ttl_val:
                return True
            #else:
            #    del self.db[field][key]
        return False
    
    def get(self,key,field,timestamp = None):
        if not self.exists(key,field,timestamp):
            return None
        return self.db[key][field][0]
    
    def get_at(self,key,field,timestamp):
        return self.get(key,field,timestamp)
    
    def delete(self,key,field,timestamp = None):
        if not self.exists(key,field,timestamp):
            return False
        del self.db[key][field]
        return True
    
    def delete_at(self,key,field,timestamp):
        return self.delete(key,field,timestamp)
    
    def format_fields_for_scan(self,fields):
        sorted_fields = sorted(list(fields.keys()))
        sorted_fields_values = [field+"("+fields[field][0]+")" for field in sorted_fields] 
        return sorted_fields_values
    
    def get_field_filter(self,key,timestamp):
        fields = self.db[key]
        existed_fields = {field:fields[field] for field in list(fields.keys()) if self.exists(key,field,timestamp)}
        return existed_fields
    
    def scan(self,key,timestamp = None):
        if key not in self.db:
            return []
        existed_fields = self.get_field_filter(key,timestamp)
        return self.format_fields_for_scan(existed_fields)
    
    def scan_at(self,key,timestamp):
        self.scan(key,timestamp)
    
    def scan_by_prefix(self,key,prefix,timestamp = None):
        if key not in self.db:
            return []
        existed_fields = self.get_field_filter(key,timestamp)
        filtered_fields = {field:existed_fields[field] for field in list(existed_fields.keys()) if field.startswith(prefix)}
        return self.format_fields_for_scan(filtered_fields)
    
    def scan_by_prefix_at(self,key,prefix,timestamp):
        self.scan_by_prefix(key,prefix,timestamp)


if __name__ == "__main__":
    print("hola")