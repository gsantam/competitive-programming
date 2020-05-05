import telnetlib
#PREPARE {<positive_int>,9} -> <dest>
tn = telnetlib.Telnet("52.49.91.111","2092")
first = 0
it = 0
secret_owner = None
servers = None
server_list = None
server_file = open("servers.txt","w")
server_file.truncate()
server_file.close()
my_servers = set('9')

while True:
    output = tn.read_until(b"ROUND FINISHED)\n").decode("utf-8")
    print(output)
    output_lines = output.split("\n")
    if it>1:
        if "secret_owner: " in output:
            secret_owner = output[output.rfind("secret_owner: ") + len("secret_owner: "):]
            secret_owner = int(secret_owner[:secret_owner.find("}")])
        if "servers: " in output:
            servers = output[output.rfind("servers: ") + len("servers: "):]
            servers = servers[:servers.find("],")+1]
            servers = servers.strip("[").strip("]").split(",")
            print("servers are: "+str(server_list))
            server_list = servers
            server_file = open("servers.txt")
            change = False
            
            for server_to_include in server_file.readlines():
                server_to_include = server_to_include.strip()
                if server_to_include not in server_list:
                    change = True
                    my_servers.add(server_to_include)
                    print("trying to include server: "+server_to_include)
                    server_list.append(server_to_include)
                    break
            if not change:
                for server in server_list:
                    if server not in my_servers:
                        print("trying to remove server: "+server)
                        server_list.remove(server)
                        break
            servers = "["+",".join([x for x in server_list]) + "]"  
    it+=1    
    
    if it>=3:
        servers_prepare = ["PREPARE {10,9} -> "+str(server_id) for server_id in server_list]
        for server_prepare in servers_prepare:
            tn.write(server_prepare.encode('ascii') +b"\n")
        servers_accept = ["ACCEPT {id: {10,9}, value: {servers: "+servers+", secret_owner: "+str(secret_owner)+"}} -> "+str(server_id) for server_id in server_list if server_id!='9']
        total_my_servers = 0
        for server in server_list:
            if server in my_servers:
                total_my_servers+=1
        if it%10==0:
            print("Trying to hack")
            servers_accept = ["ACCEPT {id: {10,9}, value: {servers: "+servers+", secret_owner: 9}} -> "+str(server_id) for server_id in server_list]

        for server_accept in servers_accept:
            tn.write(server_accept.encode('ascii') +b"\n") 
    
