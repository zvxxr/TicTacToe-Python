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

info_frame = ctk.CTkFrame(window, height=150, width=700, fg_color="#111111", corner_radius=20)
info_frame.pack(pady=(10, 10))
info_frame.pack_propagate(False)

first_player_label = ctk.CTkLabel(info_frame, text=f"{'X'}: ", font=("Poppins", 70, "bold"),)
first_player_label.pack(padx=(40, 0), side="left", anchor="center", pady=(16, 0))

first_player_score = ctk.CTkLabel(info_frame, text=f"{0}", font=("Poppins", 70, "bold"),)
first_player_score.pack(side="left", anchor="center", pady=(16, 0))

second_player_score = ctk.CTkLabel(info_frame, text=f"{0}", font=("Poppins", 70, "bold"),)
second_player_score.pack(padx=(0, 40), side="right", anchor="center", pady=(16, 0))

second_player_label = ctk.CTkLabel(info_frame, text=f"{'O'}: ", font=("Poppins", 70, "bold"))
second_player_label.pack(side="right", anchor="center", pady=(16, 0))

game_status_label = ctk.CTkLabel(info_frame, text=f"{'X'}'s turn", font=("Poppins", 34, "bold"))
game_status_label.pack(side="bottom", anchor="s")

players_ratio_progress_bar = ctk.CTkProgressBar(info_frame, width=260)
players_ratio_progress_bar.pack(side="left", anchor="center", expand=True, pady=(50, 0))

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

current_player = "X"
def button_action(btn):
    global current_player
    if btn.cget("text") == " ":
        if current_player == "X":
            btn.configure(text="X")
            current_player = "O"
        else:
            btn.configure(text="O")
            current_player = "X"


def add_buttons(frame=top_frame, fg_color="grey", text=" "):
    first_btn = ctk.CTkButton(frame, fg_color=fg_color, text=text, height= 114, width= 114,
                              command= lambda: button_action(first_btn), font=("Poppins", 34, "bold"))
    first_btn.pack(side="left", expand=True)

    second_btn = ctk.CTkButton(frame, fg_color=fg_color,text=text, height= 114, width= 114,
                               command= lambda: button_action(second_btn), font=("Poppins", 34, "bold"))
    second_btn.pack(side="left", expand=True)

    third_btn = ctk.CTkButton(frame, fg_color=fg_color, text=text, height= 114, width= 114,
                              command= lambda: button_action(third_btn), font=("Poppins", 34, "bold"))
    third_btn.pack(side="left", expand=True)

    return first_btn, second_btn, third_btn

a1, a2, a3 = add_buttons()
b1, b2, b3 = add_buttons(mid_frame)
c1, c2, c3 = add_buttons(bottom_frame)

def which_button(button=a1):
    return button


player_choose_frame = ctk.CTkFrame(window, height=130, width=480, fg_color="#111111")
player_choose_frame.pack(side="top", pady=(10, 0))
player_choose_frame.pack_propagate(False)

play_as_label= ctk.CTkLabel(player_choose_frame, text=f"Play as:", font=("Poppins", 40, "bold"))
play_as_label.pack(side="left", padx=(50, 0))

pvp_box = ctk.CTkCheckBox(player_choose_frame, font=("Poppins", 20, "bold"), text="Player vs Player")
pvp_box.pack(side="top", pady=(30, 0), anchor="w", padx=20)

pvb_box = ctk.CTkCheckBox(player_choose_frame, font=("Poppins", 20, "bold"), text="Player vs Bot")
pvb_box.pack(side="top", anchor="w", padx=20)









window.mainloop()