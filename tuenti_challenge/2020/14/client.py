import telnetlib
#PREPARE {<positive_int>,9} -> <dest>
tn = telnetlib.Telnet("52.49.91.111","2092")
first = 0
proposal_id = 100
it = 0
secret_owner = None
servers = None
my_servers =set(['9'])
output = tn.read_until(b"\n").decode("utf-8")

while True:
    if "SERVER ID" in output:
        server_id = output[output.find("SERVER ID: ")+len("SERVER ID: "):]
        server_id = server_id[:server_id.find("\n")]
        print(server_id)
        server_file = open("servers.txt","a")
        server_file.write(server_id+"\n")
        server_file.close()
        
    if "secret_owner: " in output:
        secret_owner = output[output.rfind("secret_owner: ") + len("secret_owner: "):]
        secret_owner = int(secret_owner[:secret_owner.find("}")])
    if "servers: " in output:
        servers = output[output.rfind("servers: ") + len("servers: "):]
        servers = servers[:servers.find("],")+1]
        server_list = servers.strip("[").strip("]").split(",")
        #servers = servers.strip("[").strip("]").split(",")
    
    #current_servers = open("current_servers.txt","r+")
    output = tn.read_until(b"\n").decode("utf-8")
    print(output)
    if servers is not None:

        accept = "ACCEPT {id: {10,"+str(server_id)+"}, value: {servers: "+servers+", secret_owner: 9}} -> "+str(server_id)
        tn.write(accept.encode('ascii') +b"\n")
        print("Sending ACCEPT")
