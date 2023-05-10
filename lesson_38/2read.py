from main import Project
from session import session

search = session.query(Project).filter(Project.name.ilike("2%"))
search2 = session.query(Project).filter(Project.price > 1000)
search3 = session.query(Project).filter(Project.price > 1000, Project.name.ilike("2%"))

print([i for i in search])
print([i for i in search2])
print([i for i in search3])

# [2 2 projektas - 55000.0: 2021-02-03 14:29:33.477232]
# [1 Naujas pr. - 20000.0: 2021-02-03 14:29:33.437231, 2 2 projektas - 55000.0: 2021-02-03 14:29:33.477232]
# [2 2 projektas - 55000.0: 2021-02-03 14:29:33.477232]

price_sum = 0

for project in search2:
    price_sum += project.price

print(price_sum)

