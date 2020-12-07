from utils import read_lines
from queue import Queue
import re

container_regex = re.compile(r"(?P<bag_type>\w* \w*) bags")
contents_regex = re.compile(r"(?P<num>\d*) (?P<bag_type>\w* \w*) bags?")

d = {}
d2 = {}

for line in read_lines(7):
	pieces = line.split(" contain ")
	container = container_regex.match(pieces[0])
	contents = contents_regex.findall(pieces[1])

	container_key = container.group("bag_type")
	if container_key not in d2:
		d2[container_key] = {}

	for entry in contents:
		key = entry[1]
		d2[container_key][key] = entry[0]
		if key not in d:
			d[key] = []
		d[key].append(container.group("bag_type"))

outer_bag_types = set()

q = Queue()
q.put("shiny gold")

while not q.empty():
	current = q.get()
	for parent_bag in d.get(current, []):
		outer_bag_types.add(parent_bag)
		q.put(parent_bag)

print(len(outer_bag_types))

num_of_inner_bags = 0

q = Queue()
q.put("shiny gold")
while not q.empty():
	current = q.get()
	for bag_type, num in d2.get(current, {}).items():
		num_of_inner_bags += int(num)
		for i in range(int(num)):
			q.put(bag_type)

print(num_of_inner_bags)