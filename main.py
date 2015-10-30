from PIL import Image, ImageDraw, ImageFont

# const MESSAGES
# const OPTIONS
# const PATH_TO_IMAGES (dict {'yellow': path/to/yellow.jpg})
# Class Menu (options, display(options, messages, inputs))
# Class Category (add, delete, get)
# Class Task (category, add, delete)
"""
Class Wallpaper(get_img, get_category, get_tasks, create, get_sticker_center,
    calc_num_stickers_in_row)
"""
# Class Main (to interact with user)
"""
Example of conf file:
{'category1':['task1','task2','task3']}
"""

OPTIONS = {
    '1': 'Add category',
    '2': 'Delete category',
    '3': 'Add task',
    '4': 'Delete task',
    '0': 'Quit'
}

CONF = {'programming': ['barter', 'wallpaper'], 'family': ['love', 'dinner']}

for option in OPTIONS:
    print(option + ": " + OPTIONS[option])

print("Please, type the number of your choice:")
choice = input("--> ")

if choice == '1':
    print("Please type in category name or type Q to cansel")
    category = input("--> ")
    if category.lower() == 'q':
        pass
    else:
        if CONF.get(category) is None:
            CONF[category] = []
        else:
            print('This category is already exist!')
elif choice == '2':
    for category in CONF:
        print(category)
    print('Please, type in the category you would like to remove or press Q:')
    to_remove = input("--> ")
    if to_remove.lower() == 'q':
        pass
    else:
        try:
            CONF.pop(to_remove)
        except KeyError:
            print("There is no such category")
elif choice == '3':
    print("Please type in task name or type Q to cansel:")
    task_name = input("--> ")
    if task_name.lower() == 'q':
        pass
    else:
        print("Thank you! Your task is %s" % (task_name))
        print("To what category you'd like to add %s:" % (task_name))
        for category in CONF:
            print(category)
        category = input("Category -->")
        if category in CONF:
            CONF[category] += task_name
        else:
            CONF[category] = [task_name]
elif choice == '4':
    print("Please type in task name or type Q to cansel:")
    for cat in CONF:
        for task in CONF[cat]:
            print(task)
    task_name = input("-->")
    if task_name.lower() != 'q':
        for cat in CONF:
            if task_name in CONF[cat]:
                CONF[cat].remove(task_name)
                print('Success!')
                print("Remain" + CONF[cat])


print("Please, type in the path of your wallpaper image:")
path = input("-->")
wallpaper = Image.open(path)
font = ImageFont.truetype('permian/PermianSansTypeface.otf', 40)

coord_for_sticker = (0, 0)
for category in CONF:
    sticker = Image.open("sticker.png")
    draw = ImageDraw.Draw(sticker)
    x_for_text = 50
    y_for_text = 50
    draw.text((x_for_text, y_for_text), category, font=font)
    for task in CONF[category]:
        y_for_text += 40
        draw.text((x_for_text, y_for_text), task, font=font)
    wallpaper.paste(sticker, coord_for_sticker)
    coord_for_sticker = (coord_for_sticker[0] + 400, coord_for_sticker[1])

wallpaper.save("text.jpg")
