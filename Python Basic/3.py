import statistics

stocks = {
    'info': [600,630,620],
    'ril': [1430,1490,1567],
    'mtl': [234,180,160]
}

def add():
    s= input("Enter a stocks : ")
    p= input(f"Enter {s} products")
    p= float(p)
    if s in stocks:
        stocks[s].append(p)
    else:
        stocks[s]=[p]
    print_all()

def print_all():
    for s,p in stocks.items():
        avg= statistics.mean(p)
        print(f"{s} = {p} Average = ",round(avg,2))

def main():
    p=input('Enter what you want to do (add , print)')
    if p.lower()=='add':
        add()
    else:
        p.lower()=='print'
        print_all()
if __name__=='__main__':
        main()