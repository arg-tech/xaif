# xaif

[![PyPI version](https://badge.fury.io/py/xaif_eval.svg)](https://badge.fury.io/py/xaif_eval)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python version](https://img.shields.io/badge/python-%3E=3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

## Overview

`xaif` is a Python library for working with Argument Interchange Format (AIF), primarily designed to facilitate the development, manipulation, and evaluation of argumentat structures. This package provides essential utilities to validate, traverse, and manipulate AIF-compliant JSON structures, enabling users to effectively work with complex argumentation data.

## xAIF Format

Here is an example of empty `xAIF` JSON format:

```json
{
  "AIF": {
    "nodes": [],
    "edges": [],
    "schemefulfillments": [],
    "descriptorfulfillments": [],
    "participants": [],
    "locutions": []
  },
  "text": "",
  "dialog": true,
  "OVA": {
    "firstname": "",
    "surname": "",
    "url": "",
    "nodes": [],
    "edges": []
  }
}
```

## Features

- Manage argument components: Add and manipulate various components of an argumentation framework, including relations, nodes, and edges.
- Export data in CSV format: Generate tabular representations of argument components with their respective relation types.


## Installation

You can install the `xaif` package via pip:

```sh
pip install xaif
```

## Usage

### Importing the Library

```python
from xaif import AIF
```

### Example

```python
from xaif import AIF

# Sample xAIF JSON 
aif= {
  "AIF": {
    "descriptorfulfillments": null,
    "edges": [
      {
        "edgeID": 0,
        "fromID": 0,
        "toID": 4
      },
      {
        "edgeID": 1,
        "fromID": 4,
        "toID": 3
      },
      {
        "edgeID": 2,
        "fromID": 1,
        "toID": 6
      },
      {
        "edgeID": 3,
        "fromID": 6,
        "toID": 5
      },
      {
        "edgeID": 4,
        "fromID": 2,
        "toID": 8
      },
      {
        "edgeID": 5,
        "fromID": 8,
        "toID": 7
      },
      {
        "edgeID": 6,
        "fromID": 3,
        "toID": 9
      },
      {
        "edgeID": 7,
        "fromID": 9,
        "toID": 7
      }
    ],
    "locutions": [
      {
        "nodeID": 0,
        "personID": 0
      },
      {
        "nodeID": 1,
        "personID": 1
      },
      {
        "nodeID": 2,
        "personID": 2
      }
    ],
    "nodes": [
      {
        "nodeID": 0,
        "text": "disagreements between party members are entirely to be expected.",
        "type": "L"
      },
      {
        "nodeID": 1,
        "text": "the SNP has disagreements.",
        "type": "L"
      },
      {
        "nodeID": 2,
        "text": "it's not uncommon for there to be disagreements between party members.",
        "type": "L"
      },
      {
        "nodeID": 3,
        "text": "disagreements between party members are entirely to be expected.",
        "type": "I"
      },
      {
        "nodeID": 4,
        "text": "Default Illocuting",
        "type": "YA"
      },
      {
        "nodeID": 5,
        "text": "the SNP has disagreements.",
        "type": "I"
      },
      {
        "nodeID": 6,
        "text": "Default Illocuting",
        "type": "YA"
      },
      {
        "nodeID": 7,
        "text": "it's not uncommon for there to be disagreements between party members.",
        "type": "I"
      },
      {
        "nodeID": 8,
        "text": "Default Illocuting",
        "type": "YA"
      },
      {
        "nodeID": 9,
        "text": "Default Inference",
        "type": "RA"
      }
    ],
    "participants": [
      {
        "firstname": "Speaker",
        "participantID": 0,
        "surname": "1"
      },
      {
        "firstname": "Speaker",
        "participantID": 1,
        "surname": "2"
      }
    ],
    "schemefulfillments": null
  },
  "dialog": true,
  "ova": [],
  "text": {
    "txt": " Speaker 1 <span class=\"highlighted\" id=\"0\">disagreements between party members are entirely to be expected.</span>.<br><br> Speaker 2 <span class=\"highlighted\" id=\"1\">the SNP has disagreements.</span>.<br><br> Speaker 1 <span class=\"highlighted\" id=\"2\">it's not uncommon for there to be disagreements between party members. </span>.<br><br>"
  }
}


# Initialize the AIF object with xAIF data (AIF data structure provided as input)
aif = AIF(xaif_data)

# Example: Working with xAIF in the AIF Class

# Initialize the AIF object with xAIF data (AIF data structure provided as input)
# Here, 'xaif_data' is expected to be a valid xAIF structure in JSON format
aif = AIF(xaif_data)

# Alternatively, initialize the AIF object with raw text data.
# The AIF object will automatically create locutions and other necessary components from the provided text.
aif = AIF("First Sentence. ")

# Adding components to the AIF object:

# 1. Adding a new locution (a statement made by a speaker)
# 'component_type' is specified as "locution", and you provide the 'text' of the locution and the 'speaker' name.
# The next available ID (1 in this case) will be automatically assigned to this locution.
aif.add_component(component_type="locution", text="Second Sentence.", speaker="Default Speaker")

# 2. Adding a proposition (a logical statement associated with a locution)
# The 'component_type' is specified as "proposition", and you provide the locution ID (Lnode_ID) and the proposition text.
# The associated locution ID (0) is required. 
# This creates an I-node (proposition node) with the next available ID (2), and a YA (Default Illocuting) node with ID 3.
aif.add_component(component_type="proposition", Lnode_ID=0, proposition="First sentence.")

# 3. Adding another proposition (another logical statement associated with another locution)
# Here, the 'component_type' is again "proposition", and the associated locution ID (1) is required.
# This creates an I-node with ID 4 and a YA-node with ID 5 to anchor the relation between the I-node and the associated locution.
aif.add_component(component_type="proposition", Lnode_ID=1, proposition="Second sentence.")

# 4. Adding an argument relation (representing the logical connection between propositions)
# 'component_type' is specified as "argument_relation", and you provide the relation type (e.g., "RA" for default inference).
# Here, you are creating an argument relation between two I-nodes (IDs 2 and 4), with the relation type "RA".
# This creates an RA node and edges between the I-nodes and the RA-node.
aif.add_component(component_type="argument_relation", relation_type="RA", iNode_ID2=2, iNode_ID1=4)

# Print the generated xAIF structure to visualize the entire argumentation framework
print(aif.xaif)

# Exporting the data:
# To export the argument relations in CSV format, use the get_csv method with "argument-relation" as the argument.
print(aif.get_csv("argument-relation"))  # Exports proposition pairs with argument relations in tabular (CSV) format.

# To export the locution data in CSV format, use the get_csv method with "locution" as the argument.
print(aif.get_csv("locution"))  # Exports locution data in tabular (CSV) format.



```

## Documentation

The full documentation is available at [xaif_eval Documentation](https://github.com/debelatesfaye/xaif).

## Contributing

Contributions are welcome! Please visit the [Contributing Guidelines](https://github.com/debelatesfaye/xaif/blob/main/CONTRIBUTING.md) for more information.

## Issues

If you encounter any problems, please file an issue at the [Issue Tracker](https://github.com/debelatesfaye/xaif/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/debelatesfaye/xaif/blob/main/LICENSE) file for details.

## Authors

- DEBELA - [d.t.z.gemechu@dundee.ac.uk](mailto:d.t.z.gemechu@dundee.ac.uk)

## Acknowledgments

- Thanks to all contributors and users for their feedback and support.
```

