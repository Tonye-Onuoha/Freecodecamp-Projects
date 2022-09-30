class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def deposit(self,amount,description = ""):
        """A deposit method that accepts an amount and description.
        If no description is given, it should default to an empty string."""
        money = {"amount":amount,"description":description}
        self.ledger.append(money)

    def withdraw(self,amount,description = ""):
        """A withdraw method that is similar to the deposit method,
        but the amount passed in should be stored in the ledger as a negative number."""
        if self.check_funds(amount):
            amount = -(amount)
            money = {"amount":amount,"description":description}
            self.ledger.append(money)
            return True
        else:
            return False

    def get_balance(self):
        """A get_balance method that returns the current balance of the budget category
        based on the deposits and withdrawals that have occurred."""
        result = []
        for cash in self.ledger:
            result.append(cash["amount"])
        balance = sum(result)
        return balance

    def transfer(self,amount,instance):
        """A transfer method that accepts an amount and another budget category as arguments.
        The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
        The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]"."""
        if self.check_funds(amount):
            cash = self.withdraw(amount,"Transfer to " + instance.name)
            if cash == True:
                instance.deposit(amount,"Transfer from " + self.name)
                return True
            else:
                return False
        else:
            return False

    def check_funds(self,amount):
        """A check_funds method that accepts an amount as an argument.
        It returns False if the amount is greater than the balance of the budget category and returns True otherwise."""
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        output = []
        desc   = []
        amount = []

        title = self.name.center(30,"*")
        output.append(title)


        for cash in self.ledger:
            desc.append(cash["description"])
            amount.append(cash["amount"])

            if type(amount[0]) == int:
                amount[0] = str(amount[0]) + ".00"
            else:
                amount[0] = str(amount[0])

            if len(desc[0]) > 23:
                desc[0] = desc[0][0:23]
                
            if len(amount[0]) > 7:
                amount[0] = amount[0][0:7]

            if len(desc[0]) + len(amount[0]) < 30:
                length = 30 - (len(desc[0]) + len(amount[0]))
                spaces = " " * length
                merge = desc[0] + spaces + amount[0]
                output.append(merge)
                desc = []
                amount = []
            else:
                merge = desc[0] + amount[0]
                output.append(merge)
                desc = []
                amount = []

        balance = self.get_balance()
        
        if type(balance) == int:
            balance = str(balance) + ".00"

        total = "Total: {}".format(balance)
        
        if len(total) > 30:
            total = total[0:30]

        output.append(total)

        budget = "\n".join(output)

        return budget

        
        

def create_spend_chart(categories):
    """This function takes a list of categories and returns a bar chart
    that shows the percentage spent in each category."""
    
    Hundred = ["100| "]
    Ninety  = [" 90| "]
    Eighty  = [" 80| "]
    Seventy = [" 70| "]
    Sixty   = [" 60| "]
    Fifty   = [" 50| "]
    Forty   = [" 40| "]
    Thirty  = [" 30| "]
    Twenty  = [" 20| "]
    Ten     = [" 10| "]
    Zero    = ["  0| "]
    
    withdrawals = []
    test        = []
    vertical    = []
    percentage  = []
    total_list  = []
    
    for instance in categories:
        for cash in instance.ledger:
            if str(cash["amount"]).startswith("-"):
                total_list.append(abs(cash["amount"]))

    total_spent = sum(total_list)

    for instance in categories:
        for cash in instance.ledger:
            if str(cash["amount"]).startswith("-"):
                withdrawals.append(abs(cash["amount"]))

        integer = (sum(withdrawals) * 100)
        total = integer/total_spent
        percent = total//10
        percent = int(percent * 10)
        withdrawals = []
        if percent == 100:
            Hundred.append("o  ")
            Ninety.append("o  ")
            Eighty.append("o  ")
            Seventy.append("o  ")
            Sixty.append("o  ")
            Fifty.append("o  ")
            Forty.append("o  ")
            Thirty.append("o  ")
            Twenty.append("o  ")
            Ten.append("o  ")
            Zero.append("o  ")
        if percent == 90:
            Hundred.append("   ")
            Ninety.append("o  ")
            Eighty.append("o  ")
            Seventy.append("o  ")
            Sixty.append("o  ")
            Fifty.append("o  ")
            Forty.append("o  ")
            Thirty.append("o  ")
            Twenty.append("o  ")
            Ten.append("o  ")
            Zero.append("o  ")
        if percent == 80:
            Hundred.append("   ")
            Ninety.append("   ")
            Eighty.append("o  ")
            Seventy.append("o  ")
            Sixty.append("o  ")
            Fifty.append("o  ")
            Forty.append("o  ")
            Thirty.append("o  ")
            Twenty.append("o  ")
            Ten.append("o  ")
            Zero.append("o  ")
        if percent == 70:
            Hundred.append("   ")
            Ninety.append("   ")
            Eighty.append("   ")
            Seventy.append("o  ")
            Sixty.append("o  ")
            Fifty.append("o  ")
            Forty.append("o  ")
            Thirty.append("o  ")
            Twenty.append("o  ")
            Ten.append("o  ")
            Zero.append("o  ")
        if percent == 60:
            Hundred.append("   ")
            Ninety.append("   ")
            Eighty.append("   ")
            Seventy.append("   ")
            Sixty.append("o  ")
            Fifty.append("o  ")
            Forty.append("o  ")
            Thirty.append("o  ")
            Twenty.append("o  ")
            Ten.append("o  ")
            Zero.append("o  ")
        if percent == 50:
            Hundred.append("   ")
            Ninety.append("   ")
            Eighty.append("   ")
            Seventy.append("   ")
            Sixty.append("   ")
            Fifty.append("o  ")
            Forty.append("o  ")
            Thirty.append("o  ")
            Twenty.append("o  ")
            Ten.append("o  ")
            Zero.append("o  ")
        if percent == 40:
            Hundred.append("   ")
            Ninety.append("   ")
            Eighty.append("   ")
            Seventy.append("   ")
            Sixty.append("   ")
            Fifty.append("   ")
            Forty.append("o  ")
            Thirty.append("o  ")
            Twenty.append("o  ")
            Ten.append("o  ")
            Zero.append("o  ")
        if percent == 30:
            Hundred.append("   ")
            Ninety.append("   ")
            Eighty.append("   ")
            Seventy.append("   ")
            Sixty.append("   ")
            Fifty.append("   ")
            Forty.append("   ")
            Thirty.append("o  ")
            Twenty.append("o  ")
            Ten.append("o  ")
            Zero.append("o  ")
        if percent == 20:
            Hundred.append("   ")
            Ninety.append("   ")
            Eighty.append("   ")
            Seventy.append("   ")
            Sixty.append("   ")
            Fifty.append("   ")
            Forty.append("   ")
            Thirty.append("   ")
            Twenty.append("o  ")
            Ten.append("o  ")
            Zero.append("o  ")
        if percent == 10:
            Hundred.append("   ")
            Ninety.append("   ")
            Eighty.append("   ")
            Seventy.append("   ")
            Sixty.append("   ")
            Fifty.append("   ")
            Forty.append("   ")
            Thirty.append("   ")
            Twenty.append("   ")
            Ten.append("o  ")
            Zero.append("o  ")
        if percent == 0:
            Hundred.append("   ")
            Ninety.append("   ")
            Eighty.append("   ")
            Seventy.append("   ")
            Sixty.append("   ")
            Fifty.append("   ")
            Forty.append("   ")
            Thirty.append("   ")
            Twenty.append("   ")
            Ten.append("   ")
            Zero.append("o  ")
            
            
        
        
    for instance in categories:
        test.append(instance.name)

    longest_string = max(test,key=len)

    for names in test:
        if names != longest_string:
            length = len(longest_string) - len(names)
            spaces = " " * length
            merge = str(names) + spaces
            vertical.append(merge)



    index = test.index(longest_string)

    vertical.insert(index,longest_string)

    del test

    count = 0
    arrangement = []
    depth = []

    for i in range(len(longest_string)):
        for members in vertical:
            arrangement.append(members[count])
        merge = "  ".join(arrangement)
        indent = (" " * 5) + merge + "  "
        depth.append(indent)
        arrangement = []
        count += 1

    del arrangement

    del vertical

    length = max(depth,key=len)
    hyphen_len = len(length)
    hyphen = "-" * (hyphen_len)
    hyphen = hyphen[4:]
    hyphen = (" " * 4) + hyphen

    depth.insert(0,hyphen)


    hundred = "".join(Hundred)
    ninety  = "".join(Ninety)
    eighty  = "".join(Eighty)
    seventy = "".join(Seventy)
    sixty   = "".join(Sixty)
    fifty   = "".join(Fifty)
    forty   = "".join(Forty)
    thirty  = "".join(Thirty)
    twenty  = "".join(Twenty)
    ten     = "".join(Ten)
    zero    = "".join(Zero)

    percentage.append("Percentage spent by category")
    percentage.append(hundred)
    percentage.append(ninety)
    percentage.append(eighty)
    percentage.append(seventy)
    percentage.append(sixty)
    percentage.append(fifty)
    percentage.append(forty)
    percentage.append(thirty)
    percentage.append(twenty)
    percentage.append(ten)
    percentage.append(zero)
    for i in depth:
        percentage.append(i)

    del depth

    chart = "\n".join(percentage)


    return chart
    
    

    
            





  
        








pie = Category("Food")
gucci = Category("Clothing")
car = Category("Auto")
pie.deposit(1000,"initial deposit")
pie.withdraw(10.15,"groceries")
pie.withdraw(15.89,"restaurant and more food")
pie.transfer(50,gucci)
gucci.withdraw(22.55,"Shopping")
gucci.withdraw(100,"Shopping")
car.deposit(1000,"Insurance")
car.withdraw(15,"Maintenance")


















        
