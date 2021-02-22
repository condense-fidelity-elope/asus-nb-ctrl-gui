import os
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Asus NB CTRL GUI")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        SilentButton=tk.Button(root)
        SilentButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=16)
        SilentButton["font"] = ft
        SilentButton["fg"] = "#000000"
        SilentButton["justify"] = "center"
        SilentButton["text"] = "Silent"
        SilentButton.place(x=30,y=90,width=120,height=100)
        SilentButton["command"] = self.SilentButton_command

        IntegratedButton=tk.Button(root)
        IntegratedButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=16)
        IntegratedButton["font"] = ft
        IntegratedButton["fg"] = "#000000"
        IntegratedButton["justify"] = "center"
        IntegratedButton["text"] = "Integrated"
        IntegratedButton.place(x=170,y=90,width=120,height=100)
        IntegratedButton["command"] = self.IntegratedButton_command

        CHG60Button=tk.Button(root)
        CHG60Button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=16)
        CHG60Button["font"] = ft
        CHG60Button["fg"] = "#000000"
        CHG60Button["justify"] = "center"
        CHG60Button["text"] = "60"
        CHG60Button.place(x=310,y=90,width=120,height=100)
        CHG60Button["command"] = self.CHG60Button_command

        HybridButton=tk.Button(root)
        HybridButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=16)
        HybridButton["font"] = ft
        HybridButton["fg"] = "#000000"
        HybridButton["justify"] = "center"
        HybridButton["text"] = "Hybird"
        HybridButton.place(x=170,y=200,width=120,height=100)
        HybridButton["command"] = self.HybridButton_command

        CHG100Button=tk.Button(root)
        CHG100Button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=16)
        CHG100Button["font"] = ft
        CHG100Button["fg"] = "#000000"
        CHG100Button["justify"] = "center"
        CHG100Button["text"] = "100"
        CHG100Button.place(x=310,y=310,width=120,height=100)
        CHG100Button["command"] = self.CHG100Button_command
        

        CHG80Button=tk.Button(root)
        CHG80Button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=16)
        CHG80Button["font"] = ft
        CHG80Button["fg"] = "#000000"
        CHG80Button["justify"] = "center"
        CHG80Button["text"] = "80"
        CHG80Button.place(x=310,y=200,width=120,height=100)
        CHG80Button["command"] = self.CHG80Button_command

        NvidiaButton=tk.Button(root)
        NvidiaButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=16)
        NvidiaButton["font"] = ft
        NvidiaButton["fg"] = "#000000"
        NvidiaButton["justify"] = "center"
        NvidiaButton["text"] = "Nvidia"
        NvidiaButton.place(x=170,y=310,width=120,height=100)
        NvidiaButton["command"] = self.NvidiaButton_command

        BoostButton=tk.Button(root)
        BoostButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=16)
        BoostButton["font"] = ft
        BoostButton["fg"] = "#000000"
        BoostButton["justify"] = "center"
        BoostButton["text"] = "Boost"
        BoostButton.place(x=30,y=310,width=120,height=100)
        BoostButton["command"] = self.BoostButton_command

        MediumButton=tk.Button(root)
        MediumButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=16)
        MediumButton["font"] = ft
        MediumButton["fg"] = "#000000"
        MediumButton["justify"] = "center"
        MediumButton["text"] = "Medium"
        MediumButton.place(x=450,y=200,width=120,height=100)
        MediumButton["command"] = self.MediumButton_command

        OffButton=tk.Button(root)
        OffButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=16)
        OffButton["font"] = ft
        OffButton["fg"] = "#000000"
        OffButton["justify"] = "center"
        OffButton["text"] = "Off"
        OffButton.place(x=450,y=420,width=120,height=0)
        OffButton["command"] = self.OffButton_command

        HighButton=tk.Button(root)
        HighButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=16)
        HighButton["font"] = ft
        HighButton["fg"] = "#000000"
        HighButton["justify"] = "center"
        HighButton["text"] = "High"
        HighButton.place(x=450,y=310,width=120,height=100)
        HighButton["command"] = self.HighButton_command

        LowButton=tk.Button(root)
        LowButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=16)
        LowButton["font"] = ft
        LowButton["fg"] = "#000000"
        LowButton["justify"] = "center"
        LowButton["text"] = "Low"
        LowButton.place(x=450,y=90,width=120,height=100)
        LowButton["command"] = self.LowButton_command

        NormalButton=tk.Button(root)
        NormalButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=16)
        NormalButton["font"] = ft
        NormalButton["fg"] = "#000000"
        NormalButton["justify"] = "center"
        NormalButton["text"] = "Normal"
        NormalButton.place(x=30,y=200,width=120,height=100)
        NormalButton["command"] = self.NormalButton_command

        GLabel_900=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12)
        GLabel_900["font"] = ft
        GLabel_900["fg"] = "#333333"
        GLabel_900["justify"] = "center"
        GLabel_900["text"] = "Graphics Mode"
        GLabel_900.place(x=180,y=50,width=110,height=31)

        GLabel_300=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12)
        GLabel_300["font"] = ft
        GLabel_300["fg"] = "#333333"
        GLabel_300["justify"] = "center"
        GLabel_300["text"] = ""
        GLabel_300.place(x=50,y=50,width=0,height=0)

        GLabel_400=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12)
        GLabel_400["font"] = ft
        GLabel_400["fg"] = "#333333"
        GLabel_400["justify"] = "center"
        GLabel_400["text"] = "Charge Limit"
        GLabel_400.place(x=320,y=50,width=95,height=30)

        GLabel_600=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12)
        GLabel_600["font"] = ft
        GLabel_600["fg"] = "#333333"
        GLabel_600["justify"] = "center"
        GLabel_600["text"] = "Kbd Brightness"
        GLabel_600.place(x=450,y=50,width=121,height=30)

        GLabel_500=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12)
        GLabel_500["font"] = ft
        GLabel_500["fg"] = "#333333"
        GLabel_500["justify"] = "center"
        GLabel_500["text"] = "Fan Mode"
        GLabel_500.place(x=50,y=50,width=78,height=30)

    def SilentButton_command(self):
        os.system("asusctl profile silent")


    def IntegratedButton_command(self):
        os.system("asusctl graphics -m integrated")


    def CHG60Button_command(self):
        os.system("asusctl -c 60")

    
    def OffButton_command(self):
        os.system("asusctl -k off")


    def HybridButton_command(self):
        os.system("asusctl graphics -m hybrid")


    def CHG100Button_command(self):
        os.system("asusctl -c 100")


    def CHG80Button_command(self):
        os.system("asusctl -c 80")


    def NvidiaButton_command(self):
        os.system("asusctl graphics -m nvidia")


    def BoostButton_command(self):
        os.system("asusctl profile boost")
    
    def HighButton_command(self):
        os.system("asusctl -k High")
    
    
    def MediumButton_command(self):
        os.system("asusctl -k med")


    def LowButton_command(self):
        os.system("asusctl -k low")


    def NormalButton_command(self):
        os.system("asusctl profile normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
