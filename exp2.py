
import json

# EXPERIMENT 2: KNOWLEDGE RESOLUTION
# KANISHKA CHAUDHARY 08701012023

# STEP 1: LOAD KNOWLEDGE BASE FROM EXPERIMENT 1

with open("urban_traffic_knowledge_base.json", "r") as file:
    kb = json.load(file)["knowledge_base"]


# STEP 2: DEFINE CURRENT FACTS

facts = {
    "traffic_level": "severe",
    "accident_severity": "critical",
    "road_blocked": True,
    "weather_condition": "fog",
    "public_transport_delay": 20
}


# STEP 3: KNOWLEDGE RESOLUTION / INFERENCE ENGINE

def resolve_knowledge(facts, kb):

    decisions = []

    # Rule 1: Severe traffic
    if facts["traffic_level"] == "severe":
        decision = (
            "Increase green signal duration "
            "for the congested direction."
        )

        decisions.append({
            "rule": "R1",
            "fact": "traffic_level = severe",
            "decision": decision
        })

    # Rule 2: Critical accident
    if facts["accident_severity"] == "critical":
        decision = "Dispatch nearest emergency services immediately."

        decisions.append({
            "rule": "R2",
            "fact": "accident_severity = critical",
            "decision": decision
        })

    # Rule 3: Road blocked
    if facts["road_blocked"]:
        decision = "Recommend alternative routes to drivers."

        decisions.append({
            "rule": "R3",
            "fact": "road_blocked = True",
            "decision": decision
        })

    # Rule 4: Fog
    if facts["weather_condition"] == "fog":
        decision = (
            "Reduce recommended vehicle speed "
            "because of low visibility."
        )

        decisions.append({
            "rule": "R4",
            "fact": "weather_condition = fog",
            "decision": decision
        })

    # Rule 5: High traffic
    if facts["traffic_level"] == "high":
        decision = "Advise drivers to consider alternative routes."

        decisions.append({
            "rule": "R5",
            "fact": "traffic_level = high",
            "decision": decision
        })

    # Rule 6: Public transport delay > 15 minutes
    if facts["public_transport_delay"] > 15:
        decision = "Investigate the cause of public transport delay."

        decisions.append({
            "rule": "R6",
            "fact": f"public_transport_delay = {facts['public_transport_delay']} minutes",
            "decision": decision
        })

    return decisions


# STEP 4: PERFORM KNOWLEDGE RESOLUTION

resolved_decisions = resolve_knowledge(facts, kb)


# STEP 5: DISPLAY INPUT FACTS

print("=" * 70)
print("         KNOWLEDGE RESOLUTION AND DECISION MAKING")
print("=" * 70)

print("\nINPUT FACTS:")
print("Traffic Level:", facts["traffic_level"])
print("Accident Severity:", facts["accident_severity"])
print("Road Blocked:", facts["road_blocked"])
print("Weather Condition:", facts["weather_condition"])
print(f"Public Transport Delay: {facts['public_transport_delay']} minutes")


# STEP 6: DISPLAY RESOLUTION PROCESS

print("\nRESOLUTION PROCESS:")

for result in resolved_decisions:
    print(f"\nRule: {result['rule']}")
    print(f"Given Fact: {result['fact']}")
    print("Therefore:")
    print(f"    -> {result['decision']}")


# STEP 7: DISPLAY FINAL INSTANTIATED DECISIONS

print("\n" + "=" * 70)
print("         FINAL INSTANTIATED DECISIONS")
print("=" * 70)

for i, result in enumerate(resolved_decisions, 1):
    print(f"{i}. {result['decision']}")

print(f"\nTotal decisions derived: {len(resolved_decisions)}")

print("=" * 70)

