import tkinter as tk
from PIL import Image, ImageTk
from classes import *

# ===== DATA =====
bag_data = [
    ("School Bag", "images/Bags/School Bag.jpg"),
    ("Swim Bag", "images/Bags/swim bag.jpg"),
    ("Duffel Bag", "images/Bags/duffel bag.jpg"),
    ("Suitcase", "images/Bags/suitcase.jpg"),
    ("Laptop Bag", "images/Bags/Laptop bag.jpg"),
]

org_data = [
    ("Pencil Case", "images/Orginizers/pencil case.jpg"),
    ("Toiletries Bag", "images/Orginizers/toiletries bag.jpg"),
    ("Snack Box", "images/Orginizers/Snack box.jpg"),
    ("Lunch Bag", "images/Orginizers/lunch bag.jpg"),
    ("Packing Cube", "images/Orginizers/Packing cube.jpg"),
    ("Leather Pouch", "images/Orginizers/Leather pouch.jpg"),
    ("Bathroom Pouch", "images/Orginizers/bathroom pouch.jpg"),
    ("Shoe Bag", "images/Orginizers/shoe bag.jpg"),
    ("Reusable Ziploc", "images/Orginizers/reausable ziploc.jpg"),
    ("Mesh Drawstring", "images/Orginizers/Mesh draw string.jpg"),
]

item_data = [
    ("T-shirt", "images/Items/t shirt.jpg"),
    ("Pant", "images/Items/pant.jpg"),
    ("Shorts", "images/Items/shorts.jpg"),
    ("Undies", "images/Items/undies.jpg"),
    ("Socks", "images/Items/socks.jpg"),
    ("Bra", "images/Items/bra.jpg"),
    ("Hoodie", "images/Items/hoodie.jpg"),
    ("Swimsuit", "images/Items/swimsuit.jpg"),
    ("PJs", "images/Items/pjs.jpg"),
    ("Leo", "images/Items/leo.jpg"),
    ("Laptop", "images/Items/laptop.jpg"),
    ("Charger", "images/Items/charger.jpg"),
    ("Eraser", "images/Items/eraser.jpg"),
    ("Sharpener", "images/Items/sharpnesr.jpg"),
    ("Pencil", "images/Items/pencil.jpg"),
    ("Notebook", "images/Items/notebook.jpg"),
    ("Book", "images/Items/book.jpg"),
    ("Goggles", "images/Items/goggles.jpg"),
    ("Swim Cap", "images/Items/swim cap.jpg"),
    ("Towel", "images/Items/towel.jpg"),
    ("Water Bottle", "images/Items/water bottle.jpg"),
    ("Hair Tie", "images/Items/hair tie.jpg"),
    ("Hairbrush", "images/Items/hairbrush.jpg"),
    ("Teeth Stuff", "images/Items/teeth stuff.jpg"),
    ("Liquids Bottle", "images/Items/liquids bottle.jpg"),
    ("Snack", "images/Items/snack.jpg"),
    ("Fruit", "images/Items/fruit.jpg"),
    ("Shoes", "images/Items/shoes.jpg"),
    ("Slippers", "images/Items/slippers.jpg"),
    ("Toys", "images/Items/toys.jpg"),
    ("Cap", "images/Items/cap.jpg"),
]

all_bags = {name: Bag(name, "any", "big") for name, _ in bag_data}
all_orginizer = {name: Orginizer(name, "any", "medium") for name, _ in org_data}
all_items = {name: Item(name, "any", "small") for name, _ in item_data}

selected_item = None
selected_org = None

PEACH = "#93D6F8"
DARK = "#C293DA"
BUTTON = "#F4B6DC"
HIGHLIGHT = "#ABECD5"

window = tk.Tk()
window.title("Pack It Up!")
window.state("zoomed")
window.configure(bg=PEACH)

photo_refs = {}
def load_photo(path, size):
    img = Image.open(path)
    img = img.resize((size, size))
    return ImageTk.PhotoImage(img)

def make_scrollable_canvas(parent, width, height):
    frame = tk.Frame(parent, bg="white")
    canvas = tk.Canvas(frame, bg="white", width=width, height=height, highlightthickness=1, highlightbackground=DARK)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    def bind_wheel(event):
        canvas.bind_all("<MouseWheel>", on_mousewheel)
    def unbind_wheel(event):
        canvas.unbind_all("<MouseWheel>")
    canvas.bind("<Enter>", bind_wheel)
    canvas.bind("<Leave>", unbind_wheel)
    return frame, canvas

left_frame = tk.Frame(window, bg=PEACH)
left_frame.pack(side="left", fill="y", padx=10, pady=10)
tk.Label(left_frame, text="Bags", font=("Georgia", 18, "bold"), bg=PEACH, fg=DARK).pack(anchor="w")
bags_frame, bags_canvas = make_scrollable_canvas(left_frame, 320, 350)
bags_frame.pack(pady=5)
tk.Label(left_frame, text="Orginizers", font=("Georgia", 18, "bold"), bg=PEACH, fg=DARK).pack(anchor="w", pady=(15,0))
org_frame, org_canvas = make_scrollable_canvas(left_frame, 320, 350)
org_frame.pack(pady=5)

right_frame = tk.Frame(window, bg=PEACH)
right_frame.pack(side="right", fill="y", padx=10, pady=10)
tk.Label(right_frame, text="ITEMS", font=("Georgia", 18, "bold"), bg=PEACH, fg=DARK).pack(anchor="w")
items_frame, items_canvas = make_scrollable_canvas(right_frame, 320, 720)
items_frame.pack(pady=5)

center_frame = tk.Frame(window, bg=PEACH)
center_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
tk.Label(center_frame, text="Pack-It-Up", font=("Georgia", 32, "bold"), bg=PEACH, fg=DARK).pack()
tk.Label(center_frame, text="Click ITEM, then ORGANIZER to pack. Click ORGANIZER, then BAG to pack.",
         font=("Georgia", 11, "italic"), bg=PEACH, fg=DARK).pack(pady=(0,5))
status = tk.Label(center_frame, text="Start by clicking an ITEM!",
                  font=("Georgia", 12, "bold"), bg=PEACH, fg=DARK)
status.pack(pady=5)

workspace_frame = tk.Frame(center_frame, bg="white", highlightthickness=1, highlightbackground=DARK)
workspace_frame.pack(fill="both", expand=True)
workspace_canvas = tk.Canvas(workspace_frame, bg="white", highlightthickness=0)
workspace_scrollbar = tk.Scrollbar(workspace_frame, orient="vertical", command=workspace_canvas.yview)
workspace_canvas.configure(yscrollcommand=workspace_scrollbar.set)
workspace_scrollbar.pack(side="right", fill="y")
workspace_canvas.pack(side="left", fill="both", expand=True)
workspace_inner = tk.Frame(workspace_canvas, bg="white")
workspace_canvas.create_window((0,0), window=workspace_inner, anchor="nw")

def workspace_wheel(event):
    workspace_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
def bind_wheel(event):
    workspace_canvas.bind_all("<MouseWheel>", workspace_wheel)
def unbind_wheel(event):
    workspace_canvas.unbind_all("<MouseWheel>")
workspace_canvas.bind("<Enter>", bind_wheel)
workspace_canvas.bind("<Leave>", unbind_wheel)

pack_button = tk.Button(center_frame, text="Pack it up", font=("Georgia", 16, "bold"),
                        bg=BUTTON, fg="white", padx=40, pady=10, relief="flat")
pack_button.pack(pady=10)

# ===== LIVE WORKSPACE UPDATE =====
def update_workspace():
    for widget in workspace_inner.winfo_children():
        widget.destroy()
    tk.Label(workspace_inner, text="PACKING LIST", font=("Georgia", 18, "bold"), bg="white", fg=DARK).pack(anchor="w", padx=15, pady=10)
    anything_packed = False
    for bag_name, bag in all_bags.items():
        if bag.count() > 0:
            anything_packed = True
            tk.Label(workspace_inner, text=f"{bag_name}", font=("Georgia", 14, "bold"), bg="white", fg=DARK).pack(anchor="w", padx=20, pady=(10,0))
            for org in bag.contents:
                tk.Label(workspace_inner, text=f"{org.name} ({org.count()} items)", font=("Georgia", 12, "bold"), bg="white", fg=DARK).pack(anchor="w", padx=40)
                for item in org.contents:
                    tk.Label(workspace_inner, text=f" • {item.name}", font=("Georgia", 10), bg="white", fg=DARK).pack(anchor="w", padx=60)
    for org_name, org in all_orginizer.items():
        in_a_bag = any(org in b.contents for b in all_bags.values())
        if org.count() > 0 and not in_a_bag:
            anything_packed = True
            tk.Label(workspace_inner, text=f"🧵{org_name} (not in a bag yet)", font=("Georgia", 12, "bold"), bg="white", fg="gray").pack(anchor="w", padx=20, pady=(10,0))
            for item in org.contents:
                tk.Label(workspace_inner, text=f" • {item.name}", font=("Georgia", 10), bg="white", fg="gray").pack(anchor="w", padx=40)
    if not anything_packed:
        tk.Label(workspace_inner, text="Nothing packed yet — start clicking!", font=("Georgia", 12, "italic"), bg="white", fg="gray").pack(pady=30)
    workspace_inner.update_idletasks()
    workspace_canvas.configure(scrollregion=workspace_canvas.bbox("all"))

# ===== CLICK HANDLERS =====
item_highlight_ids = {}
org_highlight_ids = {}

def click_item(name):
    global selected_item
    selected_item = name
    status.config(text=f"Selected: {name} — click an ORGANIZER!")
    for n, hid in item_highlight_ids.items():
        items_canvas.itemconfig(hid, outline="white", width=1)
    items_canvas.itemconfig(item_highlight_ids[name], outline=HIGHLIGHT, width=4)

def click_org(name):
    global selected_item, selected_org
    if selected_item is not None:
        all_orginizer[name].add_item(all_items[selected_item])
        status.config(text=f"Packed {selected_item} into {name}!")
        selected_item = None
        for n, hid in item_highlight_ids.items():
            items_canvas.itemconfig(hid, outline="white", width=1)
        update_workspace()
    else:
        selected_org = name
        status.config(text=f"Selected: {name} — click a BAG!")
        for n, hid in org_highlight_ids.items():
            org_canvas.itemconfig(hid, outline="white", width=1)
        org_canvas.itemconfig(org_highlight_ids[name], outline=HIGHLIGHT, width=4)

def click_bag(name):
    global selected_org
    if selected_org is not None:
        all_bags[name].add_item(all_orginizer[selected_org])
        status.config(text=f"Packed {selected_org} into {name}!")
        selected_org = None
        for n, hid in org_highlight_ids.items():
            org_canvas.itemconfig(hid, outline="white", width=1)
        update_workspace()
    else:
        status.config(text=f"Click an ORGANIZER first to pack into {name}")

BAG_SIZE = 130
for i, (name, path) in enumerate(bag_data):
    col = i % 2
    row = i // 2
    x = 85 + col * 155
    y = 80 + row * 180
    photo = load_photo(path, BAG_SIZE)
    photo_refs[f"bag_{i}"] = photo
    img_id = bags_canvas.create_image(x, y, image=photo)
    bags_canvas.create_text(x, y+80, text=name, font=("Georgia", 10, "bold"), fill=DARK)
    bags_canvas.tag_bind(img_id, "<Button-1>", lambda e, n=name: click_bag(n))
bags_canvas.configure(scrollregion=(0, 0, 320, 80 + ((len(bag_data)+1)//2) * 180))

ORG_SIZE = 110
for i, (name, path) in enumerate(org_data):
    col = i % 2
    row = i // 2
    x = 85 + col * 155
    y = 70 + row * 160
    photo = load_photo(path, ORG_SIZE)
    photo_refs[f"org_{i}"] = photo
    rect = org_canvas.create_rectangle(x-60, y-60, x+60, y+60, outline="white", width=1)
    org_highlight_ids[name] = rect
    img_id = org_canvas.create_image(x, y, image=photo)
    org_canvas.create_text(x, y+70, text=name, font=("Georgia", 9, "bold"), fill=DARK)
    org_canvas.tag_bind(img_id, "<Button-1>", lambda e, n=name: click_org(n))
org_canvas.configure(scrollregion=(0, 0, 320, 70 + ((len(org_data)+1)//2) * 160))

ITEM_SIZE = 100
for i, (name, path) in enumerate(item_data):
    col = i % 2
    row = i // 2
    x = 85 + col * 155
    y = 65 + row * 145
    photo = load_photo(path, ITEM_SIZE)
    photo_refs[f"item_{i}"] = photo
    rect = items_canvas.create_rectangle(x-55, y-55, x+55, y+55, outline="white", width=1)
    item_highlight_ids[name] = rect
    img_id = items_canvas.create_image(x, y, image=photo)
    items_canvas.create_text(x, y+65, text=name, font=("Georgia", 9, "bold"), fill=DARK)
    items_canvas.tag_bind(img_id, "<Button-1>", lambda e, n=name: click_item(n))
items_canvas.configure(scrollregion=(0, 0, 320, 65 + ((len(item_data)+1)//2) * 145))

def pack_it_up_celebration():
    total_items = sum(sum(org.count() for org in bag.contents) for bag in all_bags.values())
    total_orgs = sum(bag.count() for bag in all_bags.values())
    popup = tk.Toplevel(window)
    popup.title("ALL PACKED!")
    popup.geometry("400x200")
    popup.configure(bg=PEACH)
    tk.Label(popup, text="ALL PACKED!", font=("Georgia", 24, "bold"), bg=PEACH, fg=DARK).pack(pady=20)
    tk.Label(popup, text=f"{total_orgs} organizers packed", font=("Georgia", 14), bg=PEACH, fg=DARK).pack()
    tk.Label(popup, text=f"{total_items} items packed", font=("Georgia", 14), bg=PEACH, fg=DARK).pack()
    tk.Label(popup, text="Mom will be so happy!", font=("Georgia", 12, "italic"), bg=PEACH, fg=DARK).pack(pady=10)

pack_button.config(command=pack_it_up_celebration)

update_workspace()
