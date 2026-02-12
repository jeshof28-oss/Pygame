records = []

for i in range(2):
    print("\nEnter details for Group {}:".format(i+1))
    
    group_name = input("Enter group name: ")
    group_size = int(input("Enter size of the group: "))
    date_of_competition = input("Enter date of the competition: ")
    venue = input("Enter venue: ")
    medal_type = input("Enter type of medal: ")

    record = (group_name, group_size, date_of_competition, venue, medal_type)
    records.append(record)

print("\n"+"All Group Records:")
for index, record in enumerate(records):
    print(f"Group {index}: \n{record}")