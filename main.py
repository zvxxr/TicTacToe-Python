import customtkinter as ctk

window = ctk.CTk(fg_color="#292929")
window.title("TicTacToe")
ctk.set_default_color_theme("green")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 400
window_height = 400

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

info_frame = ctk.CTkFrame(window, height=150, width=1300, fg_color="#111111", corner_radius=20)
info_frame.pack(pady=(20, 20))
info_frame.pack_propagate(False)

main_frame = ctk.CTkFrame(window, height=380, width=380, fg_color="#111111", corner_radius=20)
main_frame.pack()
main_frame.pack_propagate(False)

top_frame = ctk.CTkFrame(main_frame, height=118, width=360, fg_color="#141414")
top_frame.pack(pady=(9, 1))
top_frame.pack_propagate(False)


mid_frame = ctk.CTkFrame(main_frame, height=118, width=360, fg_color="#141414")
mid_frame.pack(pady=1)
mid_frame.pack_propagate(False)


bottom_frame = ctk.CTkFrame(main_frame, height=118, width=360, fg_color="#141414")
bottom_frame.pack(pady=1)
bottom_frame.pack_propagate(False)

def add_buttons(frame=top_frame, fg_color="grey", text=" "):
    first_btn = ctk.CTkButton(frame, fg_color=fg_color, text=text, height= 114, width= 114)
    first_btn.pack(side="left", expand=True)

    second_btn = ctk.CTkButton(frame, fg_color=fg_color,text=text, height= 114, width= 114)
    second_btn.pack(side="left", expand=True)

    third_btn = ctk.CTkButton(frame, fg_color=fg_color, text=text, height= 114, width= 114)
    third_btn.pack(side="left", expand=True)

    return first_btn, second_btn, third_btn

a1, a2, a3 = add_buttons()
b1, b2, b3 = add_buttons(mid_frame)
c1, c2, c3 = add_buttons(bottom_frame)







window.mainloop()