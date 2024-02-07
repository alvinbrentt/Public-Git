import pytube
import tkinter
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()

def download_video(url):
    pass


window.title("YouTube Downloader")
window.geometry("720x480")

page_title = customtkinter.CTkLabel(master=window, width=100, height=50,  text="YouTube Downloader", font=("Roboto", 35))
page_title.pack(pady=40)

url = tkinter.StringVar()
url_input = customtkinter.CTkEntry(master=window, width=300, height=50, placeholder_text="URL", textvariable=url)
url_input.pack()


download_button = customtkinter.CTkButton(master=window, width=100, height=50, corner_radius=32, border_width=3, border_color="red", fg_color="transparent", text="Download")
download_button.pack(pady=20)

window.mainloop()