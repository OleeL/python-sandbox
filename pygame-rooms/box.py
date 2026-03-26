# public class Employee {
#     // Instance variables (non-static)
#     private String name;
#     private float salary;

#     // Constructor
#     public Employee(String name, float salary) {
#         this.name = name;
#         this.salary = salary;
#     }

#     // getters method
#     public String getName() { return name; }
#     public float getSalary() { return salary; }

#     // setters method
#     public void setName(String name) { this.name = name; }
#     public void setSalary(float salary) { this.salary = salary; }

#     // Instance method
#     public void displayDetails() {
#         System.out.println("Employee: " + name);
#         System.out.println("Salary: " + salary);
#     }

#     public static void main(String[] args) {
#         Employee emp = new Employee("Geek", 10000.0f);
#         emp.displayDetails();
#     }
# }

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.salary = salary
        
    def getSalary(self):
        
        return self.salary
    
        
oli = Employee("Oli", 100)
oli.salary = 1000
print(oli.salary)

print(oli.getSalary())