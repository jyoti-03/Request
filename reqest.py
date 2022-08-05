# 1st part

# #import requests
# #x=requests.get("http://saral.navgurukul.org/api/courses")
# #import json
# #with open("course.json","w") as file:
# #        dic=json.loads(x.text)
# #        json.dump(dic,file,indent=4)


# 2nd part

# import requests
# x=requests.get("http://saral.navgurukul.org/api/courses")
# data=x.json()
# def course():
#     i =0
#     for j in data["availableCourses"]:
#         print(i+1,j["name"],j["id"])
#         i+=1
# course()
# course=int(input("enter your course: "))
# select=data["availableCourses"][course-1]["id"]
# var1=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercises")
# data1=var1.json()
# print(data1)


# 3rd part

import requests
x=requests.get("http://saral.navgurukul.org/api/courses")
dic=x.json()
def course():
    i =0
    for j in dic["availableCourses"]:
        print(i+1,j["name"],j["id"])
        i+=1
    couse=int(input("enter your course: "))
    select=dic["availableCourses"][couse-1]["id"]
    # print(type(select))
    exercise_api=requests.get("http://saral.navgurukul.org/api/courses/"+select+"/exercises")
    print(exercise_api)
    data=exercise_api.json()
    c=1
    slug=[]
    for dic_data in data["data"]:
        print(c,dic_data["slug"])
        slug.append(dic_data["slug"]) 
        c+=1
    slug_input=int(input("enter slug number:"))
    slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+slug[slug_input])
    print(slug_api)
    slug_json=slug_api.json()
    print(slug_input,slug_json["content"])
    # print("'UP':-for up content")
    # print("'NEXT':-for next content")
    # print("'EXIT':-for exit content")
    while True:
        print("'UP':-for up content")
        print("'NEXT':-for next content")
        print("'EXIT':-for exit content")
        step=input("enter your choice: ")
        if step=="up" or step=="UP" or step=="Up":
            slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+slug[slug_input-1])
            print(slug_api)
            up_json=slug_api.json()
            print(slug_input,up_json["content"])
            slug_input-=1
        elif step=="next" or step=="NEXT" or step=="Next":
            slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+slug[slug_input+1])
            print(slug_api)
            next_json=slug_api.json()
            print(slug_input,next_json["content"])
            slug_input+=1
        elif step=="exit" or step=="EXIT" or step=="Exit":
            course()
course()
