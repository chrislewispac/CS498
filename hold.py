
    with open('input2.txt') as fp:
        for line in fp:
                l = line.strip('\n').strip()
                for d in delimiters:
                        l = l.replace(d, " ")
                        finalResult = re.sub(' +', ' ', l)
                result = finalResult.lower().split(" ")
                # print [x for x in result if x not in stopWordsList]
                ret = ret + [x for x in result if x not in stopWordsList]