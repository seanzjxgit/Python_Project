class Calculator:
    def add(self,a:int,b:int) ->int:
        return a+b

    def div(self,a:int,b:int) ->int:
        if b==0:
            raise ZeroDivisionError()

        return a//b