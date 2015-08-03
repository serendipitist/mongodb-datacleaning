import bottle

@bottle.route('/')
def home_page():
    mythings=['MongoDB','Hadoop','Python', 'Java']
    return bottle.template('hello_world',{'user':"Shireesha",'things':mythings})

@bottle.post('/favorite_skill')
def favorite_topic():
    skill=bottle.request.forms.get("skill")
    if(skill== None or skill ==""):
        skill="No skill is selected"
        return bottle.template('skill_selection.tpl',{'skill':skill})
    bottle.debug(True)
    bottle.run(host='localhost',port=8080)
    