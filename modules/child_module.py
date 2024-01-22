import parent_module
result= parent_module.kg_to_lb(57)
#result2=parent_module.lb_to_kg(126.6)
print(result)#126.666
#print(result2)#56.9

#another way of importing is only importing the specific functions from the module
from parent_module import lb_to_kg
result2=lb_to_kg(126.6)
print(result2)#56.9