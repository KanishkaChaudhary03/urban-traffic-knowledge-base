
import json

# EXPERIMENT 1: KNOWLEDGE BASE
# KANISHKA CHAUDHARY 08701012023

# DOMAIN: URBAN TRAFFIC MANAGEMENT

knowledge_base = {
    "knowledge_base": {
        "domain": "Urban Traffic Management",

        # 1. ENTITIES
        "entities": {
            "vehicles": {
                "types": [
                    "car", "bus", "truck", "motorcycle",
                    "ambulance", "fire_truck", "police_vehicle"
                ]
            },

            "roads": {
                "traffic_levels": [
                    "low", "moderate", "high", "severe"
                ]
            },

            "traffic_signals": {
                "states": ["red", "yellow", "green"]
            },

            "accidents": {
                "severity_levels": [
                    "minor", "moderate", "major", "critical"
                ]
            },

            "weather": {
                "conditions": [
                    "clear", "rain", "fog", "storm", "snow"
                ]
            },

            "public_transport": {
                "types": ["bus", "metro", "tram"]
            },

            "emergency_services": {
                "types": ["ambulance", "police", "fire_department"]
            }
        },

        # 2. RELATIONSHIPS
        "relationships": [
            {"subject": "vehicle", "relationship": "travels_on", "object": "road"},
            {"subject": "road", "relationship": "controlled_by", "object": "traffic_signal"},
            {"subject": "accident", "relationship": "occurs_on", "object": "road"},
            {"subject": "accident", "relationship": "blocks", "object": "road"},
            {"subject": "weather", "relationship": "affects", "object": "road"},
            {"subject": "weather", "relationship": "affects", "object": "vehicle_speed"},
            {"subject": "public_transport", "relationship": "travels_on", "object": "road"},
            {"subject": "emergency_service", "relationship": "responds_to", "object": "accident"}
        ],

        # 3. RULES
        "rules": [
            {
                "condition": "traffic is severe",
                "conclusion": "optimize traffic signal timing"
            },
            {
                "condition": "accident severity is critical",
                "conclusion": "dispatch emergency services immediately"
            },
            {
                "condition": "road is blocked",
                "conclusion": "recommend alternative routes"
            },
            {
                "condition": "weather condition is fog",
                "conclusion": "reduce recommended vehicle speed"
            },
            {
                "condition": "traffic is high",
                "conclusion": "suggest alternative routes"
            },
            {
                "condition": "public transport delay is more than 15 minutes",
                "conclusion": "investigate the cause of delay"
            }
        ],

        # 4. PROBLEMS
        "problems": [
            "Traffic congestion",
            "Road accidents",
            "Long emergency response times",
            "Traffic signal inefficiency",
            "Public transport delays",
            "Poor weather conditions",
            "Road blockages",
            "High fuel consumption",
            "Air pollution"
        ],

        # 5. SOLUTIONS
        "solutions": [
            "Adaptive traffic signal control",
            "Real-time traffic monitoring",
            "Accident detection systems",
            "Dynamic route recommendations",
            "Emergency vehicle priority",
            "Public transport optimization",
            "Weather-based traffic control",
            "AI-based traffic prediction"
        ]
    }
}

# SAVE KNOWLEDGE BASE AS JSON
with open("urban_traffic_knowledge_base.json", "w") as file:
    json.dump(knowledge_base, file, indent=4)

# RETRIEVE KNOWLEDGE BASE
kb = knowledge_base["knowledge_base"]

print("=" * 60)
print("URBAN TRAFFIC MANAGEMENT KNOWLEDGE BASE")
print("=" * 60)

# Display entities
print("\nEntities:", ", ".join(kb["entities"].keys()))

for entity, details in kb["entities"].items():
    for key, values in details.items():
        print(f"{entity} {key}: {', '.join(values)}")

# Display relationships
print("\nRelationships:")
for r in kb["relationships"]:
    print(r["subject"], r["relationship"], r["object"])

# Display rules
print("\nRules:")
for i, rule in enumerate(kb["rules"], 1):
    print(f"{i}. IF {rule['condition']} THEN {rule['conclusion']}")

# Display problems
print("\nProblems:", ", ".join(kb["problems"]))

# Display solutions
print("\nSolutions:", ", ".join(kb["solutions"]))

print("\nKnowledge Base successfully created and saved as JSON.")
print("=" * 60)


