# Base URL = http://www.adidas.com/us/EF1042.html?forceSelSizeEF1042_520
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}
#
def URLGen(model, size):
    BaseSize = 500
    ShoeSize = size - 6.5
    ShoeSize = ShoeSize * 20
    RawSize = ShoeSize + BaseSize
    ShoeSizeCode = int(RawSize)
    URL = 'http://www.adidas.com/us/' + str(model) + 'html?forceSelSize' + str(model) + '_' + str(ShoeSizeCode)
    return URL
#Model = raw_input('Model #')
#Size = input('Size: ')

#URL = URLGen(Model, Size)

#print(str(URL))