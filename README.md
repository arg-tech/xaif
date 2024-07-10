# xaif_eval

[![PyPI version](https://badge.fury.io/py/xaif_eval.svg)](https://badge.fury.io/py/xaif_eval)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python version](https://img.shields.io/badge/python-%3E=3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

## Overview

`xaif_eval` is a Python library designed for handling and manipulating AIF (Argument Interchange Format) structures. It provides utilities to validate, traverse, and manipulate AIF JSON structures, facilitating the development and evaluation of argumentation frameworks.

## Features

- Validate AIF JSON structures
- Generate unique node and edge IDs
- Add and manage argument components (L nodes, I nodes, edges)


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

# Sample AIF JSON structure
xaif = {
    "AIF": {
        "nodes": [
            {"type": "L", "nodeID": 1},
            {"type": "I", "nodeID": 2}
        ],
        "edges": [
            {"fromID": 1, "toID": 2, "edgeID": 1}
        ],
        "locutions": [
            {"personID": 1, "nodeID": 1}
        ],
        "participants": [
            {"participantID": 1, "firstname": "Alice", "surname": "Smith"}
        ]
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

- DEBELA - [dabookoo@gmail.com](mailto:dabookoo@gmail.com)

## Acknowledgments

- Thanks to all contributors and users for their feedback and support.
```

