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

game_status_label = ctk.CTkLabel(info_frame, text=f"X's turn", font=("Poppins", 34, "bold"))
game_status_label.pack(side="bottom", anchor="s")

players_ratio_progress_bar = ctk.CTkProgressBar(info_frame, width=260, fg_color="red")
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
game_ended = False
def button_action(btn):
    global current_player
    btn.configure(state="disabled",fg_color="#222222")
    if btn.cget("text") == " ":
        if current_player == "X":
            btn.configure(text="X")
            game_status_label.configure(text="X's turn")
            current_player = "O"
        else:
            btn.configure(text="O")
            game_status_label.configure(text="O's turn")
            current_player = "X"
        blink_buttons(game_logic())
        if game_ended:
            window.after(1200, replay)






def add_buttons(frame=top_frame, fg_color="grey", text=" "):
    first_btn = ctk.CTkButton(frame, fg_color=fg_color, text=text, height= 114, width= 114,
                              command= lambda: button_action(first_btn), font=("Poppins", 34, "bold"), hover_color="#383838")
    first_btn.pack(side="left", expand=True)

    second_btn = ctk.CTkButton(frame, fg_color=fg_color,text=text, height= 114, width= 114,
                               command= lambda: button_action(second_btn), font=("Poppins", 34, "bold"), hover_color="#383838")
    second_btn.pack(side="left", expand=True)

    third_btn = ctk.CTkButton(frame, fg_color=fg_color, text=text, height= 114, width= 114,
                              command= lambda: button_action(third_btn), font=("Poppins", 34, "bold"), hover_color="#383838")
    third_btn.pack(side="left", expand=True)

    return first_btn, second_btn, third_btn

a1, a2, a3 = add_buttons()
b1, b2, b3 = add_buttons(mid_frame)
c1, c2, c3 = add_buttons(bottom_frame)

all_buttons = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
winning_patterns = [(a1, a2, a3), (a1, b1, c1), (a1, b2, c3), (a2, b2, c2), (a3, b3, c3), (b1, b2, b3), (c1, c2, c3),
                    (a3, b2, c1)]

def blink_buttons(buttons: tuple, time=200, blinks_left = 4):
    global game_ended
    if buttons is None:
        return
    a, b, c = buttons
    if blinks_left == 0:
        a.configure(fg_color="#1b633a")
        b.configure(fg_color="#1b633a")
        c.configure(fg_color="#1b633a")
        return
    if not blinks_left == 6:
        if a.cget("fg_color") == "#1b633a":
            a.configure(fg_color="#222222")
            b.configure(fg_color="#222222")
            c.configure(fg_color="#222222")
        else:
            a.configure(fg_color="#1b633a")
            b.configure(fg_color="#1b633a")
            c.configure(fg_color="#1b633a")

    window.after(time, blink_buttons, buttons, time, blinks_left-1)



def replay():
    for button in all_buttons:
        button.configure(state="normal")
        button.configure(command= lambda: reset_game(button))


def reset_game(button):
    for button in all_buttons:
        button.configure(text=" ", fg_color="grey")
        button.configure(command= lambda: button_action(button))







def game_logic():
    global game_ended
    for first, second, third in winning_patterns:
        if first.cget("text") == second.cget("text") == third.cget("text") != " ":
            first.configure(fg_color="#1b633a")
            second.configure(fg_color="#1b633a")
            third.configure(fg_color="#1b633a")
            for button in all_buttons:
                button.configure(state="disabled")
            game_status_label.configure(text=f"'{first.cget('text')}' Won!")
            if first.cget("text") == "X":
                first_player_score.configure(text=int(first_player_score.cget("text")) + 1)
            else:
                second_player_score.configure(text=int(second_player_score.cget("text")) + 1)
            try:
                players_ratio_progress_bar.set((int(first_player_score.cget("text")) + int(second_player_score.cget("text")))/int(first_player_score.cget("text")))
            except ZeroDivisionError:
                players_ratio_progress_bar.set(0)
            game_ended = True
            return first, second, third
    return None



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