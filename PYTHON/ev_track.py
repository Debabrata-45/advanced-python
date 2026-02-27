events = set()

n = int(input("Enter number of events: "))

for _ in range(n):
    events.add(input("Enter event name: "))

print("\nEvents:")
for i, event in enumerate(events, 1):
    print(f"{i}. {event}")
