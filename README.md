# xaif_eval

[![PyPI version](https://badge.fury.io/py/xaif_eval.svg)](https://badge.fury.io/py/xaif_eval)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python version](https://img.shields.io/badge/python-%3E=3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

## Overview

`xaif_eval` is a Python library designed for handling and manipulating AIF (Argument Interchange Format) structures. It provides utilities to validate, traverse, and manipulate AIF JSON structures, facilitating the development and evaluation of argumentation frameworks.

## Features

- Validate AIF JSON structures
- Generate unique node and edge IDs
- Add and manage argument components


## Installation

You can install the `xaif_eval` package via pip:

```sh
pip install xaif_eval
```

## Usage

### Importing the Library

```python
from xaif_eval import AIF
```

### Example

```python
from xaif_eval import AIF

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

# Initialize the AIF object
aif = AIF(xaif)

# Check if the AIF JSON is valid
is_valid = aif.is_valid_json_aif()
print(f"Is valid AIF JSON: {is_valid}")

# Check if the AIF JSON is a dialog
is_dialog = aif.is_json_aif_dialog()
print(f"Is dialog: {is_dialog}")

# Get the next max node ID
next_node_id = aif.get_next_max_id('nodes', 'nodeID')
print(f"Next node ID: {next_node_id}")

# Get the speaker of a node
speaker = aif.get_speaker(1)
print(f"Speaker: {speaker}")

# Add argument relation
aif.add_component("argument_relation", Relation_type, I_nodeID-1, I_nodeID-2)
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

