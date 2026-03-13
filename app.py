from flask import Flask

app = Flask(__name__)

@app.route('/'methods =[POST'])
def index():
    data = request.get_json()
    source_currency = data ['QueryResult']]['parameters']['unit-currency']['currency']
    amount = data ['QueryResult']]['parameters']['unit-currency']['amount']
    target_currency = data ['QueryResult']]['parameters']['unit-currency']['currency-name']
    print(source_currency)
    print(amount)
    print(target _amount)
    
    cf = fetch_conversation_factor(source_currency,target_currency)
    final_amount = amount * cf
    print(final_amount)
    
    
    def fetch_conversation_factor(source_target):
    url  ="https://free.currconv.com/api/v7/convert?={}_{}compact=ultra&apikay=9aa0c54f5and4c460c36b".format(source,target)
    
    respone = request .get(url)
    respone = response.json()
    print(respone)

if __name__=="__main__":
    app.run(debug =True)