import subprocess
projectdir = "/usr/local/project/qingka-code"
projectarray=[
    ('qingka-voice',
     ('voice-api','voice-dubbo')
    ),
    ('qingka-content',
     ('content-app','content-dubbo')
    ),
    ('qingka-base',
     ('base-app','base-dubbo')
    )
]

serviceoptarray=('back','svn up','build','restart','all')
def choose_project():
    for i ,project in enumerate(projectarray):
        print(i,project[0])
    firstmenu = input("选择你的project:")

    if firstmenu.isdigit():
        firstmenu = int(firstmenu)
        if firstmenu < len(projectarray) and firstmenu >=0:
            print("project:" + projectarray[firstmenu][0])
            global service
            for j,service in enumerate(projectarray[firstmenu][1]):
                 print(j,service)
            secondmenu = input("选择你的service:")
            if secondmenu.isdigit():
                secondmenu = int(secondmenu)
                if secondmenu < len(project) and secondmenu >=0:
                    print("service:"+projectarray[firstmenu][1][secondmenu])
                else:
                    choose_project()
            else:
                choose_project()
        else:
            choose_project()
    else:
        choose_project()
    choose_opt()
def choose_opt():
    for i ,opt_list in enumerate(serviceoptarray):
        print(i,opt_list)
    global opt
    opt = input("选择你的操作：")
    if opt.isdigit():
        opt = int(opt)
        if opt < len(serviceoptarray) and opt >=0:
            print("opt:"+serviceoptarray[opt])
            if opt == "0":
                choose_project()
            elif opt == "1":
                svn_up()
            elif opt == "2":
                build()
            elif opt == "3":
                restart()
            else:
                svn_up()
                build()
                restart()
        else:
            choose_opt()
    else:
        choose_opt()
def svn_up():
    print(service+" :svn up")
    subprocess.check_output('svn up',shell=True,cwd='/usr/local/project/qingka-code')
def build():
    print(service + " :build")
    subprocess.check_output('svn up && mvn clean install -P test -Dmaven.test.skip=true -U', shell=True, cwd='/usr/local/project/qingka-code/service')
def restart():
    pass
choose_project()