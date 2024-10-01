import time
import random
import tkinter as tk
import webbrowser

def show_reminder(urls):
    root = tk.Tk()
    root.title("nobi")
    root.geometry("300x150")
    root.configure(bg='#f0f8ff')

    def open_random_url(event=None):
        url = random.choice(urls)
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
        root.destroy()  

    def close_reminder(event=None):
        root.destroy()  

    message = tk.Label(root, text="【リマインド】ストレッチしましょう", 
                       bg='#f0f8ff', fg='darkblue', font=('Arial', 12))
    message.pack(pady=10)

    open_button = tk.Button(root, text="ストレッチする(1)", command=open_random_url, 
                            bg='lightgreen', fg='black', font=('Arial', 10, 'bold'))
    open_button.pack(pady=5)

    close_button = tk.Button(root, text="閉じる(2)", command=close_reminder, 
                             bg='salmon', fg='black', font=('Arial', 10, 'bold'))
    close_button.pack(pady=5)

    root.bind('1', open_random_url)
    root.bind('2', close_reminder)

    root.focus_force() 
    root.mainloop()

def stretch_reminder(interval_minutes, urls):
    interval_seconds = interval_minutes * 60
    while True:
        time.sleep(interval_seconds)
        show_reminder(urls)

if __name__ == "__main__":
    urls = [
        "https://www.youtube.com/watch?v=tEVh6R29ORY",
        "https://www.youtube.com/watch?v=To1yijqZCCE",
        "https://www.youtube.com/watch?v=KaDsJF0qK6U",
        "https://www.youtube.com/watch?v=Vr1AdVWbrFA",
        "https://www.youtube.com/watch?v=tPJx1fgLLgI"  
    ]
    stretch_reminder(60, urls)  # Set reminder interval to x minutes
