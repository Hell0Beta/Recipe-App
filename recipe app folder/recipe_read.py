import json
import customtkinter
from PIL import Image
import recipe_home as r_home


def home_btn():
    root.destroy()
    r_home.home()


def insertion():
    with open("recipe.json", "r") as openfile:
        recipe_dict = json.load(openfile)
        recipe_dishes = str(recipe_dict.keys())
        val = recipe_dishes.index("[")
        val_end = recipe_dishes.index("]")
        recipe_dishes = recipe_dishes[val + 1:val_end].replace("'", "").split(", ")
        for i in recipe_dishes:
            if "ingredient_" in i:
                recipe_dishes.remove(i)
        for i in recipe_dishes:
            if "," in i or "'" in i:
                recipe_dishes.remove(i)
        recipe_dishes = sorted(recipe_dishes, key=str.lower)

    rec = insertie.get()
    rec = rec.lower()
    for i in recipe_dishes:
        val = recipe_dishes.index(i)
        recipe_dishes[val] = recipe_dishes[val].lower()


    if rec in recipe_dishes:
        recipes.delete(0.0, 'end')
        ingredients.delete(0.0, 'end')
        recipes.insert(0.0, recipe_dict[rec])
        rec = "ingredient_"+rec
        ingredients.insert(0.0, recipe_dict[rec])
    else:
        recipes.insert(0.0, f"SORRY T-T \n WE DONT HAVE {rec} RECIPE....BUT YOU CAN CREATE!!\n XD")
    rootie.destroy()


def insertion_rqst():
    global insertie
    global rootie
    rootie = customtkinter.CTkToplevel()
    rootie.geometry("200x200")
    rootie.attributes('-topmost', 'true')
    customtkinter.CTkLabel(rootie, text="enter dish..", font=customtkinter.CTkFont(family="Courier", size=15)).pack()
    frm = customtkinter.CTkFrame(rootie)
    frm.pack()
    insertie = customtkinter.CTkEntry(frm, font=customtkinter.CTkFont(family="Courier"))
    img = customtkinter.CTkImage(dark_image=Image.open("fca356f4e98827e9a8ac0a278bf4e8cd.png"), size=(120,120))
    customtkinter.CTkButton(rootie, image=img, fg_color="#242424",
                            command=insertion, hover_color="#333f36", text=None, width=10).pack()
    insertie.pack()

    rootie.mainloop()


def recipe():
    global ingredients
    global recipes
    global root
    root = customtkinter.CTk()
    root.geometry("900x555")

    title_text = customtkinter.CTkLabel(root, text="UMAT COOKBOOK",
                                        font=customtkinter.CTkFont(family="Courier", size=45, weight="bold"))
    title_text.pack(pady=15)

    _text = customtkinter.CTkLabel(root, text="RECIPES",
                                        font=customtkinter.CTkFont(family="Courier", size=45, ))
    _text.pack(pady=10)
    hrz_mega = customtkinter.CTkFrame(root, fg_color="#242424")
    hrz_mega.pack(expand=True, fill="both", padx=60, pady=12)

    hrz_frm_out = customtkinter.CTkFrame(hrz_mega)
    hrz_frm_out.pack(pady=5, fill="both", expand=True)

    hrz_frm = customtkinter.CTkScrollableFrame(hrz_frm_out, width=90, height=350, fg_color="#242424")
    hrz_frm.pack(side="left", padx=15)

    ing_frm = customtkinter.CTkFrame(hrz_frm_out, fg_color="#242424")
    ing_frm.pack(side="left", fill="y")
    img = customtkinter.CTkImage(dark_image=Image.open("recipebook2.png"),size=(140 ,120))
    img_lbl = customtkinter.CTkButton(ing_frm, text=None, image=img, hover_color="#333f36",
                                      fg_color="#242424", command=insertion_rqst)
    img_lbl.pack()

    home = customtkinter.CTkImage(dark_image=Image.open("Umatata-removebg-preview.png"), size=(80, 80))
    customtkinter.CTkButton(root, image=home, text=None,command=home_btn,
                            fg_color="#242424", hover_color="#333f36").place(x=15, y=15)


    ingredients = customtkinter.CTkTextbox(ing_frm, width=240,
                                           font=customtkinter.CTkFont(family="Courier"))
    ingredients.pack(fill="y", expand=True)

    recipes = customtkinter.CTkTextbox(hrz_frm_out, font=customtkinter.CTkFont(family="Courier", size=15))
    recipes.pack(side="left", padx=10, fill="both", expand=True)

    with open("recipe.json", "r") as openfile:
        recipe_dict = json.load(openfile)
        recipe_dishes = str(recipe_dict.keys())
        val = recipe_dishes.index("[")
        val_end = recipe_dishes.index("]")
        recipe_dishes = recipe_dishes[val + 1:val_end].split(",")
        for i in recipe_dishes:
            if "ingredient" in i:
                recipe_dishes.remove(i)
        recipe_dishes = sorted(recipe_dishes, key=str.lower)

    for i in recipe_dishes:
        customtkinter.CTkLabel(hrz_frm, text=i, fg_color="#242424",
                                width=10, height=10,
                                font=customtkinter.CTkFont(family="Courier")).pack(pady=5)
    root.mainloop()


