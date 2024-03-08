from typing import  List

    
class AIF:
    def __init__(self, xaif):
        self.xaif = xaif
        self.aif = xaif.get('aif')
        self.nodes = self.aif.get('nodes')
        self.locutions = self.aif.get('locutions')
        self.participants = self.aif.get('participants')
    def is_valid_json_aif(self,):
        if 'nodes' in self.aif  and 'locutions' in self.aif  and 'edges' in self.aif :
            return True
        return False
    def is_json_aif_dialog(self) -> bool:
        ''' check if json_aif is dialog
        '''

        for nodes_entry in self.nodes:					
            if nodes_entry['type'] == "L":
                return True
        return False
    

    def get_next_max_id(self, n_type):
        """
       Takes a list of nodes (edges) and returns the maximum node/edge ID.
        Arguments:
        - nodes/edges (List[Dict]): a list of nodes/edges, where each node is a dictionary containing a node/edge ID
        Returns:
        - (int): the maximum node/edge ID in the list of nodes
        """

        max_id, lef_n_id, right_n_id = 0, 0, ""
        if isinstance(self.nodes[0][n_type],str): # check if the node id is a text or integer
            if "_" in self.nodes[0][n_type]:
                for node in self.nodes:
                    temp_id = node[n_type]
                    if "_" in temp_id:
                        nodeid_parsed = temp_id.split("_") # text node id can involve the character "_"
                        lef_n_id, right_n_id = int(nodeid_parsed[0]), nodeid_parsed[1]
                        if lef_n_id > max_id:
                            max_id = lef_n_id
                return str(int(max_id)+1)+"_"+str(right_n_id)
            else:
                for node in self.nodes:
                    temp_id = int(node[n_type])     
                    if temp_id > max_id:
                        max_id = temp_id   
                return str(max_id+1)

        elif isinstance(self.nodes[0][n_type],int):	
            for node in self.nodes:
                temp_id = node[n_type]     
                if temp_id > max_id:
                    max_id = temp_id   
            return max_id+1
        


    def get_speaker(self, node_id: int) -> str:
        """
        Takes a node ID, a list of locutions, and a list of participants, and returns the name of the participant who spoke the locution with the given node ID, or "None" 
        if the node ID is not found.

        Arguments:
        - node_id (int): the node ID to search for
        - locutions (List[Dict]): a list of locutions, where each locution is a dictionary containing a node ID and a person ID
        - participants (List[Dict]): a list of participants, where each participant is a dictionary containing a participant ID, a first name, and a last name

        Returns:
        - (str): the name of the participant who spoke the locution with the given node ID, or "None" if the node ID is not found
        """

        nodeID_speaker = {}
        # Loop through each locution and extract the person ID and node ID
        for locution in self.locutions:
            personID = locution['personID']
            nodeID = locution['nodeID']
            
            # Loop through each participant and check if their participant ID matches the person ID from the locution
            for participant in self.participants:
                if participant["participantID"] == personID:
                    # If there is a match, add the participant's name to the nodeID_speaker dictionary with the node ID as the key
                    firstname = participant["firstname"]
                    surname = participant["surname"]
                    nodeID_speaker[nodeID] = (firstname+" "+surname,personID)
                    
        # Check if the given node ID is in the nodeID_speaker dictionary and return the corresponding speaker name, or "None" if the node ID is not found
        if node_id in nodeID_speaker:
            return nodeID_speaker[node_id]
        else:
            return ("None None","None")

    def create_entry(self, prediction, index1, index2):

        if prediction == "RA":
            AR_text = "Default Inference"
            AR_type = "RA"
        elif prediction == "CA":	
            AR_text = "Default Conflict"
            AR_type = "CA"
        elif prediction == "MA":	
            AR_text = "Default Rephrase"
        node_id = AIF.get_next_max_id(self.aif['nodes'], 'nodeID')
        edge_id = AIF.get_next_max_id(self.aif['edges'], 'edgeID')
        self.aif['nodes'].append({'text': AR_text, 'type':AR_type,'nodeID': node_id})				
        self.aif['edges'].append({'fromID': index1, 'toID': node_id,'edgeID':edge_id})
        edge_id = AIF.get_next_max_id(self.aif['edges'], 'edgeID')
        self.aif['edges'].append({'fromID': node_id, 'toID': index2,'edgeID':edge_id})

        
    
    def get_i_node_ya_nodes_for_l_node(self, n_id):
        """traverse through edges and returns YA node_ID and I node_ID, given L node_ID"""
        for entry in self.xaif['edges']:
            if n_id == entry['fromID']:
                ya_node_id = entry['toID']
                for entry2 in self.xaif['edges']:
                    if ya_node_id == entry2['fromID']:
                        inode_id = entry2['toID']
                        return(inode_id, ya_node_id)
        return None, None
    

    def remove_entries(self, l_node_id):
        """
        Removes entries associated with a specific node ID from a JSON dictionary.

        Arguments:
        - node_id (int): the node ID to remove from the JSON dictionary
        - json_dict (Dict): the JSON dictionary to edit

        Returns:
        - (Dict): the edited JSON dictionary with entries associated with the specified node ID removed
        """
        # Remove nodes with the specified node ID
        in_id, yn_id = self.get_i_node_ya_nodes_for_l_node(self.aif['edges'], l_node_id)
        edited_nodes = [node for node in self.aif['nodes'] if node.get('nodeID') != l_node_id]
        edited_nodes = [node for node in edited_nodes if node.get('nodeID') != in_id]

        # Remove locutions with the specified node ID
        
        edited_locutions = [node for node in self.xif['locutions'] if node.get('nodeID') != l_node_id]

        # Remove edges with the specified node ID
        edited_edges = [node for node in self.aif['edges'] if not (node.get('fromID') == l_node_id or node.get('toID') == l_node_id)]
        edited_edges = [node for node in edited_edges if not (node.get('fromID') == in_id or node.get('toID') == in_id)]
        edited_nodes = [node for node in edited_nodes if node.get('nodeID') != yn_id]
        # Return the edited JSON dictionary
        return edited_nodes, edited_edges, edited_locutions
    

    def get_xAIF_arrays(self, aif_section: dict, xaif_elements: List) -> tuple:
        """
        Extracts values associated with specified keys from the given AIF section dictionary.

        Args:
            aif_section (dict): A dictionary containing AIF section information.
            xaif_elements (List): A list of keys for which values need to be extracted from the AIF section.

        Returns:
            tuple: A tuple containing values associated with the specified keys from the AIF section.
        """
        # Extract values associated with specified keys from the AIF section dictionary
        # If a key is not present in the dictionary, returns an empty list as the default value
        return tuple(aif_section.get(element) for element in xaif_elements)


	

data = { 'aif' : {'nodes': [], 'edges':[], 'locutions': [], 'participants':[]}
        }
aif = AIF(data)
print(aif.is_valid_json_aif())



