from app import App

app = App()

screenW, screenH = app.winfo_screenwidth(), app.winfo_screenheight() 
windowW = screenW*4//5
windowH = windowW*1080//1920
app.geometry(f"{windowW}x{windowH}+{screenW//2-windowW//2}+{screenH//2-windowH//2-windowH//20}")

app.state("zoomed")
app.mainloop()