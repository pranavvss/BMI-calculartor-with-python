import tkinter as tk
from tkinter import ttk

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def update_bmi_display(val):
    height = float(val)
    bmi = calculate_bmi(weight_var.get(), height)
    bmi_label.config(text=str(bmi))
    height_label.config(text=f"{height:.2f}m")

def increment_weight():
    weight_var.set(weight_var.get() + 1)
    update_bmi_display(height_slider.get())

def decrement_weight():
    weight_var.set(weight_var.get() - 1)
    update_bmi_display(height_slider.get())

# Function to create rounded rectangles on a canvas
def create_rounded_rect(canvas, x1, y1, x2, y2, r, **kwargs):
    points = [x1+r, y1,
              x1+r, y1,
              x2-r, y1,
              x2-r, y1,
              x2, y1,
              x2, y1+r,
              x2, y1+r,
              x2, y2-r,
              x2, y2-r,
              x2, y2,
              x2-r, y2,
              x2-r, y2,
              x1+r, y2,
              x1+r, y2,
              x1, y2,
              x1, y2-r,
              x1, y2-r,
              x1, y1+r,
              x1, y1+r,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# Initialize main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x350")
root.configure(bg="#3CB7A9")
root.resizable(False, False)

# Styling variables
font_large = ("Helvetica", 60, "bold")
font_small = ("Helvetica", 14)
font_medium = ("Helvetica", 18)
button_bg = "#E8E8E8"
button_fg = "#000000"
button_active_bg = "#D0D0D0"
slider_bg = "#FFFFFF"
slider_fg = "#3CB7A9"  # Match with the main background for a clean look

# Apply custom style for the slider
style = ttk.Style()
style.configure("TScale", background=slider_bg, troughcolor=slider_bg)

# BMI display
bmi_label = tk.Label(root, text="22.49", font=font_large, bg="#3CB7A9", fg="white")
bmi_label.pack(pady=20)

# Weight control frame
weight_frame = tk.Frame(root, bg="#3CB7A9")
weight_frame.pack(pady=10)

# Weight control buttons and label
weight_var = tk.IntVar(value=70)
decrement_button = tk.Button(weight_frame, text="-", font=font_medium, command=decrement_weight, bg=button_bg, fg=button_fg, activebackground=button_active_bg, width=3, height=1, relief="flat")
decrement_button.pack(side=tk.LEFT, padx=10)

weight_label = tk.Label(weight_frame, textvariable=weight_var, font=font_medium, bg=button_bg, fg=button_fg, width=5, height=2, relief="flat")
weight_label.pack(side=tk.LEFT, padx=10)

increment_button = tk.Button(weight_frame, text="+", font=font_medium, command=increment_weight, bg=button_bg, fg=button_fg, activebackground=button_active_bg, width=3, height=1, relief="flat")
increment_button.pack(side=tk.LEFT, padx=10)

# Height slider container with rounded corners
height_container = tk.Canvas(root, bg="#3CB7A9", highlightthickness=0)
height_container.pack(pady=20, padx=20, fill="x")

# Draw rounded rectangle for the slider container
corner_radius = 15
width = 260
height = 50
x0 = 20
y0 = 20
create_rounded_rect(height_container, x0, y0, x0 + width, y0 + height, corner_radius, fill=slider_bg, outline="")

# Adding the slider and height label within the container
height_slider = ttk.Scale(height_container, from_=1.0, to=2.5, orient="horizontal", length=180, command=update_bmi_display, style="TScale")
height_slider.place(x=x0 + 20, y=y0 + 10)

height_label = tk.Label(height_container, text="1.80m", font=font_small, bg=slider_bg, fg=button_fg)
height_label.place(x=x0 + 190, y=y0 + 8)

# Metric label
metric_label = tk.Label(root, text="metric", font=font_small, bg="#3CB7A9", fg="white")
metric_label.place(x=250, y=5)

root.mainloop()
