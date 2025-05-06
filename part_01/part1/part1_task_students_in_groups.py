# Programming exercise
# Students in groups

studants = int(input("How many students on the course? "))
groups_size = int(input("Desired group size? "))

groups_formed = studants // groups_size

if studants % groups_size != 0:
    groups_formed = groups_formed + 1

print(f"Number of groups formed: {groups_formed}")

# Model solution is much better:
# students = int(input("How many students on the course? "))
#
# group_size = int(input("Desired group size? "))
#
# groups = (students + group_size - 1) // group_size
#
# print("Number of groups formed:", groups)
