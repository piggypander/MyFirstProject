active1 = True
active2 = True
filename = "text_file/历史待完成事项"
filename2 = "text_file/历史已完成事项"
with open(filename, "r") as file_object:
    content = file_object.read()
    historic_projects = content.split()
unfinished_projects = []
finished_projects = []
for project in historic_projects:
    unfinished_projects.append(project)


def add_unfinished_projects():
    while active1:
        plan_project = input("请添加待完成事项（输入end来结束添加）：")
        if plan_project == "end":
            break
        else:
            unfinished_projects.append(plan_project)
            print(f"已添加事项：{plan_project}")


def unfinished_finished_translator():
    if len(unfinished_projects) == 0:
        print("请先添加待完成事项！")
    else:
        active3 = True
        while active3:
            print(unfinished_projects)
            finished_item = input("刚完成事项（请对照未完成事项中的项目名填写，误触则输入back以返回）：")
            if finished_item == "back":
                active3 = False
            else:
                try:
                    unfinished_projects.remove(finished_item)
                except ValueError:
                    print("请正确输入未完成事项中的项目名。")
                else:
                    finished_projects.append(finished_item)
                    if finished_item in historic_projects:
                        historic_projects.remove(finished_item)
                        with open(filename, "w") as file_object1:
                            for project in historic_projects:
                                file_object1.write(project)
                    print(f"{finished_item}已完成。")
                    active3 = False


def delete_unfinished_projects():
    if len(unfinished_projects) == 0:
        print("请先添加待完成事项！")
    else:
        active4 = True
        while active4:
            print(unfinished_projects)
            delete_project = input("想要删除的事项（请对照未完成事项中的项目名称填写，误触则输入back以返回）：")
            if delete_project == "back":
                active4 = False
            else:
                try:
                    unfinished_projects.remove(delete_project)
                except ValueError:
                    print("请正确输入未完成事项中的项目名。")
                else:
                    if delete_project in historic_projects:
                        historic_projects.remove(delete_project)
                        with open(filename, "w") as file_object2:
                            for project in historic_projects:
                                file_object2.write(project)
                    print(unfinished_projects)
                    print(f"已删除{delete_project}。")
                    active4 = False


def projects_fix():
    if len(unfinished_projects) == 0:
        print("请先添加待完成事项！")
    else:
        active5 = True
        while active5:
            print(unfinished_projects)
            to_fix_project = input("想要修改的事项（请对照未完成事项中的项目名称输入,误触输入back以返回）：")
            if to_fix_project == "back":
                active5 = False
            else:
                new_project = input("你想将它修改为：")
                try:
                    unfinished_projects.remove(to_fix_project)
                except ValueError:
                    print("请正确输入未完成事项中的项目名。")
                else:
                    unfinished_projects.append(new_project)
                    if to_fix_project in historic_projects:
                        historic_projects.remove(to_fix_project)
                        historic_projects.append(new_project)
                        with open(filename, "w") as file_object3:
                            for project in historic_projects:
                                file_object3.write(project)
                    print(f"{to_fix_project} 已被修改为{new_project}.")
                    active5 = False


def project_saving():
    if len(unfinished_projects) == 0:
        print("请先添加待完成事项！")
    else:
        to_save_projects = []
        active6 = True
        while active6:
            print("未完成事项：")
            print(unfinished_projects)
            print("历史未完成事项：")
            print(historic_projects)
            to_save_project = input("请输入想要储存的待完成事项\n（请对照未完成事项与历史未完成事项输入新的需要储存的事项，一次输入一个事项,输入'end'结束）：")
            if to_save_project == "end":
                active6 = False
            else:
                if to_save_project not in unfinished_projects:
                    print("请输入正确的待完成事项。")
                else:
                    to_save_projects.append(to_save_project)
                    print(f"“{to_save_project}”已添加至历史未完成列表中。")
        if len(to_save_projects) == 0:
            print("你尚未添加想要储存的事项。")
        else:
            for project in to_save_projects:
                if project in historic_projects:
                    pass
                else:
                    historic_projects.append(project)
            with open(filename, "w") as file_object4:
                for item in historic_projects:
                    file_object4.write(f"{item}\n")
            with open(filename, "r") as file_object5:
                content1 = file_object5.read()
            new_historic_projects = content1.split()
            print(new_historic_projects)
            print("项目已储存至历史待完成事项。")


while active2:
    prompt = input("请输入指令（添加待完成事项A/完成事项B/查看待完成事项C/查看完成事项D/删除事项E/修改事项F/储存事项G/退出程序H）：")
    if prompt == "A":
        add_unfinished_projects()
    elif prompt == "B":
        unfinished_finished_translator()
    elif prompt == "C":
        print(unfinished_projects)
    elif prompt == "D":
        print(finished_projects)
    elif prompt == "E":
        delete_unfinished_projects()
    elif prompt == "F":
        projects_fix()
    elif prompt == "G":
        project_saving()
    elif prompt == "H":
        if len(unfinished_projects) == 0:
            print("谢谢你的使用！")
            active2 = False
        else:
            number = len(unfinished_projects)
            print(f"你还有{number}个项目尚未完成。")
            question = input("输入A取消退出程序，B前往储存事项，C继续退出程序：")
            if question == "A":
                pass
            elif question == "B":
                project_saving()
            elif question == "C":
                with open(filename2, "a") as file_object6:
                    for project in finished_projects:
                        file_object6.write(f"{project}\n")
                print("谢谢你的使用！")
                active2 = False
            else:
                print("请输入正确指令！")
    elif prompt == "H FINISHED":
        with open(filename2, "r") as file_object6:
            for line in file_object6:
                print(line.rstrip())
    elif prompt == "H UNFINISHED":
        with open(filename, "r") as file_object:
            for line in file_object:
                print(line.rstrip())
    else:
        print("请输入正确的指令！")
# 如何把日期加上？如何加上事件重要程度？如何加上定时提示？
# 如何优化程序做到人性化？
