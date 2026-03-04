# keyword arguments = an argument preceded by an identifier 
# helps with readability order of agruments doesnt matter 
# 1. positional 2. default 3 keyword 4 arbitary


def get_phone(country,area,first,last):
    return f"{country}--{area}--{first}--{last}"

phone_num =get_phone(area=55200,country="Malaysia",first=6019,last=5565741)

print(phone_num)