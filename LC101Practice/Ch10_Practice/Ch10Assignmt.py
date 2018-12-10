def get_country_codes(prices):

    #print(list(prices))
    #_________________# 1. Break the string into a list.

    prices.replace(',','')
    #print(prices)
    codes = prices.split()
    print(codes)
    
    nations = []
    for item in codes:
        nations.append(item.split('$'))
    # print(nations)
    
    # country_codes = []
    # for i in nations:
    #     country_codes.append(i.pop(0))
    # print(country_codes)
    # glue = ', '
    # end_result = glue.join(country_codes)
    # print(end_result)
    # return end_result

           
           
           #print(get_country_codes(prices))

# don't include these tests in Vocareum
#from test import testEqual

(get_country_codes("NZ$300, KR$1200, DK$5"), "NZ, KR, DK")
# testEqual(get_country_codes("US$40, AU$89, JP$200"), "US, AU, JP")
# testEqual(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"), "AU, NG, MX, BG, ES")
# testEqual(get_country_codes("CA$40"), "CA")