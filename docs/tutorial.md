# xAIF (Extended Argumentation Interchange Format) Documentation


## Table of Contents
1. [Overview](#overview)
2. [Features of xAIF](#features-of-xaif)
3. [Structure of xAIF](#structure-of-xaif)
   - [Main Components](#main-components)
4. [Example xAIF JSON](#example-xaif-json)
   - [Blank example](#blank-example)
   - [Basic xAIF Example](#basic-xaif-example)
   - [An example from OVA](#an-example-from-ova)
   - [An example with OVA, PropositionClassifier and Skeptic](#An-example-with-OVA-PropositionClassifier-and-Skeptic)
5. [xaif library](#xaif-library)


## Overview

xAIF (Extended Argumentation Interchange Format) is an extension of the AIF (Argumentation Interchange Format) [AIF Specification](https://www.arg-tech.org/wp-content/uploads/2011/09/aif-spec.pdf), designed to handle more flexible and dynamic argument structures in environments of incremental processing. AIF imposes certain constraints, such as requiring relations to have exactly one consequent and at least one antecedent, and limiting interconnections between propositions to relations. While these constraints are valuable in a fully formed argument structure, they can be too restrictive for environments where arguments are being built piecemeal or where intermediate annotations are needed. This is where xAIF comes in. It extends the AIF to allow for both **underspecified** and **overspecified** argumentation structures, making it a more versatile tool for argumentation representation.

### Features of xAIF:
1. **Underspecification**: Some constraints present in basic AIF (such as the number of antecedents or consequents in a relation) are relaxed, allowing for incomplete or evolving argumentation structures.
2. **Overspecification**: Additional structural markup can be added beyond the standard AIF, which can help represent intermediate discourse annotations that go beyond the formal structure of arguments.
3. **JSON-Based**: xAIF is represented in a convenient JSON format, making it easy to handle programmatically and compatible with a wide range of tools and platforms.
4. **Interlingua for Argument Mining**: xAIF serves as the interlingua for the open argument mining framework, facilitating both input and output for all its modules.

## Structure of xAIF

xAIF is represented as a JSON object that contains several key sections. Below is a breakdown of the structure, followed by an example of a sample xAIF representation.

### Main Components:
1. **AIF**: Contains the main argumentation structure, which includes descriptors, edges, locutions, nodes, participants, and scheme fulfillments.
   - **descriptorfulfillments**: Can be used to track how descriptors are fulfilled in the argumentation structure. In basic xAIF, this may be left as `null`.
   - **edges**: Defines the relationships between nodes (propositions or claims), where each edge connects two nodes. Edges are defined with a unique `edgeID` and `fromID` / `toID` indicating the direction of the relation.
   - **locutions**: The utterances associated with participants (e.g., statements or claims made by speakers). Each locution is tied to a node and a participant.
   - **nodes**: Represents individual propositions, claims, or other argumentation elements. Each node is identified by a unique `nodeID`, has associated text (`text`), and a type (`type`), which can specify whether the node is a **Locution (L)**, **Illocution (I)**, **Inference (RA)**, or **Argumentation (YA)**.
   - **participants**: Information about the speakers or contributors to the discourse, identified by a unique `participantID`.
   - **schemefulfillments**: Similar to descriptorfulfillments, but focused on tracking specific argumentation schemes. This can also be `null` in basic implementations.

2. **dialog**: A boolean flag indicating whether the text is part of a dialogue. If set to `true`, the text represents an exchange between two or more participants.
3. **ova**: An array for additional annotations or visualizations that may be required by specific applications.
4. **text**: Contains the raw textual dialogue, with each speaker's contribution marked by their corresponding span IDs, allowing for easy visualization and interaction.

### Example xAIF JSON

#### Blank example

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

#### Basic xAIF Example
```json
{
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
```

#### An example from OVA

```json
{
	"AIF": {
		"nodes": [{
			"nodeID": "2_164926129380455983",
			"text": "A",
			"type": "I"
		}, {
			"nodeID": "3_164926129380455983",
			"text": "Participant Rachel: A",
			"type": "L"
		}, {
			"nodeID": "4_164926129380455983",
			"text": "Analysing",
			"type": "YA"
		}, {
			"nodeID": "5_164926129380455983",
			"text": "Anon: Participant Rachel: A",
			"type": "L"
		}, {
			"nodeID": "6_164926129380455983",
			"text": "Asserting",
			"type": "YA"
		}, {
			"nodeID": "15_164926162804546033",
			"text": "B",
			"type": "I"
		}, {
			"nodeID": "16_164926162804546033",
			"text": "Participant Rachel: B",
			"type": "L"
		}, {
			"nodeID": "17_164926162804546033",
			"text": "Analysing",
			"type": "YA"
		}, {
			"nodeID": "18_164926162804546033",
			"text": "Anon: Participant Rachel: B",
			"type": "L"
		}, {
			"nodeID": "19_164926162804546033",
			"text": "Asserting",
			"type": "YA"
		}, {
			"nodeID": "20_164926162804546033",
			"text": "Default Transition",
			"type": "TA"
		}, {
			"nodeID": "21_164926162804546033",
			"text": "Default Inference",
			"type": "RA"
		}, {
			"nodeID": "22_164926162804546033",
			"text": "Arguing",
			"type": "YA"
		}],
		"edges": [{
			"edgeID": 1,
			"fromID": "4_164926129380455983",
			"toID": "3_164926129380455983"
		}, {
			"edgeID": 2,
			"fromID": "5_164926129380455983",
			"toID": "4_164926129380455983"
		}, {
			"edgeID": 3,
			"fromID": "3_164926129380455983",
			"toID": "6_164926129380455983"
		}, {
			"edgeID": 4,
			"fromID": "6_164926129380455983",
			"toID": "2_164926129380455983"
		}, {
			"edgeID": 5,
			"fromID": "17_164926162804546033",
			"toID": "16_164926162804546033"
		}, {
			"edgeID": 6,
			"fromID": "18_164926162804546033",
			"toID": "17_164926162804546033"
		}, {
			"edgeID": 7,
			"fromID": "16_164926162804546033",
			"toID": "19_164926162804546033"
		}, {
			"edgeID": 8,
			"fromID": "19_164926162804546033",
			"toID": "15_164926162804546033"
		}, {
			"edgeID": 9,
			"fromID": "3_164926129380455983",
			"toID": "20_164926162804546033"
		}, {
			"edgeID": 10,
			"fromID": "20_164926162804546033",
			"toID": "16_164926162804546033"
		}, {
			"edgeID": 11,
			"fromID": "15_164926162804546033",
			"toID": "21_164926162804546033"
		}, {
			"edgeID": 12,
			"fromID": "21_164926162804546033",
			"toID": "2_164926129380455983"
		}, {
			"edgeID": 13,
			"fromID": "20_164926162804546033",
			"toID": "22_164926162804546033"
		}, {
			"edgeID": 14,
			"fromID": "22_164926162804546033",
			"toID": "21_164926162804546033"
		}],
		"schemefulfillments": [{
			"nodeID": "4_164926129380455983",
			"schemeID": "75"
		}, {
			"nodeID": "6_164926129380455983",
			"schemeID": "74"
		}, {
			"nodeID": "17_164926162804546033",
			"schemeID": "75"
		}, {
			"nodeID": "19_164926162804546033",
			"schemeID": "74"
		}, {
			"nodeID": "20_164926162804546033",
			"schemeID": "82"
		}, {
			"nodeID": "21_164926162804546033",
			"schemeID": "72"
		}, {
			"nodeID": "22_164926162804546033",
			"schemeID": "80"
		}],
		"descriptorfulfillments": [],
		"participants": [{
			"participantID": 1,
			"firstname": "Participant",
			"surname": "Rachel"
		}, {
			"participantID": 2,
			"firstname": "Participant",
			"surname": "Carolyn"
		}, {
			"participantID": 3,
			"firstname": "Participant",
			"surname": "Mo"
		}, {
			"participantID": 4,
			"firstname": "Participant",
			"surname": "Zoe"
		}, {
			"participantID": 5,
			"firstname": "Participant",
			"surname": "Claire"
		}, {
			"participantID": 6,
			"firstname": "Participant",
			"surname": "Lee"
		}, {
			"participantID": 7,
			"firstname": "Participant",
			"surname": "Sally"
		}, {
			"participantID": 8,
			"firstname": "Participant",
			"surname": "Kalbir"
		}, {
			"participantID": 9,
			"firstname": "Participant",
			"surname": "Alice"
		}, {
			"participantID": 10,
			"firstname": "Anne",
			"surname": "Robinson"
		}, {
			"participantID": 11,
			"firstname": "Diane",
			"surname": "Munday"
		}, {
			"participantID": 12,
			"firstname": "Neena",
			"surname": "Modi"
		}, {
			"participantID": 13,
			"firstname": "David",
			"surname": "Steel"
		}, {
			"participantID": 14,
			"firstname": "Neil",
			"surname": "Lyndon"
		}],
		"locutions": [{
			"nodeID": "3_164926129380455983",
			"personID": 1,
			"start": "2021-11-11 21:50:00",
			"end": null
		}, {
			"nodeID": "16_164926162804546033",
			"personID": "1",
			"start": "2021-11-11 21:50:01",
			"end": null
		}]
	},
	"text": "<span id=\"node3_164926129380455983\" class=\"highlighted\">A</span> because <span id=\"node16_164926162804546033\" class=\"highlighted\">B</span><br>",
	"OVA": {
		"firstname": "Anon",
		"surname": "User",
		"url": "",
		"nodes": [{
			"nodeID": "2_164926129380455983",
			"visible": true,
			"x": 273,
			"y": 140,
			"timestamp": ""
		}, {
			"nodeID": "3_164926129380455983",
			"visible": true,
			"x": 723,
			"y": 140,
			"timestamp": "Thu Nov 11 2021 21:50:00 GMT+0000 (Greenwich Mean Time)"
		}, {
			"nodeID": "4_164926129380455983",
			"visible": false,
			"x": 0,
			"y": 0,
			"timestamp": ""
		}, {
			"nodeID": "5_164926129380455983",
			"visible": false,
			"x": 0,
			"y": 0,
			"timestamp": ""
		}, {
			"nodeID": "6_164926129380455983",
			"visible": true,
			"x": 498,
			"y": 140,
			"timestamp": ""
		}, {
			"nodeID": "15_164926162804546033",
			"visible": true,
			"x": "257",
			"y": "275",
			"timestamp": ""
		}, {
			"nodeID": "16_164926162804546033",
			"visible": true,
			"x": "714",
			"y": "280",
			"timestamp": "Thu Nov 11 2021 21:50:01 GMT+0000 (Greenwich Mean Time)"
		}, {
			"nodeID": "17_164926162804546033",
			"visible": false,
			"x": 0,
			"y": 0,
			"timestamp": ""
		}, {
			"nodeID": "18_164926162804546033",
			"visible": false,
			"x": 0,
			"y": 0,
			"timestamp": ""
		}, {
			"nodeID": "19_164926162804546033",
			"visible": true,
			"x": "464",
			"y": "271",
			"timestamp": ""
		}, {
			"nodeID": "20_164926162804546033",
			"visible": true,
			"x": 717.5,
			"y": 220,
			"timestamp": ""
		}, {
			"nodeID": "21_164926162804546033",
			"visible": true,
			"x": 274.5,
			"y": 218.5,
			"timestamp": ""
		}, {
			"nodeID": "22_164926162804546033",
			"visible": true,
			"x": "464",
			"y": "213",
			"timestamp": ""
		}],
		"edges": [{
			"fromID": "4_164926129380455983",
			"toID": "3_164926129380455983",
			"visible": false
		}, {
			"fromID": "5_164926129380455983",
			"toID": "4_164926129380455983",
			"visible": false
		}, {
			"fromID": "3_164926129380455983",
			"toID": "6_164926129380455983",
			"visible": true
		}, {
			"fromID": "6_164926129380455983",
			"toID": "2_164926129380455983",
			"visible": true
		}, {
			"fromID": "17_164926162804546033",
			"toID": "16_164926162804546033",
			"visible": false
		}, {
			"fromID": "18_164926162804546033",
			"toID": "17_164926162804546033",
			"visible": false
		}, {
			"fromID": "16_164926162804546033",
			"toID": "19_164926162804546033",
			"visible": true
		}, {
			"fromID": "19_164926162804546033",
			"toID": "15_164926162804546033",
			"visible": true
		}, {
			"fromID": "3_164926129380455983",
			"toID": "20_164926162804546033",
			"visible": true
		}, {
			"fromID": "20_164926162804546033",
			"toID": "16_164926162804546033",
			"visible": true
		}, {
			"fromID": "15_164926162804546033",
			"toID": "21_164926162804546033",
			"visible": true
		}, {
			"fromID": "21_164926162804546033",
			"toID": "2_164926129380455983",
			"visible": true
		}, {
			"fromID": "20_164926162804546033",
			"toID": "22_164926162804546033",
			"visible": true
		}, {
			"fromID": "22_164926162804546033",
			"toID": "21_164926162804546033",
			"visible": true
		}]
	}
}

```



### An example with OVA, PropositionClassifier and Skeptic


```json

{
  "AIF": {
    "nodes": [
      {
        "nodeID": "2_166178046893607143",
        "text": "Dungeons and Dragons and its imitators are right out of the pit of hell",
        "type": "I"
      },
      {
        "nodeID": "3_166178046893607143",
        "text": "No Christian or sane, decent individual of whatever faith really should have anything to do with Dungeons and Dragons and its imitators",
        "type": "I"
      },
      {
        "nodeID": "5_166178046893607143",
        "text": "Consequences",
        "type": "RA"
      },
      {
        "nodeID": "6_166178046893607143",
        "text": "It's just a game!",
        "type": "I"
      },
      {
        "nodeID": "7_166178046893607143",
        "text": "the person who thinks they can mess with Dungeons and Dragons without getting burnt is whistling in the dark",
        "type": "I"
      },
      {
        "nodeID": "8_166178046893607143",
        "text": "people who think they can play around with crack or pre-marital sex and not get burned by death, AIDS or pregnancy are whistling in the dark",
        "type": "I"
      },
      {
        "nodeID": "10_166178046893607143",
        "text": "Analogy",
        "type": "RA"
      },
      {
        "nodeID": "12_166178046893607143",
        "text": "Default Conflict",
        "type": "CA"
      },
      {
        "nodeID": "13_166178046893607143",
        "text": "Dungeons and Dragons is essentially a feeding program for occultism and witchcraft",
        "type": "I"
      },
      {
        "nodeID": "15_166178046893607143",
        "text": "Verbal Classification",
        "type": "RA"
      },
      {
        "nodeID": "16_166178046893607143",
        "text": "Dungeons and Dragons violates the commandment of I Ths. 5:22 \"Abstain from all appearance of evil.\"",
        "type": "I"
      },
      {
        "nodeID": "18_166178046893607143",
        "text": "Sign",
        "type": "RA"
      },
      {
        "nodeID": "19_166178046893607143",
        "text": "Much of the art, figurines, and writing within Dungeons and Dragons certainly appears evil to say the least of it",
        "type": "I"
      },
      {
        "nodeID": "21_166178046893607143",
        "text": "Sign",
        "type": "RA"
      },
      {
        "nodeID": "22_166178046893607143",
        "text": "the materials themselves contain magical rituals",
        "type": "I"
      },
      {
        "nodeID": "24_166178046893607143",
        "text": "Sign",
        "type": "RA"
      },
      {
        "nodeID": "25_166178046893607143",
        "text": "for the most part, the rituals are certainly authentic",
        "type": "I"
      },
      {
        "nodeID": "27_166178046893607143",
        "text": "Expert Opinion",
        "type": "RA"
      },
      {
        "nodeID": "29_166178046893607143",
        "text": "Default Conflict",
        "type": "CA"
      },
      {
        "nodeID": "31_166178046893607143",
        "text": "Default Conflict",
        "type": "CA"
      },
      {
        "nodeID": "33_166178046893607143",
        "text": "Default Conflict",
        "type": "CA"
      },
      {
        "nodeID": "34_166178046893607143",
        "text": "If a person \"innocently\" works an authentic ritual that conjures up a demon, or curses someone, thinking that they are only playing a game, the ritual will still have efficacy",
        "type": "I"
      },
      {
        "nodeID": "36_166178046893607143",
        "text": "Correlation To Cause",
        "type": "RA"
      },
      {
        "nodeID": "37_166178046893607143",
        "text": "If you play at shooting your friend in the head with what you think is an unloaded pistol and don't know a shell is in the chamber, your friend is not any less dead because you were playing",
        "type": "I"
      },
      {
        "nodeID": "39_166178046893607143",
        "text": "Analogy",
        "type": "RA"
      }
    ],
    "edges": [
      {
        "edgeID": 1,
        "fromID": "2_166178046893607143",
        "toID": "5_166178046893607143"
      },
      {
        "edgeID": 2,
        "fromID": "5_166178046893607143",
        "toID": "3_166178046893607143"
      },
      {
        "edgeID": 3,
        "fromID": "8_166178046893607143",
        "toID": "10_166178046893607143"
      },
      {
        "edgeID": 4,
        "fromID": "10_166178046893607143",
        "toID": "7_166178046893607143"
      },
      {
        "edgeID": 5,
        "fromID": "7_166178046893607143",
        "toID": "12_166178046893607143"
      },
      {
        "edgeID": 6,
        "fromID": "12_166178046893607143",
        "toID": "6_166178046893607143"
      },
      {
        "edgeID": 7,
        "fromID": "13_166178046893607143",
        "toID": "15_166178046893607143"
      },
      {
        "edgeID": 8,
        "fromID": "15_166178046893607143",
        "toID": "2_166178046893607143"
      },
      {
        "edgeID": 9,
        "fromID": "16_166178046893607143",
        "toID": "18_166178046893607143"
      },
      {
        "edgeID": 10,
        "fromID": "18_166178046893607143",
        "toID": "13_166178046893607143"
      },
      {
        "edgeID": 11,
        "fromID": "19_166178046893607143",
        "toID": "21_166178046893607143"
      },
      {
        "edgeID": 12,
        "fromID": "21_166178046893607143",
        "toID": "16_166178046893607143"
      },
      {
        "edgeID": 13,
        "fromID": "22_166178046893607143",
        "toID": "24_166178046893607143"
      },
      {
        "edgeID": 14,
        "fromID": "24_166178046893607143",
        "toID": "13_166178046893607143"
      },
      {
        "edgeID": 15,
        "fromID": "25_166178046893607143",
        "toID": "27_166178046893607143"
      },
      {
        "edgeID": 16,
        "fromID": "27_166178046893607143",
        "toID": "22_166178046893607143"
      },
      {
        "edgeID": 17,
        "fromID": "6_166178046893607143",
        "toID": "29_166178046893607143"
      },
      {
        "edgeID": 18,
        "fromID": "29_166178046893607143",
        "toID": "3_166178046893607143"
      },
      {
        "edgeID": 19,
        "fromID": "6_166178046893607143",
        "toID": "31_166178046893607143"
      },
      {
        "edgeID": 20,
        "fromID": "31_166178046893607143",
        "toID": "2_166178046893607143"
      },
      {
        "edgeID": 21,
        "fromID": "6_166178046893607143",
        "toID": "33_166178046893607143"
      },
      {
        "edgeID": 22,
        "fromID": "33_166178046893607143",
        "toID": "13_166178046893607143"
      },
      {
        "edgeID": 23,
        "fromID": "34_166178046893607143",
        "toID": "36_166178046893607143"
      },
      {
        "edgeID": 24,
        "fromID": "36_166178046893607143",
        "toID": "25_166178046893607143"
      },
      {
        "edgeID": 25,
        "fromID": "37_166178046893607143",
        "toID": "39_166178046893607143"
      },
      {
        "edgeID": 26,
        "fromID": "39_166178046893607143",
        "toID": "34_166178046893607143"
      }
    ],
    "schemefulfillments": [
      {
        "nodeID": "2_166178046893607143",
        "schemeID": "0"
      },
      {
        "nodeID": "3_166178046893607143",
        "schemeID": "0"
      },
      {
        "nodeID": "5_166178046893607143",
        "schemeID": "237"
      },
      {
        "nodeID": "6_166178046893607143",
        "schemeID": "0"
      },
      {
        "nodeID": "7_166178046893607143",
        "schemeID": "0"
      },
      {
        "nodeID": "8_166178046893607143",
        "schemeID": "0"
      },
      {
        "nodeID": "10_166178046893607143",
        "schemeID": "1"
      },
      {
        "nodeID": "12_166178046893607143",
        "schemeID": "71"
      },
      {
        "nodeID": "13_166178046893607143",
        "schemeID": "0"
      },
      {
        "nodeID": "15_166178046893607143",
        "schemeID": "31"
      },
      {
        "nodeID": "16_166178046893607143",
        "schemeID": "0"
      },
      {
        "nodeID": "18_166178046893607143",
        "schemeID": "30"
      },
      {
        "nodeID": "19_166178046893607143",
        "schemeID": "0"
      },
      {
        "nodeID": "21_166178046893607143",
        "schemeID": "30"
      },
      {
        "nodeID": "22_166178046893607143",
        "schemeID": "0"
      },
      {
        "nodeID": "24_166178046893607143",
        "schemeID": "30"
      },
      {
        "nodeID": "25_166178046893607143",
        "schemeID": "0"
      },
      {
        "nodeID": "27_166178046893607143",
        "schemeID": "15"
      },
      {
        "nodeID": "29_166178046893607143",
        "schemeID": "71"
      },
      {
        "nodeID": "31_166178046893607143",
        "schemeID": "71"
      },
      {
        "nodeID": "33_166178046893607143",
        "schemeID": "71"
      },
      {
        "nodeID": "34_166178046893607143",
        "schemeID": "0"
      },
      {
        "nodeID": "36_166178046893607143",
        "schemeID": "7"
      },
      {
        "nodeID": "37_166178046893607143",
        "schemeID": "0"
      },
      {
        "nodeID": "39_166178046893607143",
        "schemeID": "1"
      }
    ],
    "participants": [
      {
        "participantID": 1,
        "firstname": "Participant",
        "surname": "Rachel"
      },
      {
        "participantID": 2,
        "firstname": "Participant",
        "surname": "Carolyn"
      },
      {
        "participantID": 3,
        "firstname": "Participant",
        "surname": "Mo"
      },
      {
        "participantID": 4,
        "firstname": "Participant",
        "surname": "Zoe"
      },
      {
        "participantID": 5,
        "firstname": "Participant",
        "surname": "Claire"
      },
      {
        "participantID": 6,
        "firstname": "Participant",
        "surname": "Lee"
      },
      {
        "participantID": 7,
        "firstname": "Participant",
        "surname": "Sally"
      },
      {
        "participantID": 8,
        "firstname": "Participant",
        "surname": "Kalbir"
      },
      {
        "participantID": 9,
        "firstname": "Participant",
        "surname": "Alice"
      },
      {
        "participantID": 10,
        "firstname": "Anne",
        "surname": "Robinson"
      },
      {
        "participantID": 11,
        "firstname": "Diane",
        "surname": "Munday"
      },
      {
        "participantID": 12,
        "firstname": "Neena",
        "surname": "Modi"
      },
      {
        "participantID": 13,
        "firstname": "David",
        "surname": "Steel"
      },
      {
        "participantID": 14,
        "firstname": "Neil",
        "surname": "Lyndon"
      }
    ],
    "locutions": [],
    "descriptorfulfillments": [],
    "cqdescriptorfulfillments": []
  },
  "text": "Dungeons and Dragons is essentially a feeding program for occultism and witchcraft. For Christians, the first scriptural problem is the fact that Dungeons and Dragons violates the commandment of I Ths. 5:22 \"Abstain from all appearance of evil.\" Much of the art, figurines, and writing within Dungeons and Dragons certainly appears evil to say the least of it.

On top of that, the second issue is that the materials themselves contain magical rituals. From my own experience as a witch high priest (Alexandrian tradition) during the period 1973-84, I can tell you that, for the most part, the rituals are certainly authentic.

If a person \"innocently\" works an authentic ritual that conjures up a demon, or curses someone, thinking that they are only playing a game, the ritual will still have efficacy. If you play at shooting your friend in the head with what you think is an unloaded pistol and don't know a shell is in the chamber, is your friend any less dead because you were playing? 

Of course, some people will say: \"It's just a game!\" But like the people who think they can play around with crack or pre-marital sex and not get burned by death, AIDS or pregnancy, the person who thinks they can mess with Dungeons and Dragons without getting burnt is whistling in the dark.

Thus, in my mind, there is no doubt that Dungeons and Dragons and its imitators are right out of the pit of hell. No Christian or sane, decent individual of whatever faith really should have anything to do with them.
",
  "OVA": {
    "firstname": "Jacky",
    "surname": "Visser",
    "url": "",
    "nodes": [
      {
        "nodeID": "2_166178046893607143",
        "visible": true,
        "x": 192,
        "y": 175,
        "timestamp": ""
      },
      {
        "nodeID": "3_166178046893607143",
        "visible": true,
        "x": 190,
        "y": 7,
        "timestamp": ""
      },
      {
        "nodeID": "5_166178046893607143",
        "visible": true,
        "x": 235,
        "y": 132,
        "timestamp": ""
      },
      {
        "nodeID": "6_166178046893607143",
        "visible": true,
        "x": 614,
        "y": 200,
        "timestamp": ""
      },
      {
        "nodeID": "7_166178046893607143",
        "visible": true,
        "x": 581,
        "y": 311,
        "timestamp": ""
      },
      {
        "nodeID": "8_166178046893607143",
        "visible": true,
        "x": 582,
        "y": 479,
        "timestamp": ""
      },
      {
        "nodeID": "10_166178046893607143",
        "visible": true,
        "x": 638,
        "y": 422,
        "timestamp": ""
      },
      {
        "nodeID": "12_166178046893607143",
        "visible": true,
        "x": 617,
        "y": 257,
        "timestamp": ""
      },
      {
        "nodeID": "13_166178046893607143",
        "visible": true,
        "x": 192,
        "y": 311,
        "timestamp": ""
      },
      {
        "nodeID": "15_166178046893607143",
        "visible": true,
        "x": 234,
        "y": 264,
        "timestamp": ""
      },
      {
        "nodeID": "16_166178046893607143",
        "visible": true,
        "x": 84,
        "y": 465,
        "timestamp": ""
      },
      {
        "nodeID": "18_166178046893607143",
        "visible": true,
        "x": 210,
        "y": 404,
        "timestamp": ""
      },
      {
        "nodeID": "19_166178046893607143",
        "visible": true,
        "x": 84,
        "y": 616,
        "timestamp": ""
      },
      {
        "nodeID": "21_166178046893607143",
        "visible": true,
        "x": 161,
        "y": 569,
        "timestamp": ""
      },
      {
        "nodeID": "22_166178046893607143",
        "visible": true,
        "x": 321,
        "y": 464,
        "timestamp": ""
      },
      {
        "nodeID": "24_166178046893607143",
        "visible": true,
        "x": 332,
        "y": 402,
        "timestamp": ""
      },
      {
        "nodeID": "25_166178046893607143",
        "visible": true,
        "x": 325,
        "y": 579,
        "timestamp": ""
      },
      {
        "nodeID": "27_166178046893607143",
        "visible": true,
        "x": 367,
        "y": 532,
        "timestamp": ""
      },
      {
        "nodeID": "29_166178046893607143",
        "visible": true,
        "x": 425,
        "y": 52,
        "timestamp": ""
      },
      {
        "nodeID": "31_166178046893607143",
        "visible": true,
        "x": 423,
        "y": 195,
        "timestamp": ""
      },
      {
        "nodeID": "33_166178046893607143",
        "visible": true,
        "x": 421,
        "y": 321,
        "timestamp": ""
      },
      {
        "nodeID": "34_166178046893607143",
        "visible": true,
        "x": 327,
        "y": 694,
        "timestamp": ""
      },
      {
        "nodeID": "36_166178046893607143",
        "visible": true,
        "x": 363,
        "y": 647,
        "timestamp": ""
      },
      {
        "nodeID": "37_166178046893607143",
        "visible": true,
        "x": 327,
        "y": 866,
        "timestamp": ""
      },
      {
        "nodeID": "39_166178046893607143",
        "visible": true,
        "x": 392,
        "y": 820,
        "timestamp": ""
      }
    ],
    "edges": [
      {
        "fromID": "2_166178046893607143",
        "toID": "5_166178046893607143",
        "visible": true
      },
      {
        "fromID": "5_166178046893607143",
        "toID": "3_166178046893607143",
        "visible": true
      },
      {
        "fromID": "8_166178046893607143",
        "toID": "10_166178046893607143",
        "visible": true
      },
      {
        "fromID": "10_166178046893607143",
        "toID": "7_166178046893607143",
        "visible": true
      },
      {
        "fromID": "7_166178046893607143",
        "toID": "12_166178046893607143",
        "visible": true
      },
      {
        "fromID": "12_166178046893607143",
        "toID": "6_166178046893607143",
        "visible": true
      },
      {
        "fromID": "13_166178046893607143",
        "toID": "15_166178046893607143",
        "visible": true
      },
      {
        "fromID": "15_166178046893607143",
        "toID": "2_166178046893607143",
        "visible": true
      },
      {
        "fromID": "16_166178046893607143",
        "toID": "18_166178046893607143",
        "visible": true
      },
      {
        "fromID": "18_166178046893607143",
        "toID": "13_166178046893607143",
        "visible": true
      },
      {
        "fromID": "19_166178046893607143",
        "toID": "21_166178046893607143",
        "visible": true
      },
      {
        "fromID": "21_166178046893607143",
        "toID": "16_166178046893607143",
        "visible": true
      },
      {
        "fromID": "22_166178046893607143",
        "toID": "24_166178046893607143",
        "visible": true
      },
      {
        "fromID": "24_166178046893607143",
        "toID": "13_166178046893607143",
        "visible": true
      },
      {
        "fromID": "25_166178046893607143",
        "toID": "27_166178046893607143",
        "visible": true
      },
      {
        "fromID": "27_166178046893607143",
        "toID": "22_166178046893607143",
        "visible": true
      },
      {
        "fromID": "6_166178046893607143",
        "toID": "29_166178046893607143",
        "visible": true
      },
      {
        "fromID": "29_166178046893607143",
        "toID": "3_166178046893607143",
        "visible": true
      },
      {
        "fromID": "6_166178046893607143",
        "toID": "31_166178046893607143",
        "visible": true
      },
      {
        "fromID": "31_166178046893607143",
        "toID": "2_166178046893607143",
        "visible": true
      },
      {
        "fromID": "6_166178046893607143",
        "toID": "33_166178046893607143",
        "visible": true
      },
      {
        "fromID": "33_166178046893607143",
        "toID": "13_166178046893607143",
        "visible": true
      },
      {
        "fromID": "34_166178046893607143",
        "toID": "36_166178046893607143",
        "visible": true
      },
      {
        "fromID": "36_166178046893607143",
        "toID": "25_166178046893607143",
        "visible": true
      },
      {
        "fromID": "37_166178046893607143",
        "toID": "39_166178046893607143",
        "visible": true
      },
      {
        "fromID": "39_166178046893607143",
        "toID": "34_166178046893607143",
        "visible": true
      }
    ]
  },
  "propositionClassifier": {
    "nodes": [
      {
        "nodeID": "2_166178046893607143",
        "propType": "value"
      },
      {
        "nodeID": "3_166178046893607143",
        "propType": "policy"
      },
      {
        "nodeID": "6_166178046893607143",
        "propType": "fact"
      },
      {
        "nodeID": "7_166178046893607143",
        "propType": "value"
      },
      {
        "nodeID": "8_166178046893607143",
        "propType": "value"
      },
      {
        "nodeID": "13_166178046893607143",
        "propType": "fact"
      },
      {
        "nodeID": "16_166178046893607143",
        "propType": "value"
      },
      {
        "nodeID": "19_166178046893607143",
        "propType": "value"
      },
      {
        "nodeID": "22_166178046893607143",
        "propType": "fact"
      },
      {
        "nodeID": "25_166178046893607143",
        "propType": "fact"
      },
      {
        "nodeID": "34_166178046893607143",
        "propType": "fact"
      },
      {
        "nodeID": "37_166178046893607143",
        "propType": "fact"
      }
    ]
  },
  "Skeptic": {
    "questions": [
      {
        "rank": 1,
        "nodeID": "3_166178046893607143",
        "question": "Is this statement consistent with previous proposals?"
      },
      {
        "rank": 2,
        "nodeID": "3_166178046893607143",
        "question": "Is this policy appropriate for this objective?"
      },
      {
        "rank": 3,
        "nodeID": "5_166178046893607143",
        "question": "How strong is the probability or plausibility that these cited consequences will (may, might, must) occur?"
      },
      {
        "rank": 4,
        "nodeID": "5_166178046893607143",
        "question": "What evidence, if any, supported the claim that these consequences will (may, might, must) occur if the action is brought about?"
      },
      {
        "rank": 5,
        "nodeID": "5_166178046893607143",
        "question": "Are there consequences of the opposite value that ought to be taken into account?"
      },
      {
        "rank": 6,
        "nodeID": "2_166178046893607143",
        "question": "Does this statement reflect a popularly held value?"
      },
      {
        "rank": 7,
        "nodeID": "15_166178046893607143",
        "question": "What evidence is there that this thing definitely has the property, as opposed to evidence indicating room for doubt on whether it should be so classified?"
      },
      {
        "rank": 8,
        "nodeID": "15_166178046893607143",
        "question": "Is the verbal classification in the classification premise based merely on a stipulative or biased definition that is subject to doubt?"
      },
      {
        "rank": 9,
        "nodeID": "13_166178046893607143",
        "question": "Is this statement actually true?"
      },
      {
        "rank": 10,
        "nodeID": "18_166178046893607143",
        "question": "What is the strength of the correlation of the sign with the event signified?"
      },
      {
        "rank": 11,
        "nodeID": "18_166178046893607143",
        "question": "Are there other events that would more reliably account for the sign?"
      },
      {
        "rank": 12,
        "nodeID": "24_166178046893607143",
        "question": "What is the strength of the correlation of the sign with the event signified?"
      },
      {
        "rank": 13,
        "nodeID": "24_166178046893607143",
        "question": "Are there other events that would more reliably account for the sign?"
      },
      {
        "rank": 14,
        "nodeID": "22_166178046893607143",
        "question": "Is this statement actually true?"
      },
      {
        "rank": 15,
        "nodeID": "27_166178046893607143",
        "question": "How credible is the source as an expert?"
      },
      {
        "rank": 16,
        "nodeID": "27_166178046893607143",
        "question": "Is the source an expert in a relevant field?"
      },
      {
        "rank": 17,
        "nodeID": "27_166178046893607143",
        "question": "What did the source assert that implies this claim?"
      },
      {
        "rank": 18,
        "nodeID": "27_166178046893607143",
        "question": "Is the source personally reliable?"
      },
      {
        "rank": 19,
        "nodeID": "27_166178046893607143",
        "question": "Is the claim consistent with what other experts assert?"
      },
      {
        "rank": 20,
        "nodeID": "27_166178046893607143",
        "question": "Is the source’s assertion based on evidence?"
      },
      {
        "rank": 21,
        "nodeID": "6_166178046893607143",
        "question": "Is this statement actually true?"
      },
      {
        "rank": 22,
        "nodeID": "6_166178046893607143",
        "question": "Could there be any reasons for accepting this proposition?"
      },
      {
        "rank": 23,
        "nodeID": "6_166178046893607143",
        "question": "Is there any argument in support of this claim?"
      },
      {
        "rank": 24,
        "nodeID": "25_166178046893607143",
        "question": "Is this statement actually true?"
      },
      {
        "rank": 25,
        "nodeID": "36_166178046893607143",
        "question": "Is there really a correlation between the two states of affairs?"
      },
      {
        "rank": 26,
        "nodeID": "36_166178046893607143",
        "question": "Is there any reason to think that the correlation is any more than a coincidence?"
      },
      {
        "rank": 27,
        "nodeID": "36_166178046893607143",
        "question": "Could there be some third factor that is causing both states of affairs?"
      },
      {
        "rank": 28,
        "nodeID": "7_166178046893607143",
        "question": "Does this statement reflect a popularly held value?"
      },
      {
        "rank": 29,
        "nodeID": "10_166178046893607143",
        "question": "Are there differences between the compared cases that would tend to undermine the force of the similarity cited?"
      },
      {
        "rank": 30,
        "nodeID": "10_166178046893607143",
        "question": "Is the property true or false in the first compared case?"
      },
      {
        "rank": 31,
        "nodeID": "10_166178046893607143",
        "question": "Is there some other comparable case that is also similar to the first case, but in which the property is not true (false)?"
      },
      {
        "rank": 32,
        "nodeID": "16_166178046893607143",
        "question": "Does this statement reflect a popularly held value?"
      },
      {
        "rank": 33,
        "nodeID": "21_166178046893607143",
        "question": "What is the strength of the correlation of the sign with the event signified?"
      },
      {
        "rank": 34,
        "nodeID": "21_166178046893607143",
        "question": "Are there other events that would more reliably account for the sign?"
      },
      {
        "rank": 35,
        "nodeID": "34_166178046893607143",
        "question": "Is this statement actually true?"
      },
      {
        "rank": 36,
        "nodeID": "39_166178046893607143",
        "question": "Are there differences between the compared cases that would tend to undermine the force of the similarity cited?"
      },
      {
        "rank": 37,
        "nodeID": "39_166178046893607143",
        "question": "Is the property true or false in the first compared case?"
      },
      {
        "rank": 38,
        "nodeID": "39_166178046893607143",
        "question": "Is there some other comparable case that is also similar to the first case, but in which the property is not true (false)?"
      },
      {
        "rank": 39,
        "nodeID": "8_166178046893607143",
        "question": "Does this statement reflect a popularly held value?"
      },
      {
        "rank": 40,
        "nodeID": "19_166178046893607143",
        "question": "Does this statement reflect a popularly held value?"
      },
      {
        "rank": 41,
        "nodeID": "37_166178046893607143",
        "question": "Is this statement actually true?"
      }
    ]
  }
}

```

## xaif library

`xaif` is a Python library for working with Argument Interchange Format (AIF), primarily designed to facilitate the development, manipulation, and evaluation of argumentat structures. This package provides essential utilities to validate, traverse, and manipulate AIF-compliant JSON structures, enabling users to effectively work with complex argumentation data.

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
xaif_data= {
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
# Here, 'xaif_data' is expected to be a valid xAIF structure in JSON format
aif = AIF(xaif_data)

# Alternatively, initialize the AIF object with raw text data.
# The AIF object will automatically create locutions and other necessary components from the provided text.
aif = AIF("First Sentence.")

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

# Exporting the data: #
# To export the argument relations in CSV format, use the get_csv method with "argument-relation" as the argument.
print(aif.get_csv("argument-relation"))  # Exports proposition pairs with argument relations in tabular (CSV) format.

# To export the locution data in CSV format, use the get_csv method with "locution" as the argument.
print(aif.get_csv("locution"))  # Exports locution data in tabular (CSV) format.



```