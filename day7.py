from utils import read_lines
from collections import defaultdict
import re

container_regex = re.compile(r"(?P<bag_type>\w* \w*) bags")
contents_regex = re.compile(r"(?P<num>\d*) (?P<bag_type>\w* \w*) bags?")

child_to_parent = defaultdict(list)
parent_to_child = defaultdict(dict)

for line in read_lines(7):
	pieces = line.split(" contain ")
	container_bag_type = container_regex.match(pieces[0]).group("bag_type")

	for entry in contents_regex.findall(pieces[1]):
		child_bag_type = entry[1]
		parent_to_child[container_bag_type][child_bag_type] = int(entry[0])
		child_to_parent[child_bag_type].append(container_bag_type)

outer_bag_types = set()
q = ["shiny gold"]
while len(q) > 0:
	current = q.pop()
	for parent_bag in child_to_parent[current]:
		outer_bag_types.add(parent_bag)
		q.append(parent_bag)

print(len(outer_bag_types))

num_of_inner_bags = 0
q = ["shiny gold"]
while len(q) > 0:
	current = q.pop()
	for bag_type, num in parent_to_child[current].items():
		num_of_inner_bags += num
		for i in range(num):
			q.append(bag_type)

print(num_of_inner_bags)
