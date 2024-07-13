with open("F:\\python practice\\Assignment\\stocks.csv","r") as f, open("F:\\python practice\\Assignment\\ouput.csv","w") as out:
    out.write("Company Name, PE Ratio, PB Ratio\n")
    next(f)
    for line in f:
         names= line.split(',')
         stocks= names[0]
         price= float(names[1])
         ear= float(names[2])
         book= float(names[3])
         pe= round(price/ear ,2)
         pb= round(price/book ,2)
         out.write(f"{stocks},{pe},{pb}\n")