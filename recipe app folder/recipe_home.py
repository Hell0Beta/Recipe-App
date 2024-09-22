import customtkinter
from PIL import Image
import create_recipe as cr
import recipe_read

def recipe():
    root.destroy()
    recipe_read.recipe()


def create():
    root.destroy()
    cr.create_app()


def home():
    global root
    root = customtkinter.CTk()
    root.geometry("900x555")
    customtkinter.set_appearance_mode("dark")

    top_pad = customtkinter.CTkFrame(root, height=80)
    top_pad.pack(pady=20,padx=10, side="left", anchor="nw")

    title_text = customtkinter.CTkLabel(root,text="UMAT COOKBOOK",
                                        font=customtkinter.CTkFont(family="Courier", size=45, weight="bold"))
    title_text.pack(pady=15)

    # horizontal_outer_frm = customtkinter.CTkFrame(root, )
    # horizontal_outer_frm.pack(fill="x")

    horizontal_frm = customtkinter.CTkFrame(root, width=700,fg_color="#242424")
    horizontal_frm.pack(pady=10, fill="y", expand=True)

    #side = customtkinter.CTkFrame(horizontal_frm, width=30, height=90)
    #side.pack(side="left", anchor="nw",padx=20)
    #
    #side_btm = customtkinter.CTkFrame(horizontal_frm, width=30, height=90)
    #side_btm.pack(side="left", anchor="sw", padx=20)

    """::::::::::::::::::::::::::::::::::::::::::::::::::::::::BTN FRM"""

    center_img = customtkinter.CTkImage(dark_image=Image.open("cookbook442.png"), size=(350, 350))
    center_img_lbl = customtkinter.CTkLabel(horizontal_frm, image=center_img, text=None, width=10, height=10)
    center_img_lbl.pack(side="left", padx=30)

    pad_mid = customtkinter.CTkFrame(horizontal_frm, width=80, fg_color="#242424")
    pad_mid.pack(side="left")

    btn_frm = customtkinter.CTkFrame(horizontal_frm, fg_color="#242424")
    btn_frm.pack(side="left", padx=20)

    btn_image_frm = customtkinter.CTkFrame(btn_frm, height=50, fg_color="#242424")
    btn_image_frm1 = customtkinter.CTkFrame(btn_frm, height=50, fg_color="#242424")
    btn_image_frm.pack()
    btn_image_frm1.pack(pady=20)

    btn_img = customtkinter.CTkImage(dark_image=Image.open("0c996d7a3425bcb678bb240798f2e4f1.png"), size=(130,130))
    btn_img_btn = customtkinter.CTkButton(btn_image_frm, image=btn_img, command=create,
                                          text=None, width=10, height=10, fg_color="#242424")
    btn_img_btn.pack(pady=10)
    btn_create = customtkinter.CTkButton(btn_image_frm, text="create", command=create,
                                         font=customtkinter.CTkFont(family="Courier"))
    btn_create.pack()


    btn_img1 = customtkinter.CTkImage(dark_image=Image.open("a29584cd5ca5051a2b4b80119306283a.png"), size=(130, 130))
    btn_img1_lbl = customtkinter.CTkButton(btn_image_frm1, image=btn_img1, command=recipe,
                                           text=None, width=10, height=10, fg_color="#242424")
    btn_img1_lbl.pack()
    btn_recipe = customtkinter.CTkButton(btn_image_frm1, text="recipe", command=recipe,
                                         font=customtkinter.CTkFont(family="Courier"))
    btn_recipe.pack()

    top_corner = customtkinter.CTkImage(dark_image=Image.open("Umatata-removebg-preview.png"), size=(80,80))
    top_corner_lbl = customtkinter.CTkLabel(top_pad, image=top_corner, text=None, fg_color="#242424")
    top_corner_lbl.pack(side="left")

    #side_lfttop = customtkinter.CTkFrame(horizontal_frm, width=30, height=90)
    #side_lfttop.pack(side="right", anchor="ne",padx=20)
    #
    #side_lftbtm = customtkinter.CTkFrame(horizontal_frm, width=30, height=90)
    #side_lftbtm.pack(side="right", anchor="se",padx=20)
    root.mainloop()


