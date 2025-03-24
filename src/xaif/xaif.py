from typing import  List
import pandas as pd
from .xaif_templates import XAIF
import json

#python3 -m build  
# twine upload dist/*   

    
class AIF:
    def __init__(self, xaif):

        if isinstance(xaif,str):
            xaif = json.loads(self.initilise_empty(xaif))       
        self.xaif = xaif
        self.aif = xaif.get('AIF')
        self.nodes = self.aif.get('nodes')
        self.locutions = self.aif.get('locutions')
        self.participants = self.aif.get('participants')
    def initilise_empty(self,xaif):
            node_id, person_id = 0, 0
            aif, json_aif, OVA = {}, {}, {}      
            text_with_span = ""
            nodes, edges, schemefulfillments, descriptorfulfillments, participants, locutions = [], [], [], [], [], []
            speakers_and_turns = xaif                  
            nodes, locutions, participants, text_with_span, node_id, person_id = self.create_turn_entry(
                nodes, node_id, person_id, text_with_span, speakers_and_turns, locutions, participants, False)
            return XAIF.format(nodes, edges, locutions, schemefulfillments, descriptorfulfillments, participants, OVA, text_with_span, aif, {})


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
       Takes a list of nodesor/edges and returns the maximum node/edge ID.
        Arguments:
        - nodes/edges (List[Dict]): a list of nodes/edges, where each node is a dictionary containing a node/edge ID
        Returns:
        - (int): the maximum node/edge ID in the list of nodes
        """
        component_entries = self.aif.get(component_type,[])
        max_id, lef_n_id, right_n_id = 0, 0, ""
        if len(component_entries) == 0:
            return 0
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
        Takes a node ID and returns the name of the participant who spoke the locution with the given node ID, or "None" 
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

    def add_component(self, component_type: str, **kwargs):
        """
        A function to add a component to the AIF.

        Args:
            component_type (str): Type of the component to add.
            *args: Variable number of arguments depending on the component type.
        """
        if component_type == 'argument_relation':
            self._add_argument_relation(**kwargs)
        elif component_type == 'segment':
            self._add_segment(**kwargs)
        elif component_type == 'locution':
            self._add_Lnode(**kwargs)
        elif component_type == 'proposition':
            self._add_proposition(**kwargs)
        else:
            raise ValueError("Invalid component type. Supported types are 'argument_relation' and 'segment'.")

    
    def _add_argument_relation(self, relation_type, iNode_ID1, iNode_ID2,AR_text=None):
        prediction, index1, index2 = relation_type, iNode_ID1, iNode_ID2
        AR_type = prediction
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

    def _add_Lnode(self, text, speaker):       
        
        first_name_last_name = speaker.split()
        first_n, last_n = first_name_last_name[0], first_name_last_name[1]


        node_id = self.get_next_max_id('nodes', 'nodeID')
        self.xaif['AIF']['nodes'].append({'text': text, 'type':'L','nodeID': node_id})	
        self.xaif['AIF']['locutions'].append({'personID': 1, 'nodeID': node_id})
        # Loop through each participant and check if their participant ID matches the person ID from the locution
        if not any(participant['firstname'] == first_n and participant['surname'] == last_n for participant in self.xaif['AIF']['participants']):
            self.xaif['AIF']['participants'].append(
                    {
                    "participantID": 1,                                
                    "firstname": first_n,                                
                    "surname": last_n
                    }
            )


    def _add_segment(self, Lnode_ID, segments):       
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
        for segment in segments:
            node_id = self.get_next_max_id('nodes', 'nodeID')
            self.xaif['AIF']['nodes'].append({'text': segment, 'type':'L','nodeID': node_id})		
            self.xaif['AIF']['locutions'].append({'personID': speaker_id, 'nodeID': node_id})



        self.remove_entry(Lnode_ID)
    def _add_proposition(self, Lnode_ID, proposition):       

        node_id = self.get_next_max_id('nodes', 'nodeID')
        self.xaif['AIF']['nodes'].append({'text': proposition, 'type':'I','nodeID': node_id})
        ya_node_id = self.get_next_max_id('nodes', 'nodeID')
        self.xaif['AIF']['nodes'].append({'text': "Default Illocuting", 'type':'YA','nodeID': ya_node_id})
        edge_id = self.get_next_max_id('edges', 'edgeID')	
        edgefrom = {'edgeID':edge_id, 'fromID':Lnode_ID, 'toID':ya_node_id}
        edge_id = self.get_next_max_id('edges', 'edgeID')	
        edgeto= {'edgeID':edge_id, 'fromID':ya_node_id, 'toID':node_id}
        self.xaif['AIF']['edges'].append(edgefrom)
        self.xaif['AIF']['edges'].append(edgeto)

        

    
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




    def _create_none_pairs(self, propositions_dict):
        """
        Creates a DataFrame from a dictionary of propositions with pairs, including their IDs and a default 'relation' column.

        Args:
            propositions_dict (dict): Dictionary where keys are proposition IDs and values are propositions.

        Returns:
            pd.DataFrame: DataFrame with columns 'proposition_id_1', 'proposition_1', 'proposition_id_2', 'proposition_2', and 'relation'.
        """
        # Extract keys and values
        ids = list(propositions_dict.keys())
        props = list(propositions_dict.values())
        
        # Generate pairs with IDs
        pairs = []
        for i in range(len(ids)):
            for j in range(len(ids)):
                if i != j:
                    pairs.append((ids[i], props[i], ids[j], props[j]))



        return pairs

    # Example usage



    def _get_relations_argument(self, nodes, edges,relation_type):
        visited = {}
        dct_arg_structure = {'proposition1_id':[],
                             'proposition1_text':[],
                             'proposition2_id':[],
                             'proposition2_text':[],
                             'relation':[]
                             }
        if relation_type == "argument-relation": 
            AR_relations = {node['nodeID']:node['text'] for node in nodes if node['type'] in ['CA','RA','MA']}
            I_nodes = {node['nodeID']:node['text'] for node in nodes if node['type']=="I"}
        if relation_type == "locution":
            AR_relations = {node['nodeID']:node['text'] for node in nodes if node['type'] in ['YA']}
            I_nodes = {node['nodeID']:node['text'] for node in nodes if node['type']=="L"}
               
        for edge in edges:
            relation,proposition_1, proposition_2 = None,None,None
            if edge['toID'] in AR_relations.keys() and edge['fromID'] in I_nodes.keys():
                proposition_1 = edge['fromID'] 
                for edge2 in edges:
                    if edge2['fromID'] in AR_relations.keys() and edge2['fromID']==edge['toID'] and edge2['toID'] in I_nodes.keys():
                        proposition_2 = edge2['toID'] 
                        relation =AR_relations[edge2['fromID']]
            if proposition_1 and proposition_2:
                dct_arg_structure['proposition1_id'].append(proposition_1)
                dct_arg_structure['proposition1_text'].append(I_nodes[proposition_1])
                dct_arg_structure['proposition2_id'].append(proposition_2)
                dct_arg_structure['proposition2_text'].append(I_nodes[proposition_2])
                dct_arg_structure['relation'].append(relation)
        return dct_arg_structure
    
    def _get_relations_locution(self, nodes, edges,relation_type):
        dct_arg_structure = {'proposition1_id':[],
                             'proposition1_text':[],
                             'proposition2_id':[],
                             'proposition2_text':[],
                             'relation':[]
                             }
        if relation_type == "argument-relation": 
            AR_relations = {node['nodeID']:node['text'] for node in nodes if node['type'] in ['CA','RA','MA']}
            I_nodes = {node['nodeID']:node['text'] for node in nodes if node['type']=="I"}
        if relation_type == "locution":
            AR_relations = {node['nodeID']:node['text'] for node in nodes if node['type'] in ['YA']}
            L_nodes = {node['nodeID']:node['text'] for node in nodes if node['type']=="L"}
            I_nodes = {node['nodeID']:node['text'] for node in nodes if node['type']=="I"}
               
        for edge in edges:
            relation,proposition_1, proposition_2 = None,None,None
            if edge['toID'] in AR_relations.keys() and edge['fromID'] in L_nodes.keys():
                proposition_1 = edge['fromID'] 
                for edge2 in edges:
                    if edge['toID'] ==edge2['fromID'] and  edge2['fromID'] in AR_relations.keys() and edge2['toID'] in I_nodes.keys():
                        proposition_2 = edge2['toID'] 
                        relation = AR_relations[edge2['fromID']]

            if proposition_1 and proposition_2:
                dct_arg_structure['proposition1_id'].append(proposition_1)
                dct_arg_structure['proposition1_text'].append(L_nodes[proposition_1])
                dct_arg_structure['proposition2_id'].append(proposition_2)
                dct_arg_structure['proposition2_text'].append(I_nodes[proposition_2])
                dct_arg_structure['relation'].append(relation)
        return dct_arg_structure
        
    def get_csv(self,relation_type):

        """
            Generates a DataFrame from the AIF data based on the specified relation type.

            Args:
                relation_type (str): Type of relation to filter nodes by. Should be either 
                                    "argument-relation" or another valid type.

            Returns:
                pd.DataFrame: A DataFrame containing the relations between propositions, 
                            with columns for proposition IDs, texts, and their relations.
                            If no relations are found, default values are set with 'None' for relation.
            """
        # Retrieve the AIF structure from the xaif attribute
        aif = self.xaif.get("AIF")
              
        if aif:
            nodes,edges = aif.get('nodes'),aif.get('edges')
            if nodes:
                if relation_type == "argument-relation":
                    propositions =  {prop['nodeID']:prop['text'] for prop in nodes if prop['type']=="I"}
                elif relation_type == "locution":
                    propositions = {prop['nodeID']:prop['text'] for prop in nodes if prop['type']=="L"}  
                if edges:
                    # Convert dictionary to DataFrame
                    if relation_type == "argument-relation":
                        dct_arg_structure = self._get_relations_argument(nodes, edges, relation_type)
                    if relation_type == "locution":
                        dct_arg_structure = self._get_relations_locution(nodes, edges, relation_type)
                    if len(dct_arg_structure['relation'])>0:
                        # Create DataFrame for dct_arg_structure
                        df = pd.DataFrame(dct_arg_structure)
                        
                        # Create DataFrame for new pairs (none_df)
                        pairs = self._create_none_pairs(propositions)                   
                        none_df = pd.DataFrame(pairs, columns=['proposition1_id', 'proposition1_text', 'proposition2_id', 'proposition2_text'])
                        none_df['relation'] = 'None'  # Set default value for 'relation'

                        # Create a set of existing pairs from df for fast lookup
                        existing_pairs = set(zip(df['proposition1_text'], df['proposition2_text']))



                        # Filter out pairs in none_df that are already present in df
                        none_df_filtered = none_df[~none_df.apply(
                            lambda row: (row['proposition1_text'], row['proposition2_text']) in existing_pairs, axis=1
                        )]



                        # Add the filtered new pairs to df
                        df = pd.concat([df, none_df_filtered], ignore_index=True)


              
                    else:
                         # Create DataFrame
                        pairs = self._create_none_pairs(propositions)                   
                        # Create DataFrame
                        df = pd.DataFrame(pairs, columns=['proposition1_id', 'proposition1_text', 'proposition2_id', 'proposition2_text'])
                        df['relation'] = 'None'  # Set default value for 'relation'                   
                else:
                    # Create DataFrame
                    pairs = self._create_none_pairs(propositions)                   
                    # Create DataFrame
                    df = pd.DataFrame(pairs, columns=['proposition1_id', 'proposition1_text', 'proposition2_id', 'proposition2_text'])
                    df['relation'] = 'None'  # Set default value for 'relation'
            return df
    def create_turn_entry(
        self,
        nodes, 
        node_id,
        person_id, 
        text_with_span,
        propositions,
        locutions,
        participants,
        dialogue 
        ):
        if dialogue:
            for first_and_last_names, proposition in propositions:
                first_last_names = first_and_last_names.split()
                first_names, last_names = "None", "None"
                if len(first_last_names) > 1:
                    first_names,last_names = first_last_names[0],first_last_names[1]
                else:
                    first_names, last_names = first_last_names[0],"None"
                text = proposition.replace("\n","")
                nodes.append({'text': text, 'type':'L','nodeID': node_id})
                locutions.append({'personID': person_id, 'nodeID': node_id})
                # Check if the entry already exists based on first name and surname
                if not any(participant['firstname'] == first_names and participant['surname'] == last_names for participant in participants):
                    participants.append({
                        "participantID": person_id,
                        "firstname": first_names,
                        "surname": last_names
                    })
                text_with_span = text_with_span+" "+first_names+" "+last_names+": "+"<span class=\"highlighted\" id=\""+str(node_id)+"\">"+text+"</span>.<br><br>"
                node_id = node_id + 1 
                person_id = person_id + 1


        else:
            text = propositions.replace("\n","")
            speaker = "Default Speaker"
            nodes.append({'text': text, 'type':'L','nodeID': node_id})	
            locutions.append({'personID': 1, 'nodeID': node_id})
            if not any(participant['firstname'] == "Default" and participant['surname'] == "Speaker" for participant in participants):
                participants.append(
                        {
                        "participantID": 1,                                
                        "firstname": "Default",                                
                        "surname": "Speaker"
                        }
                    )	
            text_with_span=text_with_span+" "+"<span class=\"highlighted\" id=\""+str(node_id)+"\">"+text+"</span>.<br><br>"
            node_id = node_id + 1
        return (
            nodes, 
            locutions,
            participants, 
            text_with_span, 
            node_id,
            person_id
            )


'''
aif = AIF("here is the text.")

speaker = "First Speaker"
text = "another text"
aif.add_component("locution", text, speaker)
aif.add_component("locution", "the third text. fourth text", "Second Speaker")
aif.add_component("segment", 2, ["the third text.", "fourth text"])
aif.add_component("proposition", 3, "the third text.")
aif.add_component("proposition", 4, "fourth text.")
aif.add_component("argument_relation", "RA", 5,7)


print(aif.xaif)

print(aif.get_csv("argument-relation"))
'''

