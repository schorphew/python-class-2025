import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext 
import datetime
import json
import os
import random
import string
import base64

# ============ LANGUAGES ============
LANGUAGES = {
    "TH": {
        "app_title": "🚆 ระบบจองตั๋วรถไฟ", "login": "👤 เข้าสู่ระบบ", "manage_bookings": "📋 จัดการการจอง",
        "statistics": "📊 สถิติ", "contact": "📞 ติดต่อเรา", "dark_mode": "🌙 โหมดมืด", "logout": "🚪 ออกจากระบบ",
        "not_logged_in": "👤 ยังไม่ได้เข้าสู่ระบบ", "user_info": "👤 {name} | ⭐ {points} คะแนน",
        "travel_info": "📝 ข้อมูลการเดินทาง", "passenger_name": "ชื่อผู้โดยสาร:", "num_adults": "จำนวนผู้ใหญ่:",
        "num_children": "จำนวนเด็ก:", "num_seniors": "จำนวนผู้สูงอายุ:", "route": "สายรถไฟ:", "from_station": "จาก:",
        "to_station": "ไป:", "travel_date": "วันที่เดินทาง:", "train_round": "รอบรถไฟ:", "seat_class": "ประเภทที่นั่ง:",
        "sleeper_position": "ตำแหน่ง (นอน):", "seats_available": "ที่นั่งคงเหลือ: {available}/30", "next_seat_selection": "🎫 ถัดไป → เลือกที่นั่ง",
        "promotions_title": "🎁 โปรโมชั่น", "promo_discount_percent": "'{code}' ลด {discount}%", "promo_discount_baht": "'{code}' ลด {discount} บาท",
        "promo_info": "💡 สะสมคะแนน | 🍱 สั่งอาหาร | 🎫 QR Code", "footer": "© 2025 | Python + Tkinter | 📞 1690",
        "login_title": "🔐 เข้าสู่ระบบ", "username": "ชื่อผู้ใช้:", "password": "รหัสผ่าน:", "login_button": "เข้าสู่ระบบ",
        "register_button": "สมัครสมาชิก", "welcome": "ยินดีต้อนรับ {name}!", "login_error": "ข้อมูลไม่ถูกต้อง",
        "register_title": "📝 สมัครสมาชิก", "full_name": "ชื่อ-นามสกุล:", "phone": "เบอร์โทร:", "email": "อีเมล:",
        "fill_all_fields": "กรอกข้อมูลให้ครบ", "username_exists": "มีชื่อนี้แล้ว", "register_success": "สมัครสำเร็จ!",
        "bookings_title": "📋 การจองทั้งหมด", "search": "🔍 ค้นหา:", "cancel_booking": "❌ ยกเลิก", "refresh": "🔄 รีเฟรช",
        "no_bookings": "ไม่มีการจอง", "select_booking": "เลือกรายการ", "confirm_cancel": "ยกเลิก {booking_id}?",
        "cancel_success": "ยกเลิกแล้ว", "stats_title": "📊 สถิติ", "save_report": "💾 บันทึก", "report_saved": "บันทึก {filename}",
        "food_order_title": "🍱 สั่งอาหาร", "food_subtitle": "📌 ส่งถึงที่นั่ง", "food_total": "💰 รวม: {total} บาท",
        "confirm_food": "✅ ยืนยัน", "skip_food": "⏭️ ข้าม", "food_success": "สั่งแล้ว!\n{total} บาท", "order_food_question": "🍱 สั่งอาหารไหม?",
        "seat_selection_title": "🪑 เลือกที่นั่ง", "select_seats_for": "เลือกที่นั่ง ({count} คน)", "aisle": "  ทางเดิน  ",
        "seat_available": "ว่าง", "seat_selected": "เลือกแล้ว", "seat_booked": "จองแล้ว", "seat_confirmed": "ยืนยันแล้ว",
        "seat_taken": "{seat} จองแล้ว", "max_seats": "สูงสุด {max} ที่", "confirm_seats": "✅ ยืนยัน ({selected}/{total})",
        "select_all_seats": "เลือก {total} ที่ (เลือกแล้ว {selected})", "seats_confirmed": "เลือกเรียบร้อย",
        "payment_title": "💳 ชำระเงิน", "payment_summary": "สรุป", "ticket_price": "ตั๋ว: {price:.2f}", "food_price": "อาหาร: {price:.2f}",
        "total": "รวม: {total:.2f}", "group_discount": "🎉 ส่วนลดกลุ่ม! ({count} คน)", "family_discount": "🎉 ส่วนลดครอบครัว! ({count} คน)",
        "promo_code": "🎁 โค้ด:", "use_code": "ใช้", "enter_promo": "ใส่โค้ด", "invalid_promo": "'{code}' ไม่ถูกต้อง",
        "promo_applied": "✅ ใช้ '{code}' แล้ว!\n\nลด: {discount:.2f}", "discount": "ส่วนลด", "vat": "VAT 7%: {vat:.2f}",
        "net_total": "สุทธิ: {total:.2f}", "payment_method": "วิธีชำระ:", "credit_card": "💳 บัตร", "bank_transfer": "🏦 โอน",
        "qr_payment": "📱 QR", "cash": "💵 เงินสด", "confirm_payment": "✅ ยืนยัน", "ticket_title": "🎫 จองสำเร็จ",
        "booking_id": "📋 รหัส: {id}", "expense_summary": "💰 สรุป", "ticket_fee": "ตั๋ว ({count} ใบ)", "food_fee": "อาหาร",
        "subtotal": "รวม", "points_earned": "⭐ +{points} คะแนน", "save_ticket": "💾 บันทึก", "show_qr": "🎫 QR",
        "manage_booking": "📋 จัดการ", "close": "❌ ปิด", "ticket_saved": "บันทึก: {filename}", "contact_title": "📞 ติดต่อ",
        "send_message": "📝 ส่งข้อความ", "send": "📤 ส่ง", "message_sent": "ขอบคุณ!\nติดต่อกลับใน 24 ชม.",
        "error": "ผิดพลาด", "warning": "เตือน", "success": "สำเร็จ", "confirm": "ยืนยัน", "enter_name": "ใส่ชื่อ",
        "invalid_tickets": "จำนวนไม่ถูกต้อง", "same_station": "สถานีซ้ำ", "invalid_date": "วันที่ไม่ถูกต้อง", "seats_full": "เหลือ {available} ที่!",
        "passenger_types": {"ผู้ใหญ่": "ผู้ใหญ่", "เด็ก": "เด็ก", "ผู้สูงอายุ": "ผู้สูงอายุ"},
        "seat_classes": {"ชั้น 2": "ชั้น 2", "ชั้น 1": "ชั้น 1", "นอน": "นอน"},
        "upper_lower": {"บน": "บน", "ล่าง": "ล่าง"}, "status_confirmed": "ยืนยัน", "thank_you": "ขอบคุณ 🚆",
    },
    "EN": {
        "app_title": "🚆 Train Booking", "login": "👤 Login", "manage_bookings": "📋 Bookings", "statistics": "📊 Stats",
        "contact": "📞 Contact", "dark_mode": "🌙 Dark", "logout": "🚪 Logout", "not_logged_in": "👤 Not logged in",
        "user_info": "👤 {name} | ⭐ {points} pts", "travel_info": "📝 Travel Info", "passenger_name": "Name:",
        "num_adults": "Adults:", "num_children": "Children:", "num_seniors": "Seniors:", "route": "Route:", "from_station": "From:",
        "to_station": "To:", "travel_date": "Date:", "train_round": "Time:", "seat_class": "Class:", "sleeper_position": "Position:",
        "seats_available": "Available: {available}/30", "next_seat_selection": "🎫 Next → Seats", "promotions_title": "🎁 Promotions",
        "promo_discount_percent": "'{code}' {discount}% off", "promo_discount_baht": "'{code}' {discount} THB off",
        "promo_info": "💡 Points | 🍱 Food | 🎫 QR", "footer": "© 2025 | Python + Tkinter | 📞 1690", "login_title": "🔐 Login",
        "username": "Username:", "password": "Password:", "login_button": "Login", "register_button": "Register",
        "welcome": "Welcome {name}!", "login_error": "Invalid credentials", "register_title": "📝 Register", "full_name": "Full Name:",
        "phone": "Phone:", "email": "Email:", "fill_all_fields": "Fill all fields", "username_exists": "Username exists",
        "register_success": "Success!", "bookings_title": "📋 All Bookings", "search": "🔍 Search:", "cancel_booking": "❌ Cancel",
        "refresh": "🔄 Refresh", "no_bookings": "No bookings", "select_booking": "Select booking", "confirm_cancel": "Cancel {booking_id}?",
        "cancel_success": "Cancelled", "stats_title": "📊 Statistics", "save_report": "💾 Save", "report_saved": "Saved {filename}",
        "food_order_title": "🍱 Order Food", "food_subtitle": "📌 Delivered to seat", "food_total": "💰 Total: {total} THB",
        "confirm_food": "✅ Confirm", "skip_food": "⏭️ Skip", "food_success": "Ordered!\n{total} THB", "order_food_question": "🍱 Order food?",
        "seat_selection_title": "🪑 Select Seats", "select_seats_for": "Select seats ({count} ppl)", "aisle": "  Aisle  ",
        "seat_available": "Available", "seat_selected": "Selected", "seat_booked": "Booked", "seat_confirmed": "Confirmed",
        "seat_taken": "{seat} taken", "max_seats": "Max {max}", "confirm_seats": "✅ Confirm ({selected}/{total})",
        "select_all_seats": "Select {total} (selected {selected})", "seats_confirmed": "Confirmed", "payment_title": "💳 Payment",
        "payment_summary": "Summary", "ticket_price": "Ticket: {price:.2f}", "food_price": "Food: {price:.2f}", "total": "Total: {total:.2f}",
        "group_discount": "🎉 Group! ({count})", "family_discount": "🎉 Family! ({count})", "promo_code": "🎁 Code:", "use_code": "Apply",
        "enter_promo": "Enter code", "invalid_promo": "'{code}' invalid", "promo_applied": "✅ '{code}' applied!\n\n-{discount:.2f}",
        "discount": "Discount", "vat": "VAT 7%: {vat:.2f}", "net_total": "Net: {total:.2f}", "payment_method": "Method:",
        "credit_card": "💳 Card", "bank_transfer": "🏦 Transfer", "qr_payment": "📱 QR", "cash": "💵 Cash",
        "confirm_payment": "✅ Confirm", "ticket_title": "🎫 Booked", "booking_id": "📋 ID: {id}", "expense_summary": "💰 Summary",
        "ticket_fee": "Tickets ({count})", "food_fee": "Food", "subtotal": "Subtotal", "points_earned": "⭐ +{points} pts",
        "save_ticket": "💾 Save", "show_qr": "🎫 QR", "manage_booking": "📋 Manage", "close": "❌ Close",
        "ticket_saved": "Saved: {filename}", "contact_title": "📞 Contact", "send_message": "📝 Message", "send": "📤 Send",
        "message_sent": "Thanks!\nWe'll reply in 24h", "error": "Error", "warning": "Warning", "success": "Success",
        "confirm": "Confirm", "enter_name": "Enter name", "invalid_tickets": "Invalid number", "same_station": "Same station",
        "invalid_date": "Invalid date", "seats_full": "Only {available} left!", "passenger_types": {"ผู้ใหญ่": "Adult", "เด็ก": "Child", "ผู้สูงอายุ": "Senior"},
        "seat_classes": {"ชั้น 2": "Class 2", "ชั้น 1": "Class 1", "นอน": "Sleeper"},
        "upper_lower": {"บน": "Upper", "ล่าง": "Lower"}, "status_confirmed": "Confirmed", "thank_you": "Thanks 🚆",
    }
}

def t(key, **kwargs):
    text = LANGUAGES.get(current_language, LANGUAGES["TH"]).get(key, key)
    return text.format(**kwargs) if kwargs else text

# ============ DATABASE ============
class Database:
    def __init__(self):
        self.bookings_file = "bookings.json"
        self.users_file = "users.json"
        self.promotions_file = "promotions.json"
        self.food_menu_file = "food_menu.json"
        self.init_files()
    
    def init_files(self):
        for file, data in [(self.bookings_file, []), (self.users_file, {}),
                           (self.promotions_file, [{"code": "WELCOME10", "discount": 10, "type": "percent"},
                        {"code": "SAVE50", "discount": 50, "type": "baht"},
                        {"code": "FAMILY15", "discount": 15, "type": "percent", "min_tickets": 3},
                        {"code": "GROUP20", "discount": 20, "type": "percent", "min_tickets": 5}]),
                           (self.food_menu_file, [{"id": i+1, "name": n, "name_en": ne, "price": p, "category": c}
                                                  for i, (n, ne, p, c) in enumerate([
                                                      ("ข้าวผัด", "Fried Rice", 80, "อาหาร"), ("ก๋วยเตี๋ยว", "Noodle", 60, "อาหาร"),
                                                      ("แซนด์วิช", "Sandwich", 50, "อาหาร"), ("กาแฟ", "Coffee", 35, "เครื่องดื่ม"),
                                                      ("น้ำส้ม", "Orange Juice", 30, "เครื่องดื่ม"), ("ขนม", "Snack", 25, "ของว่าง")])])]:
            if not os.path.exists(file):
                with open(file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False)
    
    def save_booking(self, booking):
        bookings = self.load_bookings()
        bookings.append(booking)
        with open(self.bookings_file, 'w', encoding='utf-8') as f:
            json.dump(bookings, f, ensure_ascii=False, indent=2)
    
    def load_bookings(self):
        try:
            with open(self.bookings_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    
    def cancel_booking(self, booking_id):
        bookings = [b for b in self.load_bookings() if b.get('booking_id') != booking_id]
        with open(self.bookings_file, 'w', encoding='utf-8') as f:
            json.dump(bookings, f, ensure_ascii=False, indent=2)
    
    def save_user(self, username, user_data):
        users = self.load_users()
        users[username] = user_data
        with open(self.users_file, 'w', encoding='utf-8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)
    
    def load_users(self):
        try:
            with open(self.users_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    
    def load_promotions(self):
        try:
            with open(self.promotions_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    
    def load_food_menu(self):
        try:
            with open(self.food_menu_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []

db = Database()

# ============ SETUP ============
root = tk.Tk()
root.title("🚆 Train Booking")
root.geometry("1200x800")
root.configure(bg="#f0f4f8")

current_user = {"username": None, "name": "", "points": 0}
is_dark_mode = False
current_language = "TH"
food_orders = []

station_names = {
    "TH": {k: k for k in ["กรุงเทพฯ","อยุธยา","ลพบุรี","นครสวรรค์","พิษณุโลก","อุตรดิตถ์","ลำปาง","ลำพูน","เชียงใหม่","สระบุรี","นครราชสีมา","บุรีรัมย์","สุรินทร์","ศรีสะเกษ","อุบลราชธานี","ราชบุรี","เพชรบุรี","หัวหิน","ชุมพร","สุราษฎร์ธานี","นครศรีธรรมราช","หาดใหญ่","ยะลา"]},
    "EN": dict(zip(["กรุงเทพฯ","อยุธยา","ลพบุรี","นครสวรรค์","พิษณุโลก","อุตรดิตถ์","ลำปาง","ลำพูน","เชียงใหม่","สระบุรี","นครราชสีมา","บุรีรัมย์","สุรินทร์","ศรีสะเกษ","อุบลราชธานี","ราชบุรี","เพชรบุรี","หัวหิน","ชุมพร","สุราษฎร์ธานี","นครศรีธรรมราช","หาดใหญ่","ยะลา"],
                   ["Bangkok","Ayutthaya","Lopburi","Nakhon Sawan","Phitsanulok","Uttaradit","Lampang","Lamphun","Chiang Mai","Saraburi","Nakhon Ratchasima","Buriram","Surin","Sisaket","Ubon","Ratchaburi","Phetchaburi","Hua Hin","Chumphon","Surat Thani","Nakhon Si","Hat Yai","Yala"]))
}

route_names = {
    "TH": {"สายเหนือ": "สายเหนือ", "สายตะวันออกเฉียงเหนือ": "สายตะวันออกเฉียงเหนือ", "สายใต้": "สายใต้"},
    "EN": {"สายเหนือ": "Northern", "สายตะวันออกเฉียงเหนือ": "Northeastern", "สายใต้": "Southern"}
}

routes = {
    "สายเหนือ": ["กรุงเทพฯ","อยุธยา","ลพบุรี","นครสวรรค์","พิษณุโลก","อุตรดิตถ์","ลำปาง","ลำพูน","เชียงใหม่"],
    "สายตะวันออกเฉียงเหนือ": ["กรุงเทพฯ","สระบุรี","นครราชสีมา","บุรีรัมย์","สุรินทร์","ศรีสะเกษ","อุบลราชธานี"],
    "สายใต้": ["กรุงเทพฯ","ราชบุรี","เพชรบุรี","หัวหิน","ชุมพร","สุราษฎร์ธานี","นครศรีธรรมราช","หาดใหญ่","ยะลา"]
}

train_rounds = ["06:00","08:00","10:00","12:00","14:00","16:00","18:00","20:00"]
tickets = []
all_booked_seats = {}

def get_station_name(k): return station_names.get(current_language, station_names["TH"]).get(k, k)
def get_route_name(k): return route_names.get(current_language, route_names["TH"]).get(k, k)
def get_station_key(d): return {v: k for k, v in station_names.get(current_language, station_names["TH"]).items()}.get(d, d)
def get_route_key(d): return {v: k for k, v in route_names.get(current_language, route_names["TH"]).items()}.get(d, list(routes.keys())[0])
def generate_booking_id(): return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
def create_simple_qr(text, size=10):
    encoded = base64.b64encode(text.encode()).decode()[:50]
    random.seed(encoded)
    return "\n".join(["█" * (size + 2)] + ["█" + "".join("█" if random.random() > 0.5 else " " for _ in range(size)) + "█" for _ in range(size)] + ["█" * (size + 2)])

def class_multiplier(sc, st=None):
    if sc == t("seat_classes")["ชั้น 2"]: sc = "ชั้น 2"
    elif sc == t("seat_classes")["ชั้น 1"]: sc = "ชั้น 1"
    elif sc == t("seat_classes")["นอน"]: sc = "นอน"
    return {"ชั้น 2":1.0,"ชั้น 1":1.5,"นอน":2.0}.get(sc, 1.0)

def passenger_discount(p): return {"ผู้ใหญ่":1.0,"เด็ก":0.5,"ผู้สูงอายุ":0.7}.get(p, 1.0)
def estimate_distance(f, t, rl):
    try: return abs(rl.index(f) - rl.index(t))*100+50
    except: return 200
def calculate_points(price): return int(price * 0.1)

# ============ THEME ============
def apply_theme():
    s = ttk.Style(root)
    s.theme_use("clam")
    bg = "#1a1a2e" if is_dark_mode else "#f0f4f8"
    root.configure(bg=bg)
    s.configure("TButton", font=("Arial",11,"bold"), background="#0f3460" if is_dark_mode else "#457b9d", foreground="white")
    s.configure("TLabel", background=bg, font=("Arial",10))

def toggle_dark_mode():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    apply_theme()
    messagebox.showinfo(t("dark_mode"), f"{t('dark_mode')}: {'on' if is_dark_mode else 'off'}")

# ============ LANGUAGE ============
def change_language():
    global current_language
    current_language = "EN" if current_language == "TH" else "TH"
    update_ui_language()
    messagebox.showinfo(t("success"), f"→ {'English' if current_language == 'EN' else 'ไทย'}")

def update_ui_language():
    root.title(t("app_title"))
    header_label.config(text=t("app_title"))
    for btn, key in [(menu_button_login, "login"), (menu_button_bookings, "manage_bookings"),
                     (menu_button_stats, "statistics"), (menu_button_contact, "contact"),
                     (menu_button_dark, "dark_mode"), (menu_button_logout, "logout")]:
        btn.config(text=t(key))
    update_user_label()
    main_frame.config(text=t("travel_info"))
    for lbl, key in [(label_name, "passenger_name"), (label_adult, "num_adults"), (label_child, "num_children"),
                     (label_senior, "num_seniors"), (label_route, "route"), (label_from, "from_station"),
                     (label_to, "to_station"), (label_date, "travel_date"), (label_round, "train_round"),
                     (label_class, "seat_class"), (label_upper_lower, "sleeper_position")]:
        lbl.config(text=t(key))
    btn_book.config(text=t("next_seat_selection"))
    info_frame.config(text=t("promotions_title"))
    update_promo_text()
    footer.config(text=t("footer"))
    
    route_keys = list(routes.keys())
    route_display = [get_route_name(r) for r in route_keys]
    curr_idx = combo_route.current()
    combo_route['values'] = route_display
    combo_route.current(curr_idx)
    on_route_change()
    
    seat_display = [t("seat_classes")[k] for k in ["ชั้น 2", "ชั้น 1", "นอน"]]
    curr_class = combo_class.current()
    combo_class['values'] = seat_display
    combo_class.current(curr_class)
    
    if combo_upper_lower['state'] != 'disabled':
        sleeper_display = [t("upper_lower")[k] for k in ["บน", "ล่าง"]]
        curr_sleeper = combo_upper_lower.current()
        combo_upper_lower['values'] = sleeper_display
        if curr_sleeper >= 0: combo_upper_lower.current(curr_sleeper)
    update_available_seats()

def update_promo_text():
    promos = db.load_promotions()
    txt = ""
    for p in promos:
        if p['type'] == 'percent': txt += t('promo_discount_percent', code=p['code'], discount=p['discount']) + " | "
        else: txt += t('promo_discount_baht', code=p['code'], discount=p['discount']) + " | "
    promo_label.config(text=txt[:-3])
    promo_info_label.config(text=t("promo_info"))

# ============ AUTH ============
def show_login_window():
    win = tk.Toplevel(root)
    win.title(t("login_title"))
    win.geometry("400x280")
    win.configure(bg="#f0f4f8")
    win.transient(root)
    win.grab_set()
    
    tk.Label(win, text=t("login_title"), font=("Arial", 16, "bold"), bg="#f0f4f8").pack(pady=15)
    f = tk.Frame(win, bg="#f0f4f8")
    f.pack(pady=15)
    
    tk.Label(f, text=t("username"), bg="#f0f4f8").grid(row=0, column=0, pady=8, sticky="e")
    e_user = tk.Entry(f, width=22)
    e_user.grid(row=0, column=1, pady=8, padx=8)
    
    tk.Label(f, text=t("password"), bg="#f0f4f8").grid(row=1, column=0, pady=8, sticky="e")
    e_pass = tk.Entry(f, width=22, show="*")
    e_pass.grid(row=1, column=1, pady=8, padx=8)
    
    def login():
        u, p = e_user.get().strip(), e_pass.get().strip()
        users = db.load_users()
        if u in users and users[u].get('password') == p:
            current_user.update({'username': u, 'name': users[u].get('name', u), 'points': users[u].get('points', 0)})
            update_user_label()
            messagebox.showinfo(t("success"), t("welcome", name=current_user['name']))
            win.destroy()
        else:
            messagebox.showerror(t("error"), t("login_error"))
    
    bf = tk.Frame(win, bg="#f0f4f8")
    bf.pack(pady=15)
    tk.Button(bf, text=t("login_button"), command=login, bg="#457b9d", fg="white", font=("Arial", 10, "bold"), padx=18, pady=4).grid(row=0, column=0, padx=8)
    tk.Button(bf, text=t("register_button"), command=lambda: [win.destroy(), show_register_window()], bg="#2a9d8f", fg="white", font=("Arial", 10, "bold"), padx=18, pady=4).grid(row=0, column=1, padx=8)

def show_register_window():
    win = tk.Toplevel(root)
    win.title(t("register_title"))
    win.geometry("420x380")
    win.configure(bg="#f0f4f8")
    win.transient(root)
    win.grab_set()
    
    tk.Label(win, text=t("register_title"), font=("Arial", 16, "bold"), bg="#f0f4f8").pack(pady=15)
    f = tk.Frame(win, bg="#f0f4f8")
    f.pack(pady=10)
    
    fields = [(t("full_name"), "name"), (t("username"), "username"), (t("password"), "password"), (t("phone"), "phone"), (t("email"), "email")]
    entries = {}
    for i, (lbl, key) in enumerate(fields):
        tk.Label(f, text=lbl, bg="#f0f4f8").grid(row=i, column=0, pady=6, sticky="e")
        e = tk.Entry(f, width=26, show="*" if key == "password" else "")
        e.grid(row=i, column=1, pady=6, padx=8)
        entries[key] = e
    
    def save_reg():
        data = {k: e.get().strip() for k, e in entries.items()}
        if not all(data.values()):
            messagebox.showwarning(t("error"), t("fill_all_fields"))
            return
        users = db.load_users()
        if data['username'] in users:
            messagebox.showerror(t("error"), t("username_exists"))
            return
        data.update({'points': 0, 'register_date': datetime.date.today().strftime("%Y-%m-%d")})
        db.save_user(data['username'], data)
        messagebox.showinfo(t("success"), t("register_success"))
        win.destroy()
        show_login_window()
    
    tk.Button(win, text=t("register_button"), command=save_reg, bg="#2a9d8f", fg="white", font=("Arial", 11, "bold"), padx=25, pady=6).pack(pady=15)

def logout():
    current_user.update({'username': None, 'name': "", 'points': 0})
    update_user_label()
    messagebox.showinfo(t("logout"), t("logout"))

def update_user_label():
    user_label.config(text=t("user_info", name=current_user['name'], points=current_user['points']) if current_user['username'] else t("not_logged_in"))

# ============ BOOKINGS ============
def show_bookings_window():
    bookings = db.load_bookings()
    if current_user['username']:
        bookings = [b for b in bookings if b.get('username') == current_user['username']]
    if not bookings:
        messagebox.showinfo(t("manage_bookings"), t("no_bookings"))
        return
    
    win = tk.Toplevel(root)
    win.title(t("bookings_title"))
    win.geometry("1000x550")
    win.configure(bg="#f0f4f8")
    
    tk.Label(win, text=t("bookings_title"), bg="#1d3557", fg="white", font=("Arial", 14, "bold"), pady=8).pack(fill="x")
    
    sf = tk.Frame(win, bg="#f0f4f8")
    sf.pack(pady=8)
    tk.Label(sf, text=t("search"), bg="#f0f4f8").pack(side="left", padx=4)
    se = tk.Entry(sf, width=25)
    se.pack(side="left", padx=4)
    
    f = tk.Frame(win, bg="white")
    f.pack(fill="both", expand=True, padx=15, pady=8)
    
    cols = ("ID", "Name", "From", "To", "Date", "Time", "Seat", "Price", "Status")
    tree = ttk.Treeview(f, columns=cols, show="headings", height=12)
    widths = [90, 100, 90, 90, 80, 60, 50, 70, 70]
    for col, w in zip(cols, widths):
        tree.heading(col, text=col, anchor="center")
        tree.column(col, width=w, anchor="center")
    
    scroll = ttk.Scrollbar(f, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")
    tree.pack(fill="both", expand=True)
    
    def load_data(filt=""):
        tree.delete(*tree.get_children())
        for i, b in enumerate(bookings):
            if filt and filt.lower() not in str(b).lower(): continue
            for tkt in b.get('tickets', []):
                vals = (b.get('booking_id', ''), tkt.get('name', ''), get_station_name(tkt.get('from', '')),
                       get_station_name(tkt.get('to', '')), tkt.get('date', ''), tkt.get('dep', ''),
                       tkt.get('seat', ''), f"{tkt.get('price', 0):.0f}", t("status_confirmed"))
                tree.insert("", "end", values=vals, tags=("odd" if i % 2 == 0 else "even",))
        tree.tag_configure("odd", background="#f0f4f8")
        tree.tag_configure("even", background="white")
    
    load_data()
    
    def cancel_sel():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning(t("warning"), t("select_booking"))
            return
        bid = tree.item(sel[0])['values'][0]
        if messagebox.askyesno(t("confirm"), t("confirm_cancel", booking_id=bid)):
            db.cancel_booking(bid)
            messagebox.showinfo(t("success"), t("cancel_success"))
            win.destroy()
    
    bf = tk.Frame(win, bg="#f0f4f8")
    bf.pack(pady=8)
    tk.Button(bf, text=t("search"), command=lambda: load_data(se.get()), bg="#457b9d", fg="white", font=("Arial", 9, "bold"), padx=12, pady=4).pack(side="left", padx=4)
    tk.Button(bf, text=t("cancel_booking"), command=cancel_sel, bg="#e63946", fg="white", font=("Arial", 9, "bold"), padx=12, pady=4).pack(side="left", padx=4)
    tk.Button(bf, text=t("refresh"), command=lambda: load_data(), bg="#2a9d8f", fg="white", font=("Arial", 9, "bold"), padx=12, pady=4).pack(side="left", padx=4)

# ============ STATS ============
def show_statistics():
    bookings = db.load_bookings()
    win = tk.Toplevel(root)
    win.title(t("stats_title"))
    win.geometry("650x550")
    win.configure(bg="#f0f4f8")
    
    tk.Label(win, text=t("stats_title"), bg="#1d3557", fg="white", font=("Arial", 14, "bold"), pady=10).pack(fill="x")
    
    ta = scrolledtext.ScrolledText(win, width=70, height=25, font=("Courier", 9))
    ta.pack(padx=15, pady=15, fill="both", expand=True)
    
    tot_book = len(bookings)
    tot_rev = sum(t['price'] for b in bookings for t in b.get('tickets', []))
    tot_pass = sum(len(b.get('tickets', [])) for b in bookings)
    
    report = f"""{'='*55}
  {t("stats_title")}
{'='*55}

Date: {datetime.date.today().strftime('%d/%m/%Y')}

{'─'*55}
Total Bookings:    {tot_book:,}
Total Passengers:  {tot_pass:,}
Total Revenue:     {tot_rev:,.2f} THB
Avg per Booking:   {tot_rev/max(tot_book,1):,.2f} THB

{'─'*55}
{t('thank_you')}
{'='*55}
"""
    
    ta.insert('1.0', report)
    ta.config(state='disabled')
    
    def save_rep():
        fn = f"Report_{datetime.date.today().strftime('%Y%m%d')}.txt"
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(report)
        messagebox.showinfo(t("success"), t("report_saved", filename=fn))
    
    tk.Button(win, text=t("save_report"), command=save_rep, bg="#2a9d8f", fg="white", font=("Arial", 10, "bold"), padx=18, pady=6).pack(pady=8)

# ============ CONTACT ============
def show_contact_window():
    win = tk.Toplevel(root)
    win.title(t("contact_title"))
    win.geometry("550x500")
    win.configure(bg="#f0f4f8")
    win.transient(root)
    
    tk.Label(win, text=t("contact_title"), bg="#1d3557", fg="white", font=("Arial", 16, "bold"), pady=12).pack(fill="x")
    
    info = """
╔════════════════════════════════════════╗
║        Customer Service Center         ║
╚════════════════════════════════════════╝

📞 Call: 1690 (Free 24/7)
📧 Email: support@train.th
🌐 Web: www.train.th
📍 Address: Bangkok, Thailand

⏰ Hours: Mon-Fri 08:00-20:00
          Sat-Sun 09:00-18:00
          
════════════════════════════════════════
""" if current_language == "EN" else """
╔════════════════════════════════════════╗
║        ศูนย์บริการลูกค้า                ║
╚════════════════════════════════════════╝

📞 โทร: 1690 (ฟรี 24 ชม.)
📧 อีเมล: support@train.th
🌐 เว็บ: www.train.th
📍 ที่อยู่: กรุงเทพฯ ประเทศไทย

⏰ เวลา: จ-ศ 08:00-20:00 น.
         ส-อา 09:00-18:00 น.
         
════════════════════════════════════════
"""
    
    f = tk.Frame(win, bg="white", bd=2, relief="ridge")
    f.pack(fill="both", expand=True, padx=15, pady=15)
    
    tw = tk.Text(f, font=("Courier", 9), bg="white", wrap="word", height=18)
    tw.insert("1.0", info)
    tw.config(state="disabled")
    tw.pack(fill="both", expand=True, padx=10, pady=10)
    
    tk.Label(win, text=t("send_message"), bg="#f0f4f8", font=("Arial", 11, "bold")).pack(pady=(8, 4))
    tk.Entry(win, width=45, font=("Arial", 9)).pack(pady=4)
    tk.Button(win, text=t("send"), command=lambda: messagebox.showinfo(t("send"), t("message_sent")), bg="#2a9d8f", fg="white", font=("Arial", 10, "bold"), padx=20, pady=6).pack(pady=8)

# ============ UPDATE ============
def on_route_change(e=None):
    rd = combo_route.get()
    rk = get_route_key(rd)
    stations = routes[rk]
    sd = [get_station_name(s) for s in stations]
    combo_from['values'] = sd
    combo_to['values'] = sd
    combo_from.current(0)
    combo_to.current(1 if len(stations)>1 else 0)
    update_available_seats()

def update_sleeper_option(e=None):
    combo_upper_lower['values'] = [t("upper_lower")[k] for k in ["บน", "ล่าง"]]
    sc = combo_class.get()
    combo_upper_lower.config(state="readonly" if sc in [t("seat_classes")["นอน"], "นอน"] else "disabled")

def update_available_seats():
    rk = get_route_key(combo_route.get())
    fk = get_station_key(combo_from.get())
    tk = get_station_key(combo_to.get())
    sk = f"{rk}_{fk}_{tk}_{entry_date.get()}_{combo_round.get()}"
    
    # โหลดข้อมูลการจองจาก database และอัพเดท all_booked_seats
    bookings = db.load_bookings()
    booked_from_db = set()
    for booking in bookings:
        for ticket in booking.get('tickets', []):
            if (ticket.get('route') == rk and 
                ticket.get('from') == fk and 
                ticket.get('to') == tk and 
                ticket.get('date') == entry_date.get() and 
                ticket.get('dep') == combo_round.get() and
                ticket.get('seat')):
                booked_from_db.add(ticket['seat'])
    
    # รวมกับที่นั่งที่จองในเซสชั่นปัจจุบัน
    session_booked = set(all_booked_seats.get(sk, []))
    all_booked = booked_from_db.union(session_booked)
    all_booked_seats[sk] = list(all_booked)
    
    avail = 30 - len(all_booked)
    label_seats_available.config(text=t("seats_available", available=avail))
    label_seats_available.config(fg="red" if avail < 5 else "orange" if avail < 10 else "green")


    label_seats_available.config(fg="red" if avail < 5 else "orange" if avail < 10 else "green")

def show_calendar():
    cal_win = tk.Toplevel(root)
    cal_win.title("📅 " + t("travel_date"))
    cal_win.geometry("380x420")
    cal_win.configure(bg="#f0f4f8")
    cal_win.transient(root)
    cal_win.grab_set()
    
    try:
        curr_date = datetime.datetime.strptime(entry_date.get(), "%Y-%m-%d").date()
    except:
        curr_date = datetime.date.today()
    
    selected_date = [curr_date]
    
    tk.Label(cal_win, text="📅 " + t("travel_date"), bg="#1d3557", fg="white", 
             font=("Arial", 14, "bold"), pady=10).pack(fill="x")
    
    # Frame สำหรับเลือกเดือน/ปี
    nav_frame = tk.Frame(cal_win, bg="#f0f4f8")
    nav_frame.pack(pady=10)
    
    month_var = tk.IntVar(value=curr_date.month)
    year_var = tk.IntVar(value=curr_date.year)
    
    def update_calendar():
        for widget in cal_frame.winfo_children():
            widget.destroy()
        
        year = year_var.get()
        month = month_var.get()
        
        # หาวันแรกของเดือน
        first_day = datetime.date(year, month, 1)
        # หาว่าวันแรกเป็นวันอะไร (0=จันทร์, 6=อาทิตย์)
        start_weekday = first_day.weekday()
        # หาจำนวนวันในเดือน
        if month == 12:
            days_in_month = (datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)).day
        else:
            days_in_month = (datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)).day
        
        # แสดงหัววัน
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] if current_language == "EN" else ["จ", "อ", "พ", "พฤ", "ศ", "ส", "อา"]
        for i, day in enumerate(days):
            tk.Label(cal_frame, text=day, bg="#457b9d", fg="white", 
                    font=("Arial", 9, "bold"), width=5, height=1).grid(row=0, column=i, padx=1, pady=1)
        
        # แสดงวันที่
        row = 1
        col = start_weekday
        today = datetime.date.today()
        
        for day in range(1, days_in_month + 1):
            date_obj = datetime.date(year, month, day)
            
            def make_select(d=date_obj):
                def select():
                    if d >= today:
                        selected_date[0] = d
                        update_calendar()
                return select
            
            bg_color = "#2a9d8f" if date_obj == selected_date[0] else "#e0e0e0" if date_obj < today else "white"
            fg_color = "white" if date_obj == selected_date[0] else "#999" if date_obj < today else "black"
            state = "disabled" if date_obj < today else "normal"
            
            btn = tk.Button(cal_frame, text=str(day), bg=bg_color, fg=fg_color,
                          font=("Arial", 9, "bold" if date_obj == selected_date[0] else "normal"),
                          width=5, height=2, relief="flat", state=state,
                          command=make_select(date_obj))
            btn.grid(row=row, column=col, padx=1, pady=1)
            
            col += 1
            if col > 6:
                col = 0
                row += 1
    
    def prev_month():
        if month_var.get() == 1:
            month_var.set(12)
            year_var.set(year_var.get() - 1)
        else:
            month_var.set(month_var.get() - 1)
        update_calendar()
    
    def next_month():
        if month_var.get() == 12:
            month_var.set(1)
            year_var.set(year_var.get() + 1)
        else:
            month_var.set(month_var.get() + 1)
        update_calendar()
    
    tk.Button(nav_frame, text="◀", command=prev_month, bg="#457b9d", fg="white",
             font=("Arial", 11, "bold"), width=3, relief="flat").pack(side="left", padx=5)
    
    month_names = ["", "January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"] if current_language == "EN" else ["", "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]
    
    month_label = tk.Label(nav_frame, text="", bg="#f0f4f8", font=("Arial", 12, "bold"), width=20)
    month_label.pack(side="left", padx=10)
    
    def update_month_label():
        month_label.config(text=f"{month_names[month_var.get()]} {year_var.get()}")
    
    tk.Button(nav_frame, text="▶", command=next_month, bg="#457b9d", fg="white",
             font=("Arial", 11, "bold"), width=3, relief="flat").pack(side="left", padx=5)
    
    # Frame สำหรับปฏิทิน
    cal_frame = tk.Frame(cal_win, bg="white", bd=2, relief="ridge")
    cal_frame.pack(padx=20, pady=10)
    
    update_month_label()
    update_calendar()
    
    # ปุ่มยืนยัน
    def confirm_date():
        entry_date.delete(0, "end")
        entry_date.insert(0, selected_date[0].strftime("%Y-%m-%d"))
        update_available_seats()
        cal_win.destroy()
    
    btn_frame = tk.Frame(cal_win, bg="#f0f4f8")
    btn_frame.pack(pady=10)
    
    tk.Button(btn_frame, text=t("confirm"), command=confirm_date, bg="#2a9d8f", fg="white",
             font=("Arial", 11, "bold"), padx=25, pady=6).pack(side="left", padx=5)
    
    tk.Button(btn_frame, text=t("close"), command=cal_win.destroy, bg="#e63946", fg="white",
             font=("Arial", 11, "bold"), padx=25, pady=6).pack(side="left", padx=5)

# ============ BOOKING ============
def next_to_seat_selection():
    global tickets, food_orders
    tickets, food_orders = [], []
    
    name = entry_name.get().strip()
    if not name:
        messagebox.showwarning(t("error"), t("enter_name"))
        return
    
    try:
        ac = max(0, int(ticket_adult.get()))
        cc = max(0, int(ticket_child.get()))
        sc = max(0, int(ticket_senior.get()))
        tot = ac + cc + sc
        if tot < 1: raise ValueError
    except:
        messagebox.showwarning(t("error"), t("invalid_tickets"))
        return
    
    rd = combo_route.get()
    fd = combo_from.get()
    td = combo_to.get()
    cd = combo_class.get()
    
    rk = get_route_key(rd)
    fk = get_station_key(fd)
    tk_key = get_station_key(td)
    
    if cd == t("seat_classes")["ชั้น 2"]: seat_c = "ชั้น 2"
    elif cd == t("seat_classes")["ชั้น 1"]: seat_c = "ชั้น 1"
    elif cd == t("seat_classes")["นอน"]: seat_c = "นอน"
    else: seat_c = cd
    
    sd = combo_upper_lower.get()
    if sd == t("upper_lower")["บน"]: sub_t = "บน"
    elif sd == t("upper_lower")["ล่าง"]: sub_t = "ล่าง"
    else: sub_t = sd if sd else None
    
    route_list = routes[rk]
    date_str = entry_date.get()
    train_r = combo_round.get()
    
    if fk == tk_key:
        messagebox.showwarning(t("error"), t("same_station"))
        return
    
    try:
        td_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        if td_obj < datetime.date.today(): raise ValueError
    except:
        messagebox.showwarning(t("error"), t("invalid_date"))
        return
    
    seat_key = f"{rk}_{fk}_{tk_key}_{date_str}_{train_r}"
    
    # โหลดข้อมูลที่นั่งที่จองแล้วจาก database
    bookings = db.load_bookings()
    booked_from_db = set()
    for booking in bookings:
        for ticket in booking.get('tickets', []):
            if (ticket.get('route') == rk and 
                ticket.get('from') == fk and 
                ticket.get('to') == tk_key and 
                ticket.get('date') == date_str and 
                ticket.get('dep') == train_r and
                ticket.get('seat')):
                booked_from_db.add(ticket['seat'])
    
    # รวมกับที่นั่งที่จองในเซสชั่นปัจจุบัน
    session_booked = set(all_booked_seats.get(seat_key, []))
    all_booked = booked_from_db.union(session_booked)
    booked = len(all_booked)
    
    if booked + tot > 30:
        messagebox.showerror(t("error"), t("seats_full", available=30-booked))
        return
    
    dist = estimate_distance(fk, tk_key, route_list)
    dh, dm = map(int, train_r.split(":"))
    dt = datetime.datetime(2025, 1, 1, dh, dm)
    th, tm = divmod(dist, 80)
    tm = int(tm/80*60)
    arr = dt + datetime.timedelta(hours=th, minutes=tm)
    
    for pt, cnt in zip(["ผู้ใหญ่","เด็ก","ผู้สูงอายุ"], [ac, cc, sc]):
        for _ in range(cnt):
            tickets.append({
                "name": name, "type": pt, "class": seat_c, "sub_type": sub_t if sub_t else "-",
                "price": dist*1.5*class_multiplier(seat_c, sub_t)*passenger_discount(pt),
                "from": fk, "to": tk_key, "date": date_str, "dep": train_r,
                "arr": arr.strftime("%H:%M"), "seat": None, "route": rk
            })
    
    if messagebox.askyesno(t("food_order_title"), t("order_food_question")):
        show_food_order_window(seat_window)
    else:
        food_orders = []
        seat_window()

# ============ FOOD ============
def show_food_order_window(callback):
    global food_orders
    food_orders = []
    
    win = tk.Toplevel(root)
    win.title(t("food_order_title"))
    win.geometry("700x550")
    win.configure(bg="#f0f4f8")
    win.transient(root)
    win.grab_set()
    
    tk.Label(win, text=t("food_order_title"), bg="#1d3557", fg="white", font=("Arial", 14, "bold"), pady=10).pack(fill="x")
    tk.Label(win, text=t("food_subtitle"), bg="#fff3cd", fg="#856404", font=("Arial", 9), pady=6).pack(fill="x")
    
    mf = tk.Frame(win, bg="white", bd=2, relief="ridge")
    mf.pack(fill="both", expand=True, padx=15, pady=8)
    
    canvas = tk.Canvas(mf, bg="white")
    scroll = ttk.Scrollbar(mf, orient="vertical", command=canvas.yview)
    sf = tk.Frame(canvas, bg="white")
    
    sf.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=sf, anchor="nw")
    canvas.configure(yscrollcommand=scroll.set)
    
    menu = db.load_food_menu()
    qty_vars = {}
    
    for item in menu:
        itemf = tk.Frame(sf, bg="white")
        itemf.pack(fill="x", padx=15, pady=4)
        
        iname = item['name'] if current_language == "TH" else item.get('name_en', item['name'])
        tk.Label(itemf, text=iname, bg="white", font=("Arial", 10), width=20, anchor="w").pack(side="left")
        tk.Label(itemf, text=f"{item['price']} ฿", bg="white", font=("Arial", 10, "bold"), fg="#e63946", width=6).pack(side="left")
        
        qv = tk.IntVar(value=0)
        qty_vars[item['id']] = (qv, item)
        
        tk.Button(itemf, text="-", command=lambda v=qv: v.set(max(0, v.get()-1)), bg="#e63946", fg="white", font=("Arial", 9, "bold"), width=2).pack(side="left", padx=3)
        tk.Label(itemf, textvariable=qv, bg="white", font=("Arial", 10, "bold"), width=3).pack(side="left")
        tk.Button(itemf, text="+", command=lambda v=qv: v.set(v.get()+1), bg="#2a9d8f", fg="white", font=("Arial", 9, "bold"), width=2).pack(side="left", padx=3)
    
    canvas.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")
    
    tot_lbl = tk.Label(win, text=t("food_total", total=0), bg="#f0f4f8", font=("Arial", 12, "bold"), fg="#1d3557")
    tot_lbl.pack(pady=8)
    
    def upd_tot():
        tot = sum(v.get() * item['price'] for v, item in qty_vars.values())
        tot_lbl.config(text=t("food_total", total=tot))
        win.after(100, upd_tot)
    upd_tot()
    
    def conf():
        global food_orders
        food_orders = []
        tot = 0
        for iid, (qv, item) in qty_vars.items():
            q = qv.get()
            if q > 0:
                iname = item['name'] if current_language == "TH" else item.get('name_en', item['name'])
                food_orders.append({'name': iname, 'quantity': q, 'price': item['price'], 'total': q * item['price']})
                tot += q * item['price']
        if food_orders:
            messagebox.showinfo(t("success"), t("food_success", total=tot))
        win.destroy()
        callback()
    
    bf = tk.Frame(win, bg="#f0f4f8")
    bf.pack(pady=8)
    tk.Button(bf, text=t("confirm_food"), command=conf, bg="#2a9d8f", fg="white", font=("Arial", 11, "bold"), padx=20, pady=6).pack(side="left", padx=4)
    tk.Button(bf, text=t("skip_food"), command=lambda: [win.destroy(), callback()], bg="#457b9d", fg="white", font=("Arial", 11, "bold"), padx=20, pady=6).pack(side="left", padx=4)

# ============ SEATS ============
def seat_window():
    win = tk.Toplevel(root)
    win.title(t("seat_selection_title"))
    win.geometry("850x600")
    win.configure(bg="#f8fafc")
    win.transient(root)
    win.grab_set()
    
    tk.Label(win, text=t("select_seats_for", count=len(tickets)), bg="#1d3557", fg="white", font=("Arial", 14, "bold"), pady=10).pack(fill="x")
    
    inf = tk.Frame(win, bg="#f8fafc")
    inf.pack(pady=8)
    
    rn = get_route_name(tickets[0]['route'])
    fn = get_station_name(tickets[0]['from'])
    tn = get_station_name(tickets[0]['to'])
    tk.Label(inf, text=f"🚆 {rn} | {fn} → {tn} | 📅 {tickets[0]['date']} | ⏰ {tickets[0]['dep']}", bg="#f8fafc", font=("Arial", 10)).pack()
    
    f = tk.Frame(win, bg="#f8fafc", padx=15, pady=8)
    f.pack(fill="both", expand=True)
    
    sk = f"{tickets[0]['route']}_{tickets[0]['from']}_{tickets[0]['to']}_{tickets[0]['date']}_{tickets[0]['dep']}"
    
    # โหลดข้อมูลที่นั่งที่จองแล้วจาก database
    bookings = db.load_bookings()
    booked_from_db = set()
    for booking in bookings:
        for ticket in booking.get('tickets', []):
            if (ticket.get('route') == tickets[0]['route'] and 
                ticket.get('from') == tickets[0]['from'] and 
                ticket.get('to') == tickets[0]['to'] and 
                ticket.get('date') == tickets[0]['date'] and 
                ticket.get('dep') == tickets[0]['dep'] and
                ticket.get('seat')):
                booked_from_db.add(ticket['seat'])
    
    if sk not in all_booked_seats:
        all_booked_seats[sk] = list(booked_from_db)
    else:
        # รวมกับที่นั่งที่จองในเซสชั่นปัจจุบัน
        all_booked_seats[sk] = list(set(all_booked_seats[sk]).union(booked_from_db))
    
    sel_btns = {}
    temp_sel = set()
    
    lf = tk.Frame(win, bg="#f8fafc")
    lf.pack(pady=4)
    for txt, col in [(t("seat_available"), "#bde0fe"), (t("seat_selected"), "yellow"), (t("seat_booked"), "#adb5bd"), (t("seat_confirmed"), "#2a9d8f")]:
        tk.Label(lf, text="  ", bg=col, width=3, relief="solid", borderwidth=1).pack(side="left", padx=4)
        tk.Label(lf, text=txt, bg="#f8fafc", font=("Arial", 8)).pack(side="left", padx=(0, 12))
    
    for r in range(5):
        for c in range(6):
            seat = f"{chr(65+r)}{c+1}"
            if c == 3:
                tk.Label(f, text=t("aisle"), bg="#f8fafc", font=("Arial", 8)).grid(row=r, column=c)
                continue
            col = "#bde0fe" if seat not in all_booked_seats[sk] else "#adb5bd"
            btn = tk.Button(f, text=seat, width=5, height=2, bg=col, font=("Arial", 9, "bold"))
            btn.grid(row=r, column=c, padx=2, pady=2)
            sel_btns[seat] = btn
    
    def toggle(seat):
        if seat in all_booked_seats[sk]:
            messagebox.showinfo(t("seat_booked"), t("seat_taken", seat=seat))
            return
        if seat in temp_sel:
            temp_sel.remove(seat)
            sel_btns[seat].config(bg="#bde0fe")
        else:
            if len(temp_sel) >= len(tickets):
                messagebox.showwarning(t("warning"), t("max_seats", max=len(tickets)))
                return
            temp_sel.add(seat)
            sel_btns[seat].config(bg="yellow")
        conf_btn.config(text=t("confirm_seats", selected=len(temp_sel), total=len(tickets)))
    
    for seat, btn in sel_btns.items():
        if seat not in all_booked_seats[sk]:
            btn.config(command=lambda s=seat: toggle(s))
    
    def conf():
        if len(temp_sel) != len(tickets):
            messagebox.showwarning(t("confirm"), t("select_all_seats", total=len(tickets), selected=len(temp_sel)))
            return
        for tkt, seat in zip(tickets, sorted(temp_sel)):
            tkt["seat"] = seat
            all_booked_seats[sk].append(seat)
            sel_btns[seat].config(bg="#2a9d8f", fg="white", state="disabled")
        messagebox.showinfo(t("success"), t("seats_confirmed"))
        win.destroy()
        show_payment_window()
    
    conf_btn = tk.Button(win, text=t("confirm_seats", selected=0, total=len(tickets)), command=conf, bg="#2a9d8f", fg="white", font=("Arial", 11, "bold"), padx=25, pady=8)
    conf_btn.pack(pady=12)

# ============ PAYMENT ============
def show_payment_window():
    win = tk.Toplevel(root)
    win.title(t("payment_title"))
    win.geometry("600x650")
    win.configure(bg="#f0f4f8")
    win.transient(root)
    win.grab_set()
    
    tk.Label(win, text=t("payment_title"), bg="#1d3557", fg="white", font=("Arial", 14, "bold"), pady=10).pack(fill="x")
    
    f = tk.Frame(win, bg="white", bd=2, relief="ridge", padx=18, pady=18)
    f.pack(fill="both", expand=True, padx=18, pady=10)
    
    tp = sum(t['price'] for t in tickets)
    ft = sum(item['total'] for item in food_orders)
    gt = tp + ft
    
    tk.Label(f, text=t("payment_summary"), font=("Arial", 13, "bold"), bg="white").pack(pady=8)
    tk.Label(f, text=t("ticket_price", price=tp), font=("Arial", 10), bg="white").pack(pady=2)
    if food_orders:
        tk.Label(f, text=t("food_price", price=ft), font=("Arial", 10), bg="white").pack(pady=2)
        tk.Label(f, text=t("total", total=gt), font=("Arial", 11, "bold"), bg="white").pack(pady=4)
    
    nt = len(tickets)
    auto_p = None
    if nt >= 5:
        auto_p = "GROUP20"
        tk.Label(f, text=t("group_discount", count=nt), font=("Arial", 10), fg="#2a9d8f", bg="white").pack(pady=4)
    elif nt >= 3:
        auto_p = "FAMILY15"
        tk.Label(f, text=t("family_discount", count=nt), font=("Arial", 10), fg="#2a9d8f", bg="white").pack(pady=4)
    
    pf = tk.Frame(f, bg="white")
    pf.pack(pady=12)
    tk.Label(pf, text=t("promo_code"), bg="white", font=("Arial", 10)).grid(row=0, column=0, padx=4)
    pe = tk.Entry(pf, width=18, font=("Arial", 10))
    pe.grid(row=0, column=1, padx=4)
    if auto_p: pe.insert(0, auto_p)
    
    disc = [0]
    fp = [gt]
    
    lbl_disc = tk.Label(f, text="", font=("Arial", 10), fg="green", bg="white")
    lbl_disc.pack()
    lbl_final = tk.Label(f, text=t("net_total", total=fp[0]), font=("Arial", 13, "bold"), fg="#e63946", bg="white")
    lbl_final.pack(pady=8)
    lbl_vat = tk.Label(f, text="", font=("Arial", 9), fg="gray", bg="white")
    
    def apply_p():
        code = pe.get().strip().upper()
        if not code:
            messagebox.showwarning(t("warning"), t("enter_promo"))
            return
        promos = db.load_promotions()
        promo = next((p for p in promos if p['code'] == code), None)
        if not promo:
            messagebox.showerror(t("error"), t("invalid_promo", code=code))
            return
        if 'min_tickets' in promo and nt < promo['min_tickets']:
            messagebox.showerror(t("error"), f"Need {promo['min_tickets']}+ tickets")
            return
        if 'max_tickets' in promo and nt > promo['max_tickets']:
            messagebox.showerror(t("error"), f"Max {promo['max_tickets']} tickets")
            return
        if promo['type'] == 'percent':
            disc[0] = gt * promo['discount'] / 100
            lbl_disc.config(text=f"✅ {t('discount')} {promo['discount']}% (-{disc[0]:.2f})")
        else:
            disc[0] = min(promo['discount'], gt)
            lbl_disc.config(text=f"✅ {t('discount')} -{disc[0]:.2f}")
        fp[0] = max(0, gt - disc[0])
        vat = fp[0] * 0.07
        lbl_vat.config(text=t("vat", vat=vat))
        lbl_final.config(text=t("net_total", total=fp[0]))
        messagebox.showinfo(t("success"), t("promo_applied", code=code, discount=disc[0]))
    
    tk.Button(pf, text=t("use_code"), command=apply_p, bg="#2a9d8f", fg="white", font=("Arial", 9, "bold"), padx=8).grid(row=0, column=2, padx=4)
    if auto_p: apply_p()
    
    tk.Label(f, text=t("payment_method"), font=("Arial", 11, "bold"), bg="white").pack(pady=8)
    pms = [t("credit_card"), t("bank_transfer"), t("qr_payment"), t("cash")]
    pv = tk.StringVar(value=pms[0])
    for pm in pms:
        tk.Radiobutton(f, text=pm, variable=pv, value=pm, bg="white", font=("Arial", 9)).pack(anchor="w", padx=15)
    
    vat = fp[0] * 0.07
    lbl_vat.config(text=t("vat", vat=vat))
    lbl_vat.pack(pady=4)
    
    def conf_pay():
        bid = generate_booking_id()
        bd = {
            'booking_id': bid, 'username': current_user['username'], 'tickets': tickets,
            'food_orders': food_orders, 'ticket_price': tp, 'food_price': ft,
            'total_price': gt, 'discount': disc[0], 'final_price': fp[0], 'vat': vat,
            'payment_method': pv.get(), 'booking_date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'status': t("status_confirmed"), 'promo_code': pe.get().strip().upper() if disc[0] > 0 else None
        }
        db.save_booking(bd)
        if current_user['username']:
            pts = calculate_points(fp[0])
            current_user['points'] += pts
            users = db.load_users()
            users[current_user['username']]['points'] = current_user['points']
            db.save_user(current_user['username'], users[current_user['username']])
            update_user_label()
        win.destroy()
        show_summary(bid, bd)
    
    tk.Button(f, text=t("confirm_payment"), command=conf_pay, bg="#e63946", fg="white", font=("Arial", 11, "bold"), padx=25, pady=8).pack(pady=15)

# ============ SUMMARY ============
def show_summary(bid, bd):
    win = tk.Toplevel(root)
    win.title(t("ticket_title"))
    win.geometry("900x650")
    win.configure(bg="#f1faee")
    win.transient(root)
    
    tk.Label(win, text=t("ticket_title"), bg="#1d3557", fg="white", font=("Arial", 16, "bold"), pady=12).pack(fill="x")
    tk.Label(win, text=t("booking_id", id=bid), font=("Arial", 13, "bold"), fg="#e63946", bg="#f1faee").pack(pady=8)
    
    f = tk.Frame(win, bg="white", bd=2, relief="ridge", padx=8, pady=8)
    f.pack(fill="both", expand=True, padx=20, pady=8)
    
    cols = ("Name", "Type", "From", "To", "Seat", "Date", "Dep", "Arr", "Price") if current_language == "EN" else ("ชื่อ","ประเภท","จาก","ไป","ที่นั่ง","วันที่","ออก","ถึง","ราคา")
    tree = ttk.Treeview(f, columns=cols, show="headings", height=6)
    tree.pack(fill="both", expand=True)
    
    ws = [110, 75, 90, 90, 60, 80, 60, 60, 80]
    for col, w in zip(cols, ws):
        tree.heading(col, text=col, anchor="center")
        tree.column(col, width=w, anchor="center")
    
    scroll = ttk.Scrollbar(f, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")
    
    for i, tkt in enumerate(tickets):
        tag = "odd" if i%2==0 else "even"
        pt = t("passenger_types").get(tkt["type"], tkt["type"])
        fn = get_station_name(tkt["from"])
        tn = get_station_name(tkt["to"])
        tree.insert("", "end", values=(tkt["name"], pt, fn, tn, tkt["seat"], tkt["date"], tkt["dep"], tkt["arr"], f"{tkt['price']:.0f} ฿"), tags=(tag,))
    tree.tag_configure("odd", background="#f0f4f8")
    tree.tag_configure("even", background="white")
    
    sf = tk.LabelFrame(win, text=t("expense_summary"), bg="white", font=("Arial", 11, "bold"), fg="#1d3557", padx=15, pady=12)
    sf.pack(pady=8, padx=20, fill="x")
    
    r = 0
    tk.Label(sf, text=t("ticket_fee", count=len(tickets)), font=("Arial", 10), bg="white", anchor="w", width=22).grid(row=r, column=0, sticky="w", pady=2)
    tk.Label(sf, text=f"{bd['ticket_price']:.2f} THB", font=("Arial", 10), bg="white", anchor="e").grid(row=r, column=1, sticky="e", pady=2)
    r += 1
    
    if bd['food_orders']:
        for item in bd['food_orders']:
            tk.Label(sf, text=f"  • {item['name']} x{item['quantity']}", font=("Arial", 9), bg="white", fg="#666", anchor="w", width=22).grid(row=r, column=0, sticky="w", pady=1)
            tk.Label(sf, text=f"{item['total']:.2f} THB", font=("Arial", 9), bg="white", fg="#666", anchor="e").grid(row=r, column=1, sticky="e", pady=1)
            r += 1
        tk.Label(sf, text=t("food_fee"), font=("Arial", 10), bg="white", anchor="w", width=22).grid(row=r, column=0, sticky="w", pady=2)
        tk.Label(sf, text=f"{bd['food_price']:.2f} THB", font=("Arial", 10), bg="white", anchor="e").grid(row=r, column=1, sticky="e", pady=2)
        r += 1
    
    ttk.Separator(sf, orient="horizontal").grid(row=r, column=0, columnspan=2, sticky="ew", pady=6)
    r += 1
    tk.Label(sf, text=t("subtotal"), font=("Arial", 10, "bold"), bg="white", anchor="w", width=22).grid(row=r, column=0, sticky="w", pady=2)
    tk.Label(sf, text=f"{bd['total_price']:.2f} THB", font=("Arial", 10, "bold"), bg="white", anchor="e").grid(row=r, column=1, sticky="e", pady=2)
    r += 1
    
    if bd['discount'] > 0:
        pt = t("discount")
        if bd.get('promo_code'): pt += f" ({bd['promo_code']})"
        tk.Label(sf, text=pt, font=("Arial", 10), bg="white", fg="green", anchor="w", width=22).grid(row=r, column=0, sticky="w", pady=2)
        tk.Label(sf, text=f"-{bd['discount']:.2f} THB", font=("Arial", 10), bg="white", fg="green", anchor="e").grid(row=r, column=1, sticky="e", pady=2)
        r += 1
    
    vl = "VAT (7%)" if current_language == "EN" else "VAT 7%"
    tk.Label(sf, text=vl, font=("Arial", 9), bg="white", fg="gray", anchor="w", width=22).grid(row=r, column=0, sticky="w", pady=2)
    tk.Label(sf, text=f"{bd['vat']:.2f} THB", font=("Arial", 9), bg="white", fg="gray", anchor="e").grid(row=r, column=1, sticky="e", pady=2)
    r += 1
    
    ttk.Separator(sf, orient="horizontal").grid(row=r, column=0, columnspan=2, sticky="ew", pady=6)
    r += 1
    nl = "💰 Net Total" if current_language == "EN" else "💰 ยอดสุทธิ"
    tk.Label(sf, text=nl, font=("Arial", 13, "bold"), bg="white", fg="#e63946", anchor="w", width=22).grid(row=r, column=0, sticky="w", pady=4)
    tk.Label(sf, text=f"{bd['final_price']:.2f} THB", font=("Arial", 13, "bold"), bg="white", fg="#e63946", anchor="e").grid(row=r, column=1, sticky="e", pady=4)
    
    if current_user['username']:
        pts = calculate_points(bd['final_price'])
        pf = tk.Frame(win, bg="#fff3cd", bd=2, relief="solid")
        pf.pack(pady=8, padx=20, fill="x")
        tk.Label(pf, text=t("points_earned", points=pts), font=("Arial", 11, "bold"), fg="#e63946", bg="#fff3cd", pady=6).pack()
    
    def save_tkt():
        fn = f"Ticket_{bid}.txt"
        with open(fn, "w", encoding="utf-8") as file:
            file.write("="*65 + "\n")
            file.write("🚆  Train Ticket System 2025\n")
            file.write("="*65 + "\n\n")
            file.write(f"📋 Booking ID: {bid}\n")
            file.write(f"📅 Date: {bd['booking_date']}\n")
            file.write(f"💳 Payment: {bd['payment_method']}\n")
            file.write(f"✅ Status: {bd['status']}\n\n")
            file.write("="*65 + "\n\n")
            for i, tkt in enumerate(tickets, 1):
                file.write(f"🎟️  Ticket {i}\n")
                file.write("─"*65 + "\n")
                file.write(f"Name: {tkt['name']}\n")
                file.write(f"Type: {t('passenger_types').get(tkt['type'], tkt['type'])}\n")
                file.write(f"Route: {get_route_name(tkt['route'])}\n")
                file.write(f"From: {get_station_name(tkt['from'])} → To: {get_station_name(tkt['to'])}\n")
                file.write(f"Date: {tkt['date']} | Dep: {tkt['dep']} → Arr: {tkt['arr']}\n")
                file.write(f"Seat: {tkt['seat']} | Class: {tkt['class']} ({tkt['sub_type']})\n")
                file.write(f"Price: {tkt['price']:.2f} THB\n\n")
                qr = create_simple_qr(f"TRAIN|{bid}|{tkt['name']}|{tkt['seat']}", 6)
                file.write("QR:\n" + qr + "\n\n")
            file.write("="*65 + "\n")
            file.write(f"Total: {bd['final_price']:.2f} THB\n")
            file.write("="*65 + "\n")
            file.write(f"{t('thank_you')}\n")
        messagebox.showinfo(t("success"), t("ticket_saved", filename=fn))
    
    def show_qr():
        qw = tk.Toplevel(win)
        qw.title("🎫 QR Code")
        qw.geometry("450x500")
        qw.configure(bg="white")
        tk.Label(qw, text="🎫 QR Code", bg="#1d3557", fg="white", font=("Arial", 13, "bold"), pady=8).pack(fill="x")
        tk.Label(qw, text=f"ID: {bid}", font=("Arial", 11, "bold"), bg="white").pack(pady=8)
        qf = tk.Frame(qw, bg="white")
        qf.pack(pady=15, expand=True)
        for i, tkt in enumerate(tickets, 1):
            tf = tk.LabelFrame(qf, text=f"Ticket {i} - {tkt['name']} ({tkt['seat']})", bg="white", font=("Arial", 9, "bold"), padx=8, pady=8)
            tf.pack(pady=8, fill="x")
            qr = create_simple_qr(f"TRAIN|{bid}|{tkt['name']}|{tkt['seat']}", 8)
            tk.Label(tf, text=qr, font=("Courier", 5), bg="white", justify="left").pack()
        tk.Button(qw, text=t("close"), command=qw.destroy, bg="#e63946", fg="white", font=("Arial", 10, "bold"), padx=18, pady=6).pack(pady=15)
    
    bf = tk.Frame(win, bg="#f1faee")
    bf.pack(pady=12)
    tk.Button(bf, text=t("save_ticket"), command=save_tkt, bg="#2a9d8f", fg="white", font=("Arial", 10, "bold"), padx=15, pady=6).grid(row=0, column=0, padx=4)
    tk.Button(bf, text=t("show_qr"), command=show_qr, bg="#457b9d", fg="white", font=("Arial", 10, "bold"), padx=15, pady=6).grid(row=0, column=1, padx=4)
    tk.Button(bf, text=t("manage_booking"), command=lambda: [win.destroy(), show_bookings_window()], bg="#f4a261", fg="white", font=("Arial", 10, "bold"), padx=15, pady=6).grid(row=0, column=2, padx=4)
    tk.Button(bf, text=t("close"), command=win.destroy, bg="#e63946", fg="white", font=("Arial", 10, "bold"), padx=15, pady=6).grid(row=0, column=3, padx=4)

# ============ UI ============
apply_theme()

hf = tk.Frame(root, height=85, bg="#1d3557")
hf.pack(fill="x")
hf.pack_propagate(False)

header_label = tk.Label(hf, text=t("app_title"), font=("Arial", 24, "bold"), fg="white", bg="#1d3557")
header_label.pack(pady=8)

mf = tk.Frame(hf, bg="#1d3557")
mf.pack()

menu_button_login = tk.Button(mf, text=t("login"), command=show_login_window, bg="#457b9d", fg="white", font=("Arial", 8, "bold"), padx=8, pady=4, relief="flat")
menu_button_login.pack(side="left", padx=2)

menu_button_bookings = tk.Button(mf, text=t("manage_bookings"), command=show_bookings_window, bg="#457b9d", fg="white", font=("Arial", 8, "bold"), padx=8, pady=4, relief="flat")
menu_button_bookings.pack(side="left", padx=2)

menu_button_stats = tk.Button(mf, text=t("statistics"), command=show_statistics, bg="#457b9d", fg="white", font=("Arial", 8, "bold"), padx=8, pady=4, relief="flat")
menu_button_stats.pack(side="left", padx=2)

menu_button_contact = tk.Button(mf, text=t("contact"), command=show_contact_window, bg="#457b9d", fg="white", font=("Arial", 8, "bold"), padx=8, pady=4, relief="flat")
menu_button_contact.pack(side="left", padx=2)

menu_button_dark = tk.Button(mf, text=t("dark_mode"), command=toggle_dark_mode, bg="#457b9d", fg="white", font=("Arial", 8, "bold"), padx=8, pady=4, relief="flat")
menu_button_dark.pack(side="left", padx=2)

menu_button_lang = tk.Button(mf, text="🌐 TH/EN", command=change_language, bg="#f4a261", fg="white", font=("Arial", 8, "bold"), padx=8, pady=4, relief="flat")
menu_button_lang.pack(side="left", padx=2)

menu_button_logout = tk.Button(mf, text=t("logout"), command=logout, bg="#457b9d", fg="white", font=("Arial", 8, "bold"), padx=8, pady=4, relief="flat")
menu_button_logout.pack(side="left", padx=2)

user_label = tk.Label(root, text=t("not_logged_in"), bg="#f0f4f8", font=("Arial", 10, "bold"), fg="#1d3557")
user_label.pack(pady=4)

main_frame = tk.LabelFrame(root, text=t("travel_info"), bg="white", font=("Arial", 12, "bold"), fg="#1d3557", padx=20, pady=15)
main_frame.pack(fill="both", expand=True, padx=20, pady=8)

ls = {"background": "white", "font": ("Arial", 10)}

label_name = tk.Label(main_frame, text=t("passenger_name"), **ls)
label_name.grid(row=0, column=0, sticky="w", pady=6)
entry_name = tk.Entry(main_frame, width=28, font=("Arial", 10))
entry_name.grid(row=0, column=1, pady=6, sticky="w")

label_adult = tk.Label(main_frame, text=t("num_adults"), **ls)
label_adult.grid(row=1, column=0, sticky="w", pady=6)
ticket_adult = tk.Spinbox(main_frame, from_=0, to=10, width=9, font=("Arial", 10))
ticket_adult.grid(row=1, column=1, pady=6, sticky="w")
ticket_adult.delete(0, "end")
ticket_adult.insert(0, "1")

label_child = tk.Label(main_frame, text=t("num_children"), **ls)
label_child.grid(row=2, column=0, sticky="w", pady=6)
ticket_child = tk.Spinbox(main_frame, from_=0, to=10, width=9, font=("Arial", 10))
ticket_child.grid(row=2, column=1, pady=6, sticky="w")

label_senior = tk.Label(main_frame, text=t("num_seniors"), **ls)
label_senior.grid(row=3, column=0, sticky="w", pady=6)
ticket_senior = tk.Spinbox(main_frame, from_=0, to=10, width=9, font=("Arial", 10))
ticket_senior.grid(row=3, column=1, pady=6, sticky="w")

label_route = tk.Label(main_frame, text=t("route"), **ls)
label_route.grid(row=4, column=0, sticky="w", pady=6)
rk = list(routes.keys())
rd = [get_route_name(r) for r in rk]
combo_route = ttk.Combobox(main_frame, values=rd, state="readonly", font=("Arial", 10), width=26)
combo_route.current(0)
combo_route.grid(row=4, column=1, pady=6, sticky="w")
combo_route.bind("<<ComboboxSelected>>", on_route_change)

label_from = tk.Label(main_frame, text=t("from_station"), **ls)
label_from.grid(row=5, column=0, sticky="w", pady=6)
ist = [get_station_name(s) for s in routes["สายเหนือ"]]
combo_from = ttk.Combobox(main_frame, values=ist, state="readonly", font=("Arial", 10), width=26)
combo_from.current(0)
combo_from.grid(row=5, column=1, pady=6, sticky="w")
combo_from.bind("<<ComboboxSelected>>", lambda e: update_available_seats())

label_to = tk.Label(main_frame, text=t("to_station"), **ls)
label_to.grid(row=6, column=0, sticky="w", pady=6)
combo_to = ttk.Combobox(main_frame, values=ist, state="readonly", font=("Arial", 10), width=26)
combo_to.current(1)
combo_to.grid(row=6, column=1, pady=6, sticky="w")
combo_to.bind("<<ComboboxSelected>>", lambda e: update_available_seats())

label_date = tk.Label(main_frame, text=t("travel_date"), **ls)
label_date.grid(row=7, column=0, sticky="w", pady=6)
df = tk.Frame(main_frame, bg="white")
df.grid(row=7, column=1, pady=6, sticky="w")
entry_date = tk.Entry(df, font=("Arial", 10), width=20)
entry_date.insert(0, datetime.date.today().strftime("%Y-%m-%d"))
entry_date.pack(side="left")
entry_date.bind("<KeyRelease>", lambda e: update_available_seats())


# แก้บรรทัดนี้ เพิ่ม command=show_calendar
tk.Button(df, text="📅", bg="#457b9d", fg="white", font=("Arial", 9, "bold"), padx=6, pady=1, command=show_calendar).pack(side="left", padx=4)

label_round = tk.Label(main_frame, text=t("train_round"), **ls)
label_round.grid(row=8, column=0, sticky="w", pady=6)
combo_round = ttk.Combobox(main_frame, values=train_rounds, state="readonly", font=("Arial", 10), width=26)
combo_round.current(0)
combo_round.grid(row=8, column=1, pady=6, sticky="w")
combo_round.bind("<<ComboboxSelected>>", lambda e: update_available_seats())

label_class = tk.Label(main_frame, text=t("seat_class"), **ls)
label_class.grid(row=9, column=0, sticky="w", pady=6)
scd = [t("seat_classes")[k] for k in ["ชั้น 2", "ชั้น 1", "นอน"]]
combo_class = ttk.Combobox(main_frame, values=scd, state="readonly", font=("Arial", 10), width=26)
combo_class.current(0)
combo_class.grid(row=9, column=1, pady=6, sticky="w")
combo_class.bind("<<ComboboxSelected>>", update_sleeper_option)

label_upper_lower = tk.Label(main_frame, text=t("sleeper_position"), **ls)
label_upper_lower.grid(row=10, column=0, sticky="w", pady=6)
sld = [t("upper_lower")[k] for k in ["บน", "ล่าง"]]
combo_upper_lower = ttk.Combobox(main_frame, values=sld, state="disabled", font=("Arial", 10), width=26)
combo_upper_lower.grid(row=10, column=1, pady=6, sticky="w")

label_seats_available = tk.Label(main_frame, text=t("seats_available", available=30), bg="white", font=("Arial", 10, "bold"), fg="green")
label_seats_available.grid(row=11, column=0, columnspan=2, pady=8)

btn_book = tk.Button(main_frame, text=t("next_seat_selection"), command=next_to_seat_selection, bg="#e63946", fg="white", font=("Arial", 12, "bold"), padx=35, pady=10)
btn_book.grid(row=12, column=0, columnspan=2, pady=15)

info_frame = tk.LabelFrame(root, text=t("promotions_title"), bg="#fff3cd", font=("Arial", 10, "bold"), fg="#856404", padx=12, pady=8)
info_frame.pack(fill="x", padx=20, pady=(0, 8))

promo_label = tk.Label(info_frame, text="", bg="#fff3cd", fg="#856404", font=("Arial", 8))
promo_label.pack()

promo_info_label = tk.Label(info_frame, text=t("promo_info"), bg="#fff3cd", fg="#856404", font=("Arial", 8))
promo_info_label.pack()

update_promo_text()

footer = tk.Label(root, text=t("footer"), bg="#1d3557", fg="white", font=("Arial", 9), pady=10)
footer.pack(fill="x", side="bottom")

update_available_seats()

root.mainloop()