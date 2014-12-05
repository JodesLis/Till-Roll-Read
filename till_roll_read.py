
import os

shops = ['BHAM', 'BOND', 'BRIS', 'BTNW', 'CAMB', 'CLCH',
         'CROD', 'DERB', 'DUBL', 'IPSW', 'LEST',
         'NORW', 'NOTT', 'OXFD', 'PEBR', 'REDI', 'SHEF',
         'WDGN', 'WLON']

working_path = 'C:/Users/jody/Desktop/Python scripts/amphora/till'


def old_amphora_read(tilllog, shop):
    with open(tilllog, "r") as f_in:
        raw_data = list(f_in.readlines())
        amphora_list = []
        for i in range(len(raw_data)):
            if raw_data[i][1:8] == 'GOODSS1':
                oil = raw_data[i-1]
                oil = oil.split("  ")[0]
                oil = oil[1::]
                price = raw_data[i].split()
                price = price[-1]
                amphora_list.append([shop, oil, price])
        return amphora_list


def read_directories():
    data = []
    for shop in shops:
        new_path = working_path + "/" + shop + "/"
        for file_name in os.listdir(new_path):
            till_data = old_amphora_read(new_path + file_name, shop)
            if len(till_data) != 0:
                for line in till_data:
                    data.append(line)
    return data


def write_csv(data):
    with open("amphora_prices.csv", "w+") as f_out:
        f_out.write("Shop, Oil, Price\n")
        for line in data:
            shop = line[0]
            item = line[1].strip("\n")
            price = line[2]
            f_out.write(shop + "," + item + "," + price + "\n")


write_csv(read_directories())