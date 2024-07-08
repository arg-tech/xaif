from typing import  List

    
class AIF:
    def __init__(self, xaif):
        self.xaif = xaif
        self.aif = xaif.get('AIF')
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
    

    def get_next_max_id(self, component_type, id_key_word):
        """
       Takes a list of nodes (edges) and returns the maximum node/edge ID.
        Arguments:
        - nodes/edges (List[Dict]): a list of nodes/edges, where each node is a dictionary containing a node/edge ID
        Returns:
        - (int): the maximum node/edge ID in the list of nodes
        """
        component_entries = self.aif.get(component_type,[])
        max_id, lef_n_id, right_n_id = 0, 0, ""
        if isinstance(component_entries[0][id_key_word],str): # check if the node id is a text or integer
            if "_" in component_entries[0][id_key_word]:
                for node in component_entries:
                    temp_id = node[id_key_word]
                    if "_" in temp_id:
                        nodeid_parsed = temp_id.split("_") # text node id can involve the character "_"
                        lef_n_id, right_n_id = int(nodeid_parsed[0]), nodeid_parsed[1]
                        if lef_n_id > max_id:
                            max_id = lef_n_id
                return str(int(max_id)+1)+"_"+str(right_n_id)
            else:
                for node in component_entries:
                    temp_id = int(node[id_key_word])     
                    if temp_id > max_id:
                        max_id = temp_id   
                return str(max_id+1)

        elif isinstance(component_entries[0][id_key_word],int):	
            for node in component_entries:
                temp_id = node[id_key_word]     
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
        for locution in self.xaif['AIF']['locutions']:
            personID = locution['personID']
            nodeID = locution['nodeID']
            
            # Loop through each participant and check if their participant ID matches the person ID from the locution
            for participant in self.xaif['AIF']['participants']:
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

    def add_component(self, component_type: str, *args):
        """
        A function to add a component to the AIF.

        Args:
            component_type (str): Type of the component to add.
            *args: Variable number of arguments depending on the component type.
        """
        if component_type == 'argument_relation':
            self._add_argument_relation(*args)
        elif component_type == 'segment':
            self._add_segment(*args)
        else:
            raise ValueError("Invalid component type. Supported types are 'argument_relation' and 'segment'.")

    
    def _add_argument_relation(self, prediction, index1, index2):

        if prediction == "RA":
            AR_text = "Default Inference"
            AR_type = "RA"
        elif prediction == "CA":	
            AR_text = "Default Conflict"
            AR_type = "CA"
        elif prediction == "MA":	
            AR_text = "Default Rephrase"
            AR_type = "MA"
        node_id = self.get_next_max_id( 'nodes', 'nodeID')
        edge_id = self.get_next_max_id( 'edges', 'edgeID')
        self.aif['nodes'].append({'text': AR_text, 'type':AR_type,'nodeID': node_id})				
        self.aif['edges'].append({'fromID': index1, 'toID': node_id,'edgeID':edge_id})
        edge_id = self.get_next_max_id('edges', 'edgeID')
        self.aif['edges'].append({'fromID': node_id, 'toID': index2,'edgeID':edge_id})



    def _add_segment(self, Lnode_ID, segment):       
        speaker, speaker_id = "", None		
        if self.xaif['AIF']['participants']:
            speaker, speaker_id = self.get_speaker(Lnode_ID)
            first_name_last_name = speaker.split()
            first_n, last_n = first_name_last_name[0], first_name_last_name[1]
            if last_n=="None":
                speaker = first_n
            else:
                speaker = first_n+" " + last_n
        else:
            first_n, last_n  = "None", "None"

        node_id = self.get_next_max_id('nodes', 'nodeID')
        self.xaif['AIF']['nodes'].append({'text': segment, 'type':'L','nodeID': node_id})		
        self.xaif['AIF']['locutions'].append({'personID': speaker_id, 'nodeID': node_id})
        self.remove_entry(Lnode_ID)
    
    def get_i_node_ya_nodes_for_l_node(self, Lnode_ID):
        """traverse through edges and returns YA node_ID and I node_ID, given L node_ID"""
        for entry in self.xaif['AIF']['edges']:
            if Lnode_ID == entry['fromID']:
                ya_node_id = entry['toID']
                for entry2 in self.xaif['AIF']['edges']:
                    if ya_node_id == entry2['fromID']:
                        inode_id = entry2['toID']
                        return(inode_id, ya_node_id)
        return None, None
    

    def remove_entry(self, Lnode_ID):
        """
        Removes entries associated with a specific node ID from a JSON dictionary.

        Arguments:
        - node_id (int): the node ID to remove from the JSON dictionary
        - json_dict (Dict): the JSON dictionary to edit

        Returns:
        - (Dict): the edited JSON dictionary with entries associated with the specified node ID removed
        """
        # Remove nodes with the specified node ID
        in_id, yn_id = self.get_i_node_ya_nodes_for_l_node(Lnode_ID)
        self.xaif['AIF']['nodes'] = [node for node in self.xaif['AIF']['nodes'] if node.get('nodeID') != Lnode_ID]
        self.xaif['AIF']['nodes'] = [node for node in self.xaif['AIF']['nodes'] if node.get('nodeID') != in_id]

        # Remove locutions with the specified node ID
        
        self.xaif['AIF']['locutions'] = [node for node in self.xaif['AIF']['locutions'] if node.get('nodeID') != Lnode_ID]

        # Remove edges with the specified node ID
        self.xaif['AIF']['edges'] = [node for node in self.xaif['AIF']['edges'] if not (node.get('fromID') == Lnode_ID or node.get('toID') == Lnode_ID)]
        self.xaif['AIF']['edges'] = [node for node in self.xaif['AIF']['edges'] if not (node.get('fromID') == in_id or node.get('toID') == in_id)]
        self.xaif['AIF']['nodes'] = [node for node in self.xaif['AIF']['nodes'] if node.get('nodeID') != yn_id]

    

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


	




