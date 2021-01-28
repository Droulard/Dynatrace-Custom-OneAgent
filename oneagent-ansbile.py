import json, os

# Global Variables
OneAgentPlaybook="OneAgent.yaml"
host_config="host_config.json"
optional_metadata = ["HOST_DCUID"]

def create_metadata_str(metadata, metadata_str):
	"""
	Purpose: Parse the metadata
	"""
	metadata_str= "\"metadata\":{"
	for key in metadata:
		if(key in optional_metadata): 
			pass
		elif(key != list(metadata)[-1]):
			metadata_str += "\"{}\":\"{}\",".format(key, metadata[key])
		else:
			metadata_str+="\"{}\":\"{}\"}},".format(key, metadata[key])
	for key in optional_metadata:
		if(len(metadata[key]) >0):
			metadata_str+= " \"{}\":\"{}\",".format(key, metadata[key])
	
	return metadata_str


def create_input_vars(host_config):
	"""
	Purpose: Open the host information file and parse required data
	"""
	# Obtain data from the json file 
	with open('./' + host_config) as f:
	    host_info = json.load(f)

	input_str = "\'{"	

	input_str+= create_metadata_str(host_info["metadata"], input_str)
	input_str += "\"{}\":\"{}\"".format("HOST_GROUP", host_info["HOST_GROUP"])
	
	input_str += "}\'"
	
	return input_str

def call_playbook(input_str):
	"""
	Purpose: Call the OneAgent playbook on the created input string
	"""
	command = "ansible-playbook {}  --extra-vars  {}".format( OneAgentPlaybook, input_str)
	os.system(command) 
	# print(command)
	
if __name__ == "__main__":
	metadata = create_input_vars(host_config)
	call_playbook(metadata)
