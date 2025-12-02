# Ranges for the question
ranges = [
    "851786270-851907437",
    "27-47",
    "577-1044",
    "1184-1872",
    "28214317-28368250",
    "47766-78575",
    "17432-28112",
    "2341-4099",
    "28969-45843",
    "5800356-5971672",
    "6461919174-6461988558",
    "653055-686893",
    "76-117",
    "2626223278-2626301305",
    "54503501-54572133",
    "990997-1015607",
    "710615-802603",
    "829001-953096",
    "529504-621892",
    "8645-12202",
    "3273269-3402555",
    "446265-471330",
    "232-392",
    "179532-201093",
    "233310-439308",
    "95134183-95359858",
    "3232278502-3232401602",
    "25116215-25199250",
    "5489-8293",
    "96654-135484",
    "2-17"
]
# Example ranges shown
sampleRanges = [
    "11-22",
    "95-115",
    "998-1012",
    "1188511880-1188511890",
    "222220-222224",
    "1698522-1698528",
    "446443-446449",
    "38593856-38593862"
]
# Example ranges shown for second part
secondSampleRanges = [
    "11-22",
    "95-115",
    "998-1012",
    "1188511880-1188511890",
    "222220-222224",
    "1698522-1698528",
    "446443-446449",
    "38593856-38593862",
    "565653-565659",
    "824824821-824824827",
    "2121212118-2121212124"
]

def partOne():
    invalid = [];
    count = 0
    for r in ranges:
        arr = r.split("-")
        start = int(arr[0])
        end = int(arr[1])
        i = start
        while i <= end:
            string = str(i)
            firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
            if firstpart == secondpart:
                invalid.append(i)
                i = i+11
            else:
                i =i+1
    for num in invalid:
        count = count + num
    print(count)


def partTwo():
    invalid = []
    count = 0
    for r in ranges:
        arr = r.split("-")
        start = int(arr[0])
        end = int(arr[1])
        num = start
        
        while num <= end:
            string = str(num)
            l = len(string)
            parts = []
            
            for splitI in range(1, l):
                # Only consider split sizes that divide the length exactly
                if l % splitI != 0:
                    continue

                parts = [string[i:i+splitI] for i in range(0, len(string), splitI)]
                allSame = len(parts) > 0 and len(set(parts)) == 1

                if allSame:
                    invalid.append(num)
                    break

            num += 1

    for number in invalid:
        count = count + number

    print(count)



if __name__ == "__main__":
    partTwo()

