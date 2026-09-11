import threading
import time
import tkinter as tk
import customtkinter as ctk
from pynput import keyboard as pynput_keyboard
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController

# --- INTERNATIONALIZATION 
LANGS = {
    "ENGLISH": {
        "title": "PALIA TOUR TICKETS", "start": "START MACRO", "stop": "STOP",
        "d_start": "START DELAY (S)", "d_act": "ACTION DELAY (S)", "d_fin": "FINAL DELAY (S)",
        "loops": "LOOPS", "hk": "HOTKEY", "k1": "KEY 1", "k2": "KEY 2",
        "idle": "IDLE"
    },
    "العربية": {
        "title": "PALIA TOUR TICKETS", "start": "تشغيل الماكرو", "stop": "إيقاف",
        "d_start": "تأخير البدء", "d_act": "تأخير الحركة", "d_fin": "التأخير النهائي",
        "loops": "التكرار", "hk": "مفتاح الاختصار", "k1": "المفتاح 1", "k2": "المفتاح 2",
        "idle": "خامل"
    },
    "FRANÇAIS": {
        "title": "PALIA TOUR TICKETS", "start": "LANCER MACRO", "stop": "ARRÊTER",
        "d_start": "DÉLAI INITIAL", "d_act": "DÉLAI D'ACTION", "d_fin": "DÉLAI FINAL",
        "loops": "BOUCLES", "hk": "RACCOURCI", "k1": "TOUCHE 1", "k2": "TOUCHE 2",
        "idle": "INACTIF"
    },
    "ESPAÑOL": {
        "title": "PALIA TOUR TICKETS", "start": "INICIAR MACRO", "stop": "PARAR",
        "d_start": "RETRASO INICIO", "d_act": "RETRASO ACCIÓN", "d_fin": "RETRASO FINAL",
        "loops": "ITERACIONES", "hk": "ATAJO", "k1": "TECLA 1", "k2": "TECLA 2",
        "idle": "INACTIVO"
    }
}

class EliteMacro(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- WINDOW CONFIG
        self.title("PALIA TICKET TOUR")
        self.geometry("480x800")
        ctk.set_appearance_mode("dark")
        
        # --- STYLE CONFIGURATION 
        self.primary = "#0000FF"
        self.bg_black = "#0D0D0D"
        self.r = 8  
        
        self.current_lang = "ENGLISH"
        self.setup_ui()
        self.init_logic()

    def setup_ui(self):
        self.configure(fg_color=self.bg_black)
        self.header = ctk.CTkFrame(self, fg_color=self.primary, corner_radius=self.r, height=90)
        self.header.pack(fill="x", padx=10, pady=10)
        
        self.title_label = ctk.CTkLabel(self.header, text=LANGS[self.current_lang]["title"], 
                                        font=ctk.CTkFont(size=22, weight="bold"), text_color="WHITE")
        self.title_label.pack(side="left", padx=20, pady=20)

        self.lang_selector = ctk.CTkOptionMenu(self.header, values=list(LANGS.keys()), 
                                               command=self.update_language, 
                                               corner_radius=self.r, fg_color="#1A1A1A", 
                                               button_color="#222", width=110)
        self.lang_selector.pack(side="right", padx=15)

        # MAIN CONTAINER
        self.main_container = ctk.CTkScrollableFrame(self, fg_color="#151515", 
                                                     corner_radius=self.r,
                                                     scrollbar_button_color=self.primary)
        self.main_container.pack(fill="both", expand=True, padx=15, pady=5)

        self.fields = [
            ("d_start", "3"), ("d_act", "0.15"), ("d_fin", "0.25"),
            ("loops", "50"), ("hk", "F6"), ("k1", "1"), ("k2", "5")
        ]
        
        self.inputs = {}
        self.label_objs = {}

        for key, default in self.fields:
            self.create_input_group(key, default)

        self.btn_start = ctk.CTkButton(self, text=LANGS[self.current_lang]["start"],
                                       fg_color=self.primary, hover_color="#0000CC",
                                       font=ctk.CTkFont(size=18, weight="bold"),
                                       height=55, corner_radius=self.r,
                                       command=self.start_macro)
        self.btn_start.pack(fill="x", padx=30, pady=(15, 5))

        self.btn_stop = ctk.CTkButton(self, text=LANGS[self.current_lang]["stop"],
                                      fg_color="#222", hover_color="#FF0000",
                                      height=45, corner_radius=self.r,
                                      command=self.stop_macro)
        self.btn_stop.pack(fill="x", padx=30, pady=(5, 15))

        # FOOTER
        self.status_bar = ctk.CTkFrame(self, fg_color="#111", height=35, corner_radius=self.r)
        self.status_bar.pack(fill="x", side="bottom", padx=10, pady=5)
        
        self.status_text = ctk.CTkLabel(self.status_bar, text=LANGS[self.current_lang]["idle"], 
                                        font=ctk.CTkFont(size=12, weight="bold"), text_color="#777")
        self.status_text.pack(expand=True)

    def create_input_group(self, key, default):
        frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        frame.pack(fill="x", pady=8, padx=10)
        
        lbl = ctk.CTkLabel(frame, text=LANGS[self.current_lang][key], 
                           font=ctk.CTkFont(size=11, weight="bold"), text_color="#888")
        lbl.pack(anchor="w", padx=5)
        
        entry = ctk.CTkEntry(frame, fg_color="#0A0A0A", border_color="#333", 
                             border_width=1, corner_radius=self.r, height=42)
        entry.insert(0, default.upper())
        entry.pack(fill="x", pady=2)
        
        entry.bind("<FocusIn>", lambda e, en=entry: en.configure(border_color=self.primary))
        entry.bind("<FocusOut>", lambda e, en=entry: en.configure(border_color="#333"))
        
        self.inputs[key] = entry
        self.label_objs[key] = lbl

    def update_language(self, choice):
        self.current_lang = choice
        self.title_label.configure(text=LANGS[choice]["title"])
        self.btn_start.configure(text=LANGS[choice]["start"])
        self.btn_stop.configure(text=LANGS[choice]["stop"])
        self.status_text.configure(text=LANGS[choice]["idle"])
        for key, obj in self.label_objs.items():
            obj.configure(text=LANGS[choice][key])

    def init_logic(self):
        self.kb = KeyboardController()
        self.ms = MouseController()
        self.stop_evt = threading.Event()
        threading.Thread(target=self.hotkey_listener, daemon=True).start()

    def hotkey_listener(self):
        def on_press(key):
            try:
                trigger = self.inputs["hk"].get().lower()
                if (hasattr(key, 'name') and key.name == trigger) or (hasattr(key, 'char') and key.char == trigger):
                    self.start_macro()
            except: pass
        with pynput_keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def start_macro(self):
        self.stop_evt.clear()
        threading.Thread(target=self.run_logic, daemon=True).start()

    def stop_macro(self):
        self.stop_evt.set()

    def run_logic(self):
        try:
            loops = int(self.inputs["loops"].get())
            k1, k2 = self.inputs["k1"].get(), self.inputs["k2"].get()
            d_s, d_a = float(self.inputs["d_start"].get()), float(self.inputs["d_act"].get())
            d_f = float(self.inputs["d_fin"].get())
        except: return

        self.status_text.configure(text="● RUNNING", text_color=self.primary)
        time.sleep(d_s)

        for i in range(loops):
            if self.stop_evt.is_set(): break
            for k in [k1, k2]:
                self.kb.press(k); self.kb.release(k)
                time.sleep(d_a)
                self.ms.click(Button.left)
                time.sleep(d_a)
            time.sleep(d_f)
        
        self.status_text.configure(text=LANGS[self.current_lang]["idle"], text_color="#777")

if __name__ == "__main__":
    app = EliteMacro()
    app.mainloop()