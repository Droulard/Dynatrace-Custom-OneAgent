import json, os

# Global Variables
OneAgentPlaybook="./agent_playbooks/SelfHealthOneAgent.yaml"
host_config="./test_configs/self_health_host_config.json"
optional_metadata = ["HOST_DCUID"]

def create_attribute_str(attribute_type, attribute_dict, attribute_str):
	"""
	Purpose: Parse the metadata or tags
	"""
	attribute_str= "\"{}\":{{".format(attribute_type)
	for key in attribute_dict:
		if(key in optional_metadata): 
			pass
		elif(key != list(attribute_dict)[-1]):
			attribute_str += "\"{}\":\"{}\",".format(key, attribute_dict[key])
		else:
			attribute_str+="\"{}\":\"{}\"}}".format(key, attribute_dict[key])
	
	return attribute_str

def create_opt_metadata_str(metadata_dict, metadata_str):
	for key in optional_metadata:
		if(key in metadata_dict and len(metadata_dict[key]) >0):
			metadata_str+= " ,\"{}\":\"{}\",".format(key, metadata_dict[key])
	
	return metadata_str


def create_input_vars(host_config):
	"""
	Purpose: Open the host information file and parse required data
	"""
	# Obtain data from the json file 
	with open('./' + host_config) as f:
	    host_info = json.load(f)

	input_str = "\'{"	

	input_str+= create_attribute_str("metadata", host_info["metadata"], input_str)

	input_str+= "," + create_attribute_str("tags", host_info['tags'], input_str)
	
	if ("HOST_GROUP" in host_info):
		input_str += ",\"{}\":\"{}\"".format("HOST_GROUP", host_info["HOST_GROUP"])
	
	input_str += "}\'"
	
	return input_str

def call_playbook(input_str):
	"""
	Purpose: Call the OneAgent playbook on the created input string
	"""
	command = "ansible-playbook {}  --extra-vars  {}".format( OneAgentPlaybook, input_str)
	os.system(command) 
	
if __name__ == "__main__":
	metadata = create_input_vars(host_config)
	call_playbook(metadata)
