Dynatrace-Custom-OneAgent
=========================

<strong>Purpose: </strong> Automate the process of downloading and configuring the Dynatrace OneAgent, this is an automated approach that offers setting all tags/metadata for a Dynatrace tenant with a simple json file.
<strong> To install the OneAgent you must have run the python script with root privileges </strong>


Requirements
------------
+ Dynatrace Tenant
+ PaaS Token 
+ Network Zone (optional)

How Does It Work?
----------------
1. Use the template host config file provided to create your own host config
2. Edit the Python script to use the proper OneAgent yaml file based off of your needs
3. The Python script will read your JSON file and create the proper input string for the Ansible playbook
4. The Python script will then call the Ansible playbook which will then download and install a OneAgent with the proper configurations

Example Configuration file
----------------
```json
{
    "HOST_GROUP":"HOST GROUP",
    "metadata": {
        "HOST_PROVIDER":"HOST_PROVIDER",
        "HOST_REGION":"HOST_REGION", 
        "HOST_PURPOSE":"HOST_PURPOSE", 
        "HOST_APPNAME":"HOST_APPNAME"
    },

    "tags":{
        "HOST_NAME":"HOST-NAME",
        "HOST_PROVIDER":"HOST_PROVIDER", 
        "HOST_PURPOSE":"HOST_PURPOSE"   
    }
}
```

License
-------

BSD

Author Information
------------------

Kyle.Droulard@dynatrace.com
