# American College of Technology
# Department of Computer Science (MSc)
# Advanced Database Assignment
# Submitted to: Natnael Argaw (PhD)
# Submitted by: Abel Getahun - 035/RMSC_B7/2023

class HorizontalMinitermFragmentGenerator:
    def __init__(self, relations):
        self.relations = relations

    def generate_fragments(self, predicates):
        fragments = []
        for predicate in predicates:
            for relation in self.relations:
                fragment = f"SELECT * FROM {relation} WHERE {predicate};"
                fragments.append(fragment)
        return fragments

# Example usage:
relations = ["table1", "table2", "table3"]
predicates = ["age > 30", "salary <= 50000", "department = 'IT'"]
generator = HorizontalMinitermFragmentGenerator(relations)
fragments = generator.generate_fragments(predicates)
for fragment in fragments:
    print(fragment)

