# Simple Python Program for Resolution Theorem

def resolve(ci, cj):
    for x in ci:
        for y in cj:
            if x == '' + y or y == '' + x:
                return (ci - {x}) | (cj - {y})
    return None

def resolution(kb, query):
    kb.append(set(['~' + query]))
    while True:
        new = []
        for i in range(len(kb)):
            for j in range(i + 1, len(kb)):
                resolvent = resolve(kb[i], kb[j])
                if resolvent == set():
                    print("Empty clause derived → Contradiction found!")
                    return True
                if resolvent and resolvent not in kb:
                    new.append(resolvent)
        if not new:
            print("No new clauses. Resolution ends.")
            return False
        kb.extend(new)

# Example Knowledge Base
kb = [
    {'A', 'B'},
    {'~A', 'C'},
    {'~B', 'C'},
    {'~C'}
]
query = 'C'

print("Knowledge Base:", kb)
print("Query:", query)

if resolution(kb, query):
    print("Conclusion: KB ⊨", query)
else:
    print("Conclusion: KB ⊭", query)