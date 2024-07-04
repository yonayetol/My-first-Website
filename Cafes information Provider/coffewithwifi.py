from flask import Flask,render_template,request
boom=Flask(__name__)
# the data of the cafes wil be here 👇
my_list=[
    {
        "name":"YONAS CAFE",
        "Location":"https://www.google.com/maps/place/Holy+Trinity+Cathedral/@9.0308544,38.7664298,17z/data=!3m1!4b1!4m6!3m5!1s0x164b8588f1adbed3:0x7bf4bbfea240b9b9!8m2!3d9.0308544!4d38.7664298!16s%2Fm%2F02z7bnw?entry=ttu",
        "Open":"2AM",
        "Close":"5PM",
        "Coffee":"☕☕☕",
        "Wifi":"💪💪💪",
        "Power":"🔌🔌🔌"
    }
]
@boom.route("/")
def front():
    return render_template("index.html")
@boom.route("/the_cafes.html")
def the_list_of_cafes():
    return render_template("the_cafes.html", my_list=my_list)
@boom.route('/adding_new')
def add():
    return render_template("adding.html")
@boom.route("/adding_new", methods=['POST'])
def to_add():
    new_Cafe={
        "name":request.form['name'],
        "Location":request.form['Location'],
        "Open":request.form['Open'],
        "Close":request.form['Close'],
        "Coffee":request.form['Coffee'],
        "Wifi":request.form['Wifi'],
        "Power":request.form['Power']
    }
    my_list.append(new_Cafe)
    return render_template("the_cafes.html", my_list=my_list)
boom.run(debug=True)
