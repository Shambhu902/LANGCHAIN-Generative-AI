from langchain_community.document_loaders import WebBaseLoader
url = "https://www.flipkart.com/crocs-bayaband-unisex-clogs/p/itmf9zdexxjdjz7z?pid=SNDGFF5U4ZFBTRAQ&lid=LSTSNDGFF5U4ZFBTRAQZNMUAQ&marketplace=FLIPKART&q=crocs&store=osp&srno=s_1_8&otracker=search&otracker1=search&fm=organic&iid=57688765-cc42-4f28-918a-be668e16e66e.SNDGFF5U4ZFBTRAQ.SEARCH&ppt=hp&ppn=homepage&ssid=kg26h6vxdsdfzg8w1792333459948&qH=288311fdda8a29ae&ov_redirect=true"
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)