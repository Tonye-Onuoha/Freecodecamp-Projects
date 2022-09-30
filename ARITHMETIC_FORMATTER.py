import re

def arithmetic_arranger(array,answer = None):
    if len(array) > 5:
        return "Error: Too many problems."
    top     = []
    middle  = []
    bottom  = []
    display = []

    pattern1 = r"^.+\s(/|\*)\s.+$"
    pattern2 = r"^\d+\s(\+|\-)\s\d+$"
    pattern3 = r"^\d{1,4}\s(\+|\-)\s\d{1,4}$"

    for math in array:
        if re.match(pattern1,math):
            return "Error: Operator must be '+' or '-'."
        if re.match(pattern2,math):
            result = eval(math)
            split = math.split(" ")
            if re.match(pattern3,math):
                head = split[0]
                if len(split[0]) > len(split[2]):
                    diff = len(split[0]) - len(split[2])
                    spaces = " " * (diff + 1)
                    split.insert(2,spaces)
                    head = " " + " " + head
                elif len(split[2]) > len(split[0]):
                    diff = len(split[2]) - len(split[0])
                    spaces = " " * diff
                    head = " " + " " + spaces + head
                    split.insert(2," ")
                else:
                    head = " " + " " + head
                    split.insert(2," ")
                split = split[1:]
                merge = "".join(split)
                length = len(merge)
                hyphen = "-" * length
                top.append(head)
                middle.append(merge)
                bottom.append(hyphen)
                if len(hyphen) > len(str(result)):
                    subt = len(hyphen) - len(str(result))
                    gap = " " * subt
                    result = gap + str(result)
                    display.append(result)
                else:
                    display.append(result)
            else:
                 return "Error: Numbers cannot be more than four digits."
                 
        else:
            return "Error: Numbers must only contain digits."


    first  = "    ".join(top)
    second = "    ".join(middle)
    last   = "    ".join(bottom)
    end    = "    ".join(display)

    del top
    del middle
    del bottom
    del display

    formula = []

    formula.append(first)
    formula.append(second)
    formula.append(last)
    formula.append(end)

    if answer == True:
        formula = "\n".join(formula)
        return formula
    else:
        formula.pop(-1)
        formula = "\n".join(formula)
        return formula
        
    
   




            
            
            
    
