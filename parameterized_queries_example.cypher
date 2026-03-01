
// Example of how to use these parameterized queries:

// 1. First, create indexes
CREATE INDEX ON :Category(name);
CREATE INDEX ON :Architecture(name);

// 2. Then create categories with parameters:
// Parameters: {
//   "categories": [
    {
        "name": "FeedForward",
        "count": 129
    },
    {
        "name": "CNN",
        "count": 47
    },
    {
        "name": "GNN",
        "count": 50
    },
    {
        "name": "TransformersAndAttention",
        "count": 151
    },
    {
        "name": "Generative",
        "count": 62
    },
    {
        "name": "NAS",
        "count": 50
    },
    {
        "name": "Multimodal",
        "count": 70
    },
    {
        "name": "EnergyAndEquilibriaum",
        "count": 51
    },
    {
        "name": "EfficientAndMobile",
        "count": 58
    },
    {
        "name": "RecAndSeq",
        "count": 51
    },
    {
        "name": "RL",
        "count": 50
    },
    {
        "name": "StateSpace",
        "count": 69
    },
    {
        "name": "SmallDataAndFewShot",
        "count": 70
    },
    {
        "name": "Specialized",
        "count": 72
    },
    {
        "name": "SpikeAndNeuromorph",
        "count": 73
    },
    {
        "name": "NeuroSymbolicAndHybrid",
        "count": 70
    },
    {
        "name": "NeuralODEsAndContin",
        "count": 72
    }
]
// }
UNWIND $categories AS cat_data
MERGE (c:Category {name: cat_data.name})
SET c.type = 'category_group',
    c.architecture_count = cat_data.count;

// 3. Then create architectures for each category with parameters:
// For each category, you would run:
// Parameters: {
//   "category_name": "FeedForward",
//   "architectures": [/* array of architecture objects */]
// }
MATCH (c:Category {name: $category_name})
UNWIND $architectures AS arch_data
MERGE (a:Architecture {name: arch_data.name})
SET a.description = arch_data.description,
    a.category = $category_name
WITH a, c
MERGE (a)-[:BELONGS_TO]->(c);
