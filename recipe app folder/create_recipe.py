import customtkinter
from PIL import Image
import json
import recipe_home as r_home

recipe = {}

# customtkinter.set_appearance_mode("dark")
#
# main_frm = customtkinter.CTkFrame(root, fg_color="#2a193e", height=223)
# main_frm.pack(fill="x")
#
# text_frm = customtkinter.CTkFrame(main_frm ,height=100)
# text_frm.pack()
# header = customtkinter.CTkLabel(text_frm)
# header.pack()


def home():
    root.destroy()
    r_home.home()


def save():
    dish = "ingredient_"
    dish += title.get()
    with open("recipe.json", "r") as openfile:
        recipe = json.load(openfile)

    recipe[dish] = textbox_ingredient.get("1.0", "end").lower()
    recipe[title.get()] = textbox_recipe.get("1.0", "end").lower()
    """adds ingredients to json file"""

    with open("recipe.json", "w") as outfile:
        json.dump(recipe, outfile, indent=4)
    rqst_root.destroy()


def rqst_name():
    global title

    title = customtkinter.CTkEntry(rqst_root, font=customtkinter.CTkFont(family="Courier"))
    title.pack(fill="x")

    customtkinter.CTkButton(rqst_root, text="save", command=save,
                            font=customtkinter.CTkFont(family="Courier")).pack()


def rqst_to_save():
    global rqst_root
    rqst_root = customtkinter.CTkToplevel(root)
    rqst_root.geometry("350x120")
    rqst_root.attributes('-topmost', 'true')
    customtkinter.CTkLabel(rqst_root, text="Do you want to save your recipe?",
                           font=customtkinter.CTkFont(family="Courier")).pack()
    btn_frm = customtkinter.CTkFrame(rqst_root)
    btn_frm.pack()
    btn_yes = customtkinter.CTkButton(btn_frm, text="yes", font=customtkinter.CTkFont(family="Courier"), command=rqst_name)
    btn_yes.pack(side="left")
    btn_no = customtkinter.CTkButton(btn_frm, text="no", font=customtkinter.CTkFont(family="Courier"),)
    btn_no.pack(side="left")
    rqst_root.mainloop()


def create_app():
    global textbox_ingredient
    global textbox_recipe
    global root
    root = customtkinter.CTk()
    root.geometry("900x555")
    """::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::TOP FRAME"""
    top_frm = customtkinter.CTkFrame(root, fg_color="#242424")
    top_frm.pack(fill="x", expand=True)
    home_img = customtkinter.CTkImage(dark_image=Image.open("Umatata-removebg-preview.png"), size=(60, 60))
    home_btn = customtkinter.CTkButton(top_frm, text=None, image=home_img, command=home
                                       ,width=10, fg_color="#242424")
    home_btn.pack(side="left")
    #middle_pad = customtkinter.CTkFrame(top_frm, height=10, )
    #middle_pad.pack(side="left")
    header = customtkinter.CTkLabel(top_frm, text="UMAT COOKBOOK", font=customtkinter.CTkFont(family="Courier", size=45, weight="bold"))
    header.pack()


    """::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;)RECIPE FRAMES"""

    cookbook_supermega_frm = customtkinter.CTkFrame(root, fg_color="#242424")
    cookbook_supermega_frm.pack(side="top", padx=50, fill="x", expand=True)

    recipe_mega_frm = customtkinter.CTkFrame(cookbook_supermega_frm, fg_color="#242424")
    recipe_mega_frm.pack(side="left", fill="y", )

    padfrm = customtkinter.CTkFrame(recipe_mega_frm, height=160, width=250, fg_color="#242424")
    padfrm.pack()
    img_of_create_label = customtkinter.CTkImage(dark_image=Image.open("recipebook2.png"), size=(110, 110))
    create_label_img = customtkinter.CTkButton(padfrm, text=None, image=img_of_create_label, width=10, height=10,
                                               fg_color="#242424", hover_color="#435c49", command=rqst_to_save)
    create_label_img.pack()

    create_label = customtkinter.CTkLabel(padfrm, text="LET'S COOK!!",
                                          font=customtkinter.CTkFont(size=35, family="Courier"))
    create_label.pack()

    ingredient_frm = customtkinter.CTkFrame(recipe_mega_frm, fg_color="#242424")
    ingredient_frm.pack(padx=20)

    textbox_ingredient = customtkinter.CTkTextbox(ingredient_frm, width=250, height=250, font=customtkinter.CTkFont(family="Courier"))
    textbox_ingredient.pack()
    textbox_ingredient.insert(0.0, "INGREDIENTS\n: ")



    recipe_frm = customtkinter.CTkFrame(cookbook_supermega_frm, fg_color="#242424")
    recipe_frm.pack(fill="x", expand=True, pady=15, padx=30)
    textbox_recipe = customtkinter.CTkTextbox(recipe_frm, width=250, height=400,
                                          font=customtkinter.CTkFont(family="Courier"))
    textbox_recipe.pack(fill="x", expand=True)
    textbox_recipe.insert(0.0, "RECIPES\n")

    root.mainloop()




