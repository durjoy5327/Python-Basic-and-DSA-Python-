population={
    'India':170,
    'China':156,
    'USA':100,
    'Indonesia':80
}

def add():
    country= input("Enter country Name: ")
    country= country.lower()
    if country in population:
        print("Country already exist in the population so you can't change")
        return 
    p=input(f'Enter the {country} Population: ')
    p= float(p)
    population[country]=p
    print_all()

def delete():
    country= input("Enter country Name: ")
    country= country.lower()
    if country not in population:
        print(f"{Country} doesn't exist in Population")
        return
    del population[country]
    print_all()

def query():
    country= input("Enter country Name: ")
    if country not in population:
        print(f"{country} doesn't exist in population")
        return
    print(f"Population if {country} = {population[country]}")
def print_all():
    for country ,p in population.items():
        print(f"{country} = {p}" )

def main():
    inp= input('Enter (add , delete , print) what do you want  ')
    if inp.lower()=='add':
        add()
    elif inp.lower()=='delete':
        delete()
    elif inp.lower()=='print':
        print_all()
    else:
        print('Please Enter (add , delete , print)')
if __name__== '__main__':
    main()