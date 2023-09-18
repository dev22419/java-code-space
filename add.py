def add(a) :
    f = open("add.html" , "a")
    f.write(a)
    f.close()

x = int(input("enter no of question : "))

i = 0
# <h2 class="codet">question 9</h2>
#   <h3 class="codet"></h3>
#       <iframe class="code" src="./assignment_1/nine.java" frameborder="1"></iframe>

while i < x :
    ques_no = ""
    ques = ""
    path = ""
    ques_no = input("question no : ")
    ques = input("question : ")
    path = input("file path : ")
    ques_no = "<h2 class=\"codet\">question "+ ques_no +"</h2>\n"
    ques = "<h3 class=\"codet\">"+ ques +"</h3>\n"
    path = "<iframe class=\"code\" src=\""+ path +"\" frameborder=\"1\"></iframe>\n"
    add(ques_no)
    add(ques)
    add(path)
    i = i + 1