Data_item = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
u_values = set(val for dic in Data_item for val in dic.values())
print(u_values)
