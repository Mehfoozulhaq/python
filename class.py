class programmer:
    company= "Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=int(salary)
        self.pin=pin

p= programmer("harry",1500000,1922)
print(p.name,p.salary,p.pin,p.company)
r= programmer("anav",1500000,1922)
print(r.name,r.salary,r.pin,r.company)
